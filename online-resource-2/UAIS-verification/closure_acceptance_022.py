from pathlib import Path
import json,hashlib,datetime,copy
R=Path(__file__).resolve().parent
BUILD=R/'closure-0.2.2';RUN=BUILD/'runs/20260913T030324Z-075d96fc';OUT=R/'closure-assessment-022';OUT.mkdir(exist_ok=False)
def dump(n,x):(OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8')
criteria=json.loads((R/'assessment-1/audit_manifest.json').read_text(encoding='utf-8'))
dump('audit_manifest.json',{'Version':criteria['Version'],'CriteriaUnchanged':criteria,'ExecutionDate':datetime.datetime.now(datetime.timezone.utc).isoformat(),'CodeSHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'ImplementationBuildID':'UAIS-CORE-0.2.2'})
records=[json.loads(x) for x in (RUN/'records.jsonl').read_text(encoding='utf-8').splitlines()];traces=[json.loads(x) for x in (RUN/'traces.jsonl').read_text(encoding='utf-8').splitlines()];by={r['TraceID']:r for r in traces}
def check(ts):
 missing=[];lookup={r['TraceID']:r for r in ts}
 for r in ts:
  for p in r['Parents']:
   if p not in lookup:missing.append('dangling parent')
  if not all(r.get(k) for k in ['SpecificationVersion','CatalogueVersion','ServiceManifestVersion','BuildVersion']):missing.append('version linkage')
  if r['Stage']=='Resolver' and 'plans' not in r:missing.append('resolver inputs')
  if r['Stage']=='Admission':
   if 'invariants' not in r or len(r['invariants'])!=5:missing.append('invariants')
   if 'snapshot_tokens' not in r or 'current_tokens' not in r:missing.append('tokens')
 for r in ts:
  if r['Stage']=='Result':
   found=set();todo=[r['TraceID']]
   while todo:
    k=todo.pop()
    if k in found or k not in lookup:continue
    found.add(k);todo.extend(lookup[k]['Parents'])
   ancestors=[lookup[k] for k in found];stages={k['Stage'] for k in ancestors}
   if not set(['Observation','Context','C-N','Need','N-R','Rule','Action','Resolver','Admission','Result'])<=stages:missing.append('chain')
   for stage in ['C-N','N-R']:
    if not any(a['Stage']==stage and a.get('truth') is True for a in ancestors):missing.append('true edge provenance')
 return sorted(set(missing))
out=[]
for c in records:
 if not c['TestCaseID'].startswith('TRACE/'):continue
 ts=[by[i] for i in c['RelevantTraceIDs']];missing=check(ts)
 if c['Input']['branch'].startswith('defer'):
  latest=[r for r in ts if r['Stage']=='Result'][-1]
  if not any(d.get('lifecycle')=='superseded' and d.get('successor')=='d2' for d in latest['S']['deferred']):missing.append('supersession')
 out.append({'TestCaseID':'ACCEPT/'+c['TestCaseID'],'ExpectedOutcome':{'missing_required_fields':[]},'ObservedOutcome':{'missing_required_fields':missing},'Status':'Fail' if missing else 'Pass','RelevantTraceIDs':c['RelevantTraceIDs'],'RequiredStages':10,'CompleteStages':len(set(r['Stage'] for r in ts)&set(['Observation','Context','C-N','Need','N-R','Rule','Action','Resolver','Admission','Result']))})
# Negative controls demonstrate that the acceptance checker rejects removed required evidence.
base=[by[i] for i in next(c for c in records if c['TestCaseID']=='TRACE/applied')['RelevantTraceIDs']]
controls=[]
for name in ['version','token','parent']:
 ts=copy.deepcopy(base)
 if name=='version':ts[0].pop('CatalogueVersion')
 elif name=='token':next(r for r in ts if r['Stage']=='Admission').pop('current_tokens')
 else:next(r for r in ts if r['Stage']=='Result')['Parents']=['absent-record']
 missing=check(ts);controls.append({'Control':name,'Expected':'reject missing evidence','ObservedMissing':missing,'Status':'Pass' if missing else 'Fail'})
dump('trace_acceptance_records.json',out);dump('audit_negative_controls.json',controls)
print(json.dumps({'acceptance_pass':sum(x['Status']=='Pass' for x in out),'acceptance_fail':sum(x['Status']=='Fail' for x in out),'negative_controls_pass':sum(x['Status']=='Pass' for x in controls)}))

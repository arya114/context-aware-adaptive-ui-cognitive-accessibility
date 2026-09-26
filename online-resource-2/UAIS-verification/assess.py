"""Independent post-run acceptance audit; preserves the original run.
The stricter trace checks implement TRACE-CD1/TRACE-CAT1 requirements that
the first runner's stage-presence checker does not test. No oracle changed.
"""
from pathlib import Path
import json,hashlib,datetime,collections
R=Path(__file__).resolve().parent
RUN=R/'runs/20260913T022049Z-e0dd89d1'
OUT=R/'assessment-1'
OUT.mkdir(exist_ok=False)
def dump(n,x):(OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8')
# Freeze the audit rules before reading execution records.
criteria={'Version':'UAIS-TRACE-ACCEPTANCE-1.0','Expected':'All eight representative trace scenarios have version, scoped need provenance, actual resolver witnesses, admission and resulting-state links. Missing required fields fail acceptance.','Source':'specs/UAIS_Section3_Final_Completion_Decisions.md; specs/UAIS_Final_Action_Catalogue.md','checks':['recorded specification/catalogue/service version available in trace or linked envelope','all selected action candidates have need/rule ancestors','every Resolver record retains actual plan inputs and comparator witnesses or explicit non-comparison reason','execution admission records have invariant vector and current version-token comparison','deferred successors identify and supersede their predecessor'], 'FrozenAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'AuditCodeSHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
dump('audit_manifest.json',criteria)
records=[json.loads(x) for x in (RUN/'records.jsonl').read_text(encoding='utf-8').splitlines()]
traces=[json.loads(x) for x in (RUN/'traces.jsonl').read_text(encoding='utf-8').splitlines()];by={x['TraceID']:x for x in traces}
results=[]
for case in records:
 if not case['TestCaseID'].startswith('TRACE/'):continue
 ts=[by[i] for i in case['RelevantTraceIDs']];missing=[]
 # The case envelope supplies spec/build version, but neither service nor catalogue version links.
 if 'CatalogueVersion' not in case or 'ServiceManifestVersion' not in case:missing.append('catalogue/service version absent from per-case envelope and trace records')
 for r in ts:
  if r['Stage']=='Resolver':
   if 'plans' not in r:missing.append(r['TraceID']+': resolver plan inputs/typed effects absent')
  if r['Stage']=='Admission':
   if 'invariants' not in r:missing.append(r['TraceID']+': invariant vector absent')
   if 'snapshot_tokens' not in r or 'current_tokens' not in r:missing.append(r['TraceID']+': explicit commit-token comparison absent')
 if case['Input']['branch'].startswith('defer'):
  missing.append('predecessor retained but no recorded superseded lifecycle mutation')
 results.append({'TestCaseID':'ACCEPT/'+case['TestCaseID'],'ParentCaseID':'V3-06','Oracle':['End-to-End'],'InputTraceCase':case['TestCaseID'],'RelevantTraceIDs':case['RelevantTraceIDs'],'ExpectedOutcome':{'missing_required_fields':[]},'ObservedOutcome':{'missing_required_fields':missing},'Status':'Fail' if missing else 'Pass','FailureClass':'implementation/instrumentation defect' if missing else None})
dump('trace_acceptance_records.json',results)
parents=json.loads((R/'parent_inventory.json').read_text(encoding='utf-8'))
pc=collections.Counter(r['ParentCaseID'] for r in records if r['Status']!='Not run')
fc=collections.Counter(r['ChildFamilyID'] for r in records if r['Status']!='Not run' and r['ChildFamilyID'])
coverage={'parents_with_executed_instances':len(pc),'historical_parent_count':35,'parents_without_explicit_instances':[p for p in parents['historical_parent_ids'] if p not in pc],'current_families_with_instances':len(fc),'current_family_count':44,'families_without_explicit_instances':[p for p in parents['current_children'] if p not in fc],'warning':'A linked instance does not establish full branch, scope, parameter, guard or effect coverage of its family.'}
dump('coverage.json',coverage)
defects=[
{'DefectID':'IMPL-001','Class':'implementation defect','Component':'trace instrumentation','Evidence':'All eight strict acceptance records identify missing catalogue/service version linkage, actual resolver plan witnesses and/or commit-token comparison.','Status':'OPEN','Change':'None; original execution retained','Retest':'Not performed'},
{'DefectID':'HARNESS-001','Class':'implementation defect','Component':'runner trace oracle','Evidence':'Eight initial TRACE cases passed stage/parent-presence checking but fail the required-field acceptance audit.','Status':'OPEN','Change':'Independent stricter acceptance audit added without editing original expected outcomes or first-run verdicts','Retest':'Eight acceptance failures; original eight stage-presence passes retained as superseded for acceptance'},
{'DefectID':'COVERAGE-001','Class':'coverage gap','Component':'contract semantics and browser boundary','Evidence':'Five explicit not-run entries plus incomplete full-contract scope/effect coverage; family-mask test is a projection rather than end-to-end nomination.','Status':'OPEN'},
{'DefectID':'COVERAGE-002','Class':'coverage gap','Component':'case traceability','Evidence':coverage,'Status':'OPEN'},
{'DefectID':'IMPL-LIMIT-001','Class':'implementation limitation','Component':'canonical key','Evidence':'Known restricted implementation compares NFC strings rather than the full typed tuple, decimal and set-normalisation domain. This is the GAP/canonical-typed-domain not-run entry.','Status':'OPEN'}]
dump('defect_retest_register.json',{'SpecificationDefectsDiscovered':0,'ConfirmedImplementationDefects':2,'ImplementationLimitations':1,'Entries':defects,'Note':'No claim of zero undiscovered defects. No fixes or successful retests are claimed.'})
print(json.dumps({'trace_acceptance':collections.Counter(x['Status'] for x in results),'coverage':coverage}))

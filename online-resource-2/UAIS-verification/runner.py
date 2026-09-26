"""Run frozen cases once into a unique immutable run directory.
Compare observed objects to independently frozen expected objects.
"""
from pathlib import Path
from copy import deepcopy
import json,hashlib,datetime,uuid,traceback
import model as m
R=Path(__file__).resolve().parent

def normal_decision(t,need='N2',scope='ST04',predecessor=None):
 kinds={'N1':'clarification','N2':'step-guidance','N3':'orientation','N4':'reminder','N5':'choice','N6':'correction'}
 if need=='N7':ev=[['C3.1','N7',{'base':True,'relevant':True}]]
 else:ev=[['C1.3',need,{'state':'AssistanceNeeded','quality':'known','kind':kinds[need],'relevant':True}]]
 conditions={f'{need}→R{i}':True for i in range(1,5)}
 return m.decision(ev,conditions,t,scope,predecessor)

def ready_action(aid,t,d=None,branch='target'):
 c=m.contracts()[aid];need=next(iter(c['NeedCoverage']['declared']))
 d=d or normal_decision(t,need)
 x={'facts':{k:True for k in m.REQUIRES[aid]}}
 if branch=='exclusion':x['facts'][m.REQUIRES[aid][0]]=False
 elif branch=='unknown':x['facts'][m.REQUIRES[aid][0]]=None
 elif branch=='wait':x['blocker']='scoped edit completion'
 elif branch=='illegal':x['variant']='UNLISTED'
 elif branch=='no-need':d={**d,'rules':{}}
 return m.candidate(aid,d,x,t)

def trace_check(records):
 # Independent structural auditor: traverses actual parents and checks edge truths.
 by={r['TraceID']:r for r in records};missing=[]
 for r in records:
  for p in r['Parents']:
   if p not in by:missing.append('dangling:'+p)
 required=['Observation','Context','C-N','Need','N-R','Rule','Action','Resolver','Admission','Result']
 results=[r for r in records if r['Stage']=='Result']
 if not results:missing.append('Result')
 for result in results:
  seen=set();todo=[result['TraceID']]
  while todo:
   i=todo.pop()
   if i in seen or i not in by:continue
   seen.add(i);todo.extend(by[i]['Parents'])
  ancestors=[by[i] for i in seen];stages={r['Stage'] for r in ancestors}
  missing.extend(k for k in required if k not in stages)
  for stage in ['C-N','N-R']:
   if not any(r['Stage']==stage and r.get('truth') is True for r in ancestors):missing.append(stage+':no true provenance')
 return {'complete':not missing,'missing':sorted(set(missing))}

def transaction(x,t,s,u):
 ledger=m.Ledger(x['status']);before=ledger.effects
 d=m.decision([['C3.1','N6',{'base':True,'relevant':True}],['C3.2','N7',{'base':True,'relevant':True}]],{'N7→R4':True},t,'X/status-determination')
 a=ready_action('R3.A7',t,d);r=m.resolve([{'id':'query','valid':True,'feasibility':a['status'],'coverage':['N6/X/status-determination','N7/X/status-determination'],'disruption':[],'stability':[],'changes':1}],t,[a['trace']])
 m.apply(u,s,{'P':{'transaction.reconciliation':'guarded-query'}},'tx-query',t,r['trace'])
 response=ledger.query('trigger1')
 response_id=t.add('ObservationLogger','ServiceResponse',input=response,source='simulated-ledger',ledger_before=before,ledger_after=ledger.effects,read_only=ledger.effects==before)
 valid=m.accept_response(s,response)
 # A new full decision follows accepted evidence; no callback directly invokes retry.
 d2=m.decision([['C3.3','N6',{'base':True,'relevant':True}],['C3.3','N7',{'base':True,'relevant':True}]],{'N7→R4':True},t,'X/permitted-retry',predecessor=d['trace'])
 t.records[-1]['Parents'].append(response_id)
 facts={k:True for k in m.REQUIRES['R3.A2']}
 if x['status']!='safely_retryable':facts['retry_permit']=None
 a2=m.candidate('R3.A2',d2,{'facts':facts},t)
 r2=m.resolve([{'id':'retry','valid':True,'feasibility':a2['status'],'coverage':['N6/X/permitted-retry'],'disruption':[],'stability':[],'changes':0}],t,[a2['trace']])
 admitted=a2['status']=='READY' and valid and bool(r2['selected'])
 admission_id=t.add('ActionExecutionLogger','Admission',[r2['trace']],admitted=admitted,permit=response.get('permit') if response else None)
 retried=ledger.retry(response,mediated=admitted)
 tid=t.add('ActionExecutionLogger','TransactionCommand',[admission_id],command='retry' if retried else 'withheld',permit=response.get('permit') if response else None,attempts=ledger.attempts,identities=1,effects=ledger.effects)
 t.add('ActionExecutionLogger','Result',[tid],U=deepcopy(u),S=deepcopy(s),operation='retry' if retried else 'withheld')
 second=ledger.retry(response,mediated=admitted)
 if second:raise AssertionError('duplicate permit dispatched')
 ledger.query('trigger1');ledger.query('derived-failure',origin='query')
 return {'status':s['transaction']['status'],'retry':retried,'attempts':ledger.attempts,'identities':1,'effects':ledger.effects,'queries':ledger.queries,'direct_retry':False}

def execute(case,t,s,u):
 x=case['Input'];kind=case['Kind']
 if kind=='classification':
  oid=t.add('ObservationLogger','Observation',input=x)
  value=m.classify(x['classifier'],x);t.add('ObservationLogger','Context',[oid],result=value);return value
 if kind=='assistance':
  machine=m.Assistance(x['known']);out=[]
  for e in x['events']:
   oid=t.add('ObservationLogger','Observation',input=e);v=machine.event(e);out.append(v);t.add('ObservationLogger','Context',[oid],result=v)
  return out
 if kind=='risk':
  machine=m.Risk();out=[]
  for p in x['pairs']:
   oid=t.add('ObservationLogger','Observation',input=p);v=machine.pair(*p);out.append(v);t.add('ObservationLogger','Context',[oid],result=v)
  return out
 if kind=='cn':
  oid=t.add('ObservationLogger','Observation',input=x);v=m.edge_cn(x['c'],x['n'],x['witness']);t.add('DecisionTraceLogger','C-N',[oid],edge=x['c']+'→'+x['n'],truth=v);return v
 if kind=='nr':
  oid=t.add('DecisionTraceLogger','Need',need=x['n'],active=x['active']);v=m.edge_nr(x['n'],x['r'],x['active'],x['condition']);t.add('DecisionTraceLogger','N-R',[oid],edge=x['n']+'→'+x['r'],truth=v);return v
 if kind=='action':
  a=ready_action(x['action'],t,branch=x['branch']);return {k:a[k] for k in ['status','operation']}
 if kind in ['legal','legal_variant']:
  c=m.contracts()[x['action']]
  value=x['value'] in c['Legal parameters/values'][x['parameter']] if kind=='legal' else x['variant'] in [v['VariantID'] for v in c['PermittedTransformations']]
  t.add('DecisionTraceLogger','RegistryCheck',input=x,result=value);return value
 if kind=='resolver':
  r=m.resolve(x['plans'],t);return {k:r[k] for k in ['selected','operation']}
 if kind=='compose':
  r=m.compose(x['actions'],x);t.add('DecisionTraceLogger','Resolver',input=x,result=r);return r
 if kind=='reduce':
  r=m.reduce_scope(x['selected'],x['protected']);t.add('DecisionTraceLogger','Resolver',input=x,result=r);return r
 if kind=='combinations':
  # Projection deliberately labelled partial in inventory; not an end-to-end nomination oracle.
  selected=[r for i,r in enumerate(['R1','R2','R3','R4']) if x['mask']&(1<<i)]
  t.add('DecisionTraceLogger','FamilyFilter',mask=x['mask'],selected=selected);return selected
 if kind=='state':
  d=normal_decision(t);a=ready_action('R4.A1',t,d)
  r=m.resolve([{'id':'stage','valid':True,'feasibility':'READY','coverage':['N2/ST04'],'disruption':[],'stability':[],'changes':1}],t,[a['trace']])
  if x['branch']=='active':s['active']={'field':'FLD05','buffer':'unfinished','selection':[2,4],'composition':True}
  target=deepcopy(u) if x['branch']=='same' else {'F':{'flow':'staged'}}
  return m.apply(u,s,target,'decision1',t,r['trace'],structural=True,snapshot=0 if x['branch']=='stale' else s['version'],inject_failure=x['branch']=='rollback')
 if kind=='invariant':
  after=deepcopy(s);ch=x['changed']
  if ch=='values':after['values'].pop('FLD05')
  elif ch=='step':after['step']='ST07'
  elif ch=='active':after['active']={'field':'FLD05','buffer':'lost'}
  elif ch=='transaction':after['transaction']['status']='completed'
  v=m.invariants(s,after,x.get('hidden',[]));t.add('ActionExecutionLogger','InvariantProbe',before=s,proposed=after,result=v,applied=False);return v
 if kind=='transaction':return transaction(x,t,s,u)
 if kind=='response':
  ledger=m.Ledger('completed');response=ledger.query('q',identity=x.get('identity','X'),revision=x.get('revision'));v=m.accept_response(s,response);t.add('ActionExecutionLogger','ResponseAdmission',input=response,accepted=v,result=s);return v
 if kind=='query':
  ledger=m.Ledger('unknown');ledger.query('q1')
  if x['branch']=='duplicate':ledger.query('q1')
  elif x['branch']=='self':ledger.query('failure',origin='query')
  else:ledger.query('q2')
  t.add('ActionExecutionLogger','QueryCommands',count=ledger.queries,branch=x['branch']);return ledger.queries
 if kind=='resume':
  draft={'owner':'synthetic','service_version':'1.0.0','values':deepcopy(s['values'])}
  if x['conflict']:draft['values']['FLD05']='conflicting value'
  v=m.restore(s,draft,x['authorised']);t.add('ActionExecutionLogger','DraftRestore',accepted=v,result=s);return v
 if kind=='baseline':
  ledger=m.Ledger('safely_retryable');r=ledger.query('baseline-query');ledger.retry(r);second=ledger.retry(r);t.add('ActionExecutionLogger','BaselineSafety',origin='baseline_safety',mode=x['mode'],effects=ledger.effects);return {'effects':ledger.effects,'second_retry':second}
 if kind=='trace':
  b=x['branch']
  if b=='transaction':transaction({'status':'safely_retryable'},t,s,u);return trace_check(t.records)
  d=normal_decision(t);a=ready_action('R4.A1',t,d)
  status='UNKNOWN' if b=='unknown' else 'BLOCKED' if b=='suppress' else 'READY'
  r=m.resolve([{'id':'stage','valid':True,'feasibility':status,'coverage':['N2/ST04'],'disruption':[],'stability':[],'changes':1}],t,[a['trace']])
  if b in ['combine','transform']:
   ids=['R1.A2','R3.A1'] if b=='combine' else ['R1.A3','R4.A2']
   aa=[ready_action(aid,t) for aid in ids]
   rr=m.compose(ids,{'facts':{'same_identity':True}})
   r['trace']=t.add('DecisionTraceLogger','Resolver',[a['trace'] for a in aa],result=rr)
  if b.startswith('defer'):s['active']={'field':'FLD05','buffer':'partial','selection':[0,3],'composition':True}
  if b in ['suppress','unknown']:
   admit=t.add('ActionExecutionLogger','Admission',[r['trace']],admitted=False,reason=status)
   t.add('ActionExecutionLogger','Result',[admit],U=u,S=s,operation=r['operation'])
  else:m.apply(u,s,{'F':{'flow':'staged'}},'d1',t,r['trace'],structural=True)
  if b.startswith('defer'):
   s['active']=None;s['version']+=1
   d2=normal_decision(t,predecessor=d['trace']);a2=ready_action('R4.A1',t,d2)
   r2=m.resolve([{'id':'stage2','valid':True,'feasibility':'READY' if b=='defer-execute' else 'BLOCKED','coverage':['N2/ST04'],'disruption':[],'stability':[],'changes':1}],t,[a2['trace']])
   if b=='defer-execute':m.apply(u,s,{'F':{'flow':'staged'}},'d2',t,r2['trace'],snapshot=s['version'],predecessor='d1')
   else:
    eid=t.add('ActionExecutionLogger','Admission',[r2['trace']],admitted=False,predecessor='d1');t.add('ActionExecutionLogger','Result',[eid],U=u,S=s,operation='SUPPRESS')
  return trace_check(t.records)
 raise ValueError(kind)

def main():
 manifest=json.loads((R/'execution_manifest.json').read_text(encoding='utf-8'))
 for name,digest in manifest['hashes'].items():
  if hashlib.sha256((R/name).read_bytes()).hexdigest()!=digest:raise RuntimeError('Frozen input changed: '+name)
 cases=json.loads((R/'inventory.json').read_text(encoding='utf-8'));expected=json.loads((R/'expected.json').read_text(encoding='utf-8'))
 runid=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:8];folder=R/'runs'/runid;folder.mkdir(parents=True,exist_ok=False)
 records=[];traces=[]
 for case in cases:
  cid=case['TestCaseID'];t=m.Trace(runid+'/'+cid);s=m.initial_state();u=deepcopy(case['InitialU']);initial=deepcopy(s);reason=None;observed=None
  if case['Kind']=='not_run':status='Not run';reason=case['Input']['reason']
  else:
   try:observed=execute(case,t,s,u);status='Pass' if observed==expected[cid] else 'Fail';reason=None if status=='Pass' else 'Observed object differs from frozen oracle'
   except Exception:status='Fail';reason=traceback.format_exc()
  records.append({**case,'ExecutionID':runid+'/'+cid,'RunID':runid,'InitialS':initial,'ExpectedOutcome':expected[cid],'ObservedOutcome':observed,'Status':status,'RelevantTraceIDs':[r['TraceID'] for r in t.records],'FailureReason':reason,'SpecificationVersion':manifest['SpecificationVersion'],'BuildVersion':manifest['ImplementationBuildID']})
  traces.extend(t.records)
 for name,rows in [('records.jsonl',records),('traces.jsonl',traces)]:
  with (folder/name).open('w',encoding='utf-8') as f:
   for row in rows:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 summary={k:sum(r['Status']==k for r in records) for k in ['Pass','Fail','Unresolved','Not run']}
 (folder/'run.json').write_text(json.dumps({'RunID':runid,'ManifestSHA256':hashlib.sha256((R/'execution_manifest.json').read_bytes()).hexdigest(),'counts':summary},indent=2),encoding='utf-8')
 print(json.dumps({'run':str(folder),'counts':summary}))
if __name__=='__main__':main()

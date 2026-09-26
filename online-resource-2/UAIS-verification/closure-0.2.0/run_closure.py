from pathlib import Path
from copy import deepcopy
import json,hashlib,datetime,uuid,traceback
import model as m
import semantic as sem
import runner
R=Path(__file__).resolve().parent

def postconditions(aid,f,out,before):
 s0=before['S'];v=f['view'];s=f['S'];cmd=f['commands'];checks={}
 checks['values_preserved']=s['values']==s0['values']
 checks['step_progress_preserved']=s['step']==s0['step'] and s['valid']==s0['valid']
 checks['input_preserved']=s['active']==s0['active']
 checks['configuration_invariants']=out['invariants']==[True]*5
 checks['command_identity_unchanged']=all(s['transaction'][k]==s0['transaction'][k] for k in ['id','key','operation','payload','authorised'])
 checks['required_routes']=all(k in f['graph']['root'] for k in ['error','status','recovery','navigation','submit-explanation'])
 if aid=='R1.A1':checks['instruction_content']=v['instructions']==[before['content']['INFO-ST04']]
 elif aid=='R1.A2':checks['correct_definition']=v['definition']==before['content']['TERM01'] and bool(v['definition_route'])
 elif aid=='R1.A3':checks['actual_step_cue']=v['cue']['current']==s0['step'] and v['cue']['next']=='ST05'
 elif aid=='R1.A4':checks['example_identity']=v['example']==before['content']['EX-FLD05'] and v['example_contents']==['EX-FLD05']
 elif aid=='R1.A5':checks['help_semantics']=v['help']==['standard','typed-request'] and v['preview_confirms_need'] is False
 elif aid=='R1.A6':checks['error_identity_truth']=v['error']['id']=='VAL06' and v['error']['valid']==before['validation']['VAL06'] and bool(v['error']['instruction'])
 elif aid=='R2.A1':checks['essential_content']=set(v['essential'])==set(before['graph']['root']+['INFO-ST04'])
 elif aid=='R2.A2':checks['independent_scopes']=f['elements']=={'OPT01':'collapsed','OPT02':'shown','error':'shown'}
 elif aid=='R2.A3':checks['members_dependencies']=sorted(x for group in v['groups'] for x in group)==sorted(before['members']) and v['dependencies']==before['dependencies']
 elif aid=='R2.A4':checks['valid_control']=v['primary']=='ST04/next' and not cmd
 elif aid=='R2.A5':checks['requirements_truth']=v['checklist']==before['requirements'] and set(v['full_requirement_routes'])==set(before['requirements'])
 elif aid=='R3.A1':checks['persisted_accepted_snapshot']=f['saved']=={'values':s0['values'],'source_version':s0['draft']['version'],'owner':s0['draft']['owner']}
 elif aid=='R3.A2':checks['guarded_same_identity_retry']=cmd[0]['result']=={'dispatched':True,'permit_consumed':True,'attempts':2,'effects':1,'identity':'X'} and s['transaction']['status']=='safely_retryable'
 elif aid=='R3.A3':checks['essential_asset_ids']=v['asset_contents']==['INFO-ST04']
 elif aid=='R3.A4':checks['honest_recovery']=v['recovery']['status']==s0['transaction']['status'] and v['recovery']['controls']==['status-check'] and not cmd
 elif aid=='R3.A5':checks['honest_feedback']=v['feedback']==s0['transaction']['status'] and not cmd and s['transaction']==s0['transaction']
 elif aid=='R3.A6':checks['authorised_lossless_resume']=cmd[0]['result']['restored'] is True and cmd[0]['result']['values']==s0['values'] and cmd[0]['result']['source_version']==s0['draft']['version']
 elif aid=='R3.A7':
  c=cmd[0]['result'];checks['readonly_new_evidence']=c['queries']==1 and c['attempts']==1 and c['effects']==0 and c['before_status']=='unknown' and c['after_status']=='safely_retryable'
 elif aid=='R4.A1':checks['logical_stage_binding']=v['stage']=={'logical':s0['step'],'fields':['FLD04','FLD05'],'document':'DOC01'}
 elif aid=='R4.A2':checks['actual_progress']=v['progress']=={'current':s0['step'],'satisfied':s0['valid']}
 elif aid=='R4.A3':checks['existing_validation']=v['validation']=={f'VAL{i:02}':i<7 for i in range(1,8)} and f['validation']==before['validation']
 elif aid=='R4.A4':checks['faithful_review']=v['review']=={'values':s0['values'],'document':s0['upload']['ref'],'correction':'ST04','status_separate':True}
 elif aid=='R4.A5':checks['legal_navigation']=v['navigation']==[['ST04','ST03'],['ST04','ST05']] and s['step']=='ST04'
 elif aid=='R4.A6':checks['dependency_identity']=v['dependency_cues']==[['FLD04','FLD05']]
 if aid not in ['R3.A1','R3.A2','R3.A6','R3.A7']:checks['no_service_side_effect']=not cmd and s['transaction']==s0['transaction']
 if out.get('variant') in ['shared-progress','shared-cue']:checks['joint_cue_progress']=v['cue']['current']==v['progress']['current']==s0['step']
 if out.get('variant') in ['shared-review','shared-recovery']:checks['separate_review_recovery']=v['review']['status_separate'] and v['recovery']['status']==s0['transaction']['status']
 return checks

def run(c,t):
 x=c['Input'];kind=c['Kind']
 if kind=='key':
  a,b=m.canonical_key(x['left']),m.canonical_key(x['right']);result=(a>b)-(a<b)
  t.add('DecisionTraceLogger','CanonicalComparison',input=x,relation=result);return result,{}
 if kind=='key-reject':
  try:m.canonical_key(x['actions']);r='ACCEPTED'
  except (ValueError,TypeError):r='REJECT_UNKNOWN'
  t.add('DecisionTraceLogger','CanonicalAdmission',input=x,outcome=r);return r,{}
 if kind=='resolve':
  r=m.resolve(x['plans'],t);return {'selected':r['selected'],'operation':r['operation'],'canonical_used':r.get('canonical_used',False)},r
 if kind in ['effect','reject']:
  f=sem.fixture();aid=x['action']
  if aid=='R3.A2':f['S']['transaction'].update(status='safely_retryable',revision=1)
  if aid=='R1.A6':f['validation']['VAL06']=False;f['S']['upload']['state']='rejected'
  before=deepcopy({k:v for k,v in f.items() if k!='ledger'})
  if kind=='reject':
   out=sem.execute(aid,f,t,x['variant'],x['need']);return {'operation':out['disposition'],'unchanged':before['U']==f['U'] and before['S']==f['S']},{'before':before,'after':{k:v for k,v in f.items() if k!='ledger'}}
  out=sem.execute(aid,f,t,x['variant'],x['need']);checks=postconditions(aid,f,out,before)
  p=c['ExpectedOutcome']['property'];observed_value=f['U'][p[0]].get(p)
  checks['declared_property']=observed_value==c['ExpectedOutcome']['value']
  checks['mediated_coverage']=out['coverage']==[x['need']+'@'+sem.SCOPES[aid]]
  checks['trace_reconstruction']=runner.trace_check(t.records)['complete']
  contract=m.contracts()[aid];expected_rule=contract['RuleSource']
  checks['rule_source']=any(r['Stage']=='Rule' and expected_rule in r['rules'] for r in t.records)
  if x['variant']:
   if aid in sem.REALISATIONS:checks['realisation']=f['U'][p[0]][sem.REALISATIONS[aid]]==x['variant']
   checks['permitted_transform']=out['disposition']=='TRANSFORM' and x['variant'] in [v['VariantID'] for v in contract['PermittedTransformations']]
  checks['command_phase_order']=True
  command_indices=[i for i,r in enumerate(t.records) if r['Stage']=='CommandAdmission']
  for i in command_indices:
   checks['command_phase_order'] &= any(r['Stage']=='Result' and r.get('phase')=='configuration' for r in t.records[:i]) and any(r['Stage']=='ServiceEvidence' for r in t.records[i+1:])
  return {'property':p,'value':observed_value,'checks_pass':all(checks.values())},{'checks':checks,'effect':out,'initial':before}
 if kind=='multi':
  f=sem.fixture();rules=set();items=[];dispositions={};mode=x['mode']
  if mode=='deferred':f['S']['active']={'field':'FLD05','buffer':'unfinished','selection':[1,3],'composition':True}
  before=deepcopy(f['S'])
  if not x['components']:t.add('ObservationLogger','Observation',input={'assistance_requests':[],'additional_task_needs':[]},scope='fixture/empty');t.add('ActionExecutionLogger','BaselineSafety',origin='baseline_safety',status=f['S']['transaction']['status'])
  for item in x['components']:
   # Conditions are supplied with explicit object-level support evidence from the frozen scenario.
   t.add('ObservationLogger','SupportConditionWitness',input=item['facts'],scope=item['scope'])
   d=sem.nominate(item['need'],item['scope'],t,item['conditions']);rules.update(d['rules']);aid=item['action']
   variant='within-stage' if mode=='transformed' and aid=='R2.A3' else None
   facts={k:True for k in m.REQUIRES[aid]};args={'facts':facts,'scope':item['scope'],'variant':variant}
   if mode=='suppressed' and aid=='R2.A3':facts['partition_total']=False
   if mode=='deferred' and aid=='R4.A1':args['blocker']='FLD05 edit completion'
   a=m.candidate(aid,d,args,t);items.append((item,d,a,variant))
  # Candidate set is complete before any effect executes; joint resource witness is frozen.
  joint=t.add('DecisionTraceLogger','ConcurrentPlan',[a['trace'] for _,_,a,_ in items],actions=[a['action'] for _,_,a,_ in items],compatibility='distinct typed properties; declared independent scopes except specified grouping/staging branch',mode=mode)
  for item,d,a,variant in items:
   aid=item['action']
   if a['status']!='READY':
    dispositions[aid]=a['operation'];t.add('ActionExecutionLogger','Withheld',[a['trace'],joint],disposition=a['operation'],state=deepcopy(f['S']));continue
   out=sem.execute(aid,f,t,variant,item['need'],d,a);dispositions[aid]=out['disposition']
  preserved=all(m.invariants(before,f['S']))
  return {'rules':sorted(rules),'dispositions':dispositions,'preserved':preserved},{'scope_inputs':x['components'],'U':f['U'],'S':f['S'],'candidate_actions':[a['action'] for _,_,a,_ in items],'joint_plan_trace':joint}
 if kind=='multi_conflict':
  f=sem.fixture();before=deepcopy(f['S']);rules=set();plans=[];items={}
  for item in x['components']:
   aid=item['action'];d=sem.nominate(item['need'],item['scope'],t,item['conditions']);rules.update(d['rules'])
   variant='within-stage' if aid=='R2.A3' and x['mode']=='lower' else None
   a=m.candidate(aid,d,{'scope':item['scope'],'facts':{k:True for k in m.REQUIRES[aid]},'variant':variant},t)
   target=deepcopy(f['U']);p,v=sem.TARGETS[aid];target[p[0]][p]=v
   if variant:target[p[0]][sem.REALISATIONS[aid]]=variant
   changes=sum(target[dim][key]!=f['U'][dim][key] for dim in target for key in target[dim])
   plans.append({'id':aid,'valid':True,'feasibility':a['status'],'coverage':[item['need']+'@'+item['scope']],'disruption':[],'stability':[],'changes':changes,'target':target})
   items[aid]=(item,d,a,variant)
  r=m.resolve(plans,t,[item[2]['trace'] for item in items.values()])
  t.add('DecisionTraceLogger','CoupledScopeConstraint',[r['trace']],exclusive_support_region=x['exclusive_support_region'],unmet=[p['coverage'] for p in plans if p['id'] not in r['selected']])
  for aid in r['selected']:
   item,d,a,variant=items[aid];sem.execute(aid,f,t,variant,item['need'],d,a)
  if not r['selected']:t.add('ActionExecutionLogger','SafeHold',[r['trace']],U=f['U'],S=f['S'],disposition='DEFER')
  return {'rules':sorted(rules),'selected':r['selected'],'operation':r['operation'],'canonical_used':r.get('canonical_used',False),'preserved':all(m.invariants(before,f['S']))},{'plans':plans,'resolver':r,'context_scopes':x['components'],'U':f['U']}
 raise ValueError(kind)

def main():
 manifest=json.loads((R/'execution_manifest.json').read_text(encoding='utf-8'))
 for f,h in manifest['hashes'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h,f
 cases=json.loads((R/'closure_inventory.json').read_text(encoding='utf-8'));expected=json.loads((R/'closure_expected.json').read_text(encoding='utf-8'))
 runid=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:8];folder=R/'closure_runs'/runid;folder.mkdir(parents=True,exist_ok=False);records=[];traces=[]
 for c in cases:
  t=m.Trace(runid+'/'+c['TestCaseID']);detail={};actual=None;error=None
  try:actual,detail=run(c,t);status='Pass' if actual==expected[c['TestCaseID']] else 'Fail'
  except Exception:status='Fail';error=traceback.format_exc()
  records.append({**c,'ObservedOutcome':actual,'Status':status,'FailureReason':error,'Details':detail,'ExecutionID':runid+'/'+c['TestCaseID'],'BuildVersion':manifest['ImplementationBuildID'],'SpecificationVersion':manifest['SpecificationVersion'],'RelevantTraceIDs':[r['TraceID'] for r in t.records]});traces+=t.records
 for name,rows in [('records.jsonl',records),('traces.jsonl',traces)]:
  with (folder/name).open('w',encoding='utf-8') as f:
   for row in rows:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 print(json.dumps({'run':str(folder),'executed':len(records),'pass':sum(c['Status']=='Pass' for c in records),'fail':sum(c['Status']=='Fail' for c in records)}))
if __name__=='__main__':main()

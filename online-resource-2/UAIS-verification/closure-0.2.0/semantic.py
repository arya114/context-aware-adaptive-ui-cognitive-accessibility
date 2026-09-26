"""Concrete semantic renderer/service-action bindings for UAIS-VRI-1.0.
No expected-result imports. Content objects and command results are inspectable.
"""
from copy import deepcopy
import model as m

TARGETS={
'R1.A1':('G.guidance.visibility','contextual'),'R1.A2':('G.term.explanation','inline'),
'R1.A3':('G.step.cue','full'),'R1.A4':('G.example.visibility','on-demand'),'R1.A5':('G.help.access','contextual'),'R1.A6':('G.error.explanation','contextual'),
'R2.A1':('D.layout.density','reduced'),'R2.A2':('D.content.reduction[OPT01].state','collapsed'),'R2.A3':('D.grouping.mode','semantic'),'R2.A4':('D.primary.control.emphasis','emphasized'),'R2.A5':('D.requirements.view','checklist'),
'R3.A1':('P.draft.autosave','on'),'R3.A2':('P.network.retry','guarded-auto'),'R3.A3':('P.asset.profile','low-bandwidth'),'R3.A4':('P.recovery.panel','visible'),'R3.A5':('P.submission.feedback','explicit'),'R3.A6':('P.draft.resume','guided'),'R3.A7':('P.transaction.reconciliation','guarded-query'),
'R4.A1':('F.flow.mode','staged'),'R4.A2':('F.progress.indicator','on'),'R4.A3':('F.validation.timing','step'),'R4.A4':('F.review.summary','on'),'R4.A5':('F.stage.navigation','back-review'),'R4.A6':('F.dependency.cue','visible')}
REALISATIONS={'R1.A3':'G.step.cue.realisation','R1.A4':'G.example.realisation','R2.A3':'D.grouping.realisation','R3.A3':'P.asset.realisation','R3.A4':'P.recovery.realisation','R4.A2':'F.progress.realisation','R4.A4':'F.review.realisation'}
SCOPES={'R1.A1':'INFO-ST04','R1.A2':'TERM01','R1.A3':'ST04','R1.A4':'EX-FLD05','R1.A5':'ST04/help','R1.A6':'VAL06','R2.A1':'ST04/layout','R2.A2':'OPT01','R2.A3':'GROUP-ST04','R2.A4':'ST04/next','R2.A5':'REQ01-REQ03','R3.A1':'d1/persistence','R3.A2':'X/permitted-retry','R3.A3':'ASSET01','R3.A4':'X/recovery-controls','R3.A5':'X/status-communication','R3.A6':'d1/resumption','R3.A7':'X/status-determination','R4.A1':'ST04','R4.A2':'ST04','R4.A3':'VAL06','R4.A4':'REVIEW01','R4.A5':'ST04/navigation','R4.A6':'FLD04-FLD05'}

def fixture():
 s=m.initial_state();s['values']['FLD06']=False
 u={'G':{},'D':{},'P':{},'F':{}}
 defaults=['off','on-demand','compact','hidden','standard','standard','standard','shown','standard','standard','full','on','manual','standard','visible','standard','manual','manual','single-page','off','submit','off','basic','hidden']
 for (aid,(prop,_)),default in zip(TARGETS.items(),defaults):
  u[prop[0]][prop]=default
  if aid in REALISATIONS:u[prop[0]][REALISATIONS[aid]]='native'
 return {'S':s,'U':u,'view':{},'saved':None,'commands':[],
  'content':{'INFO-ST04':'Choose a purpose and attach the synthetic address evidence.','TERM01':'A synthetic document attached for this fixture.','EX-FLD05':'Research demonstration (example only).'},
  'requirements':{'REQ01':True,'REQ02':True,'REQ03':False},'members':['FLD04','FLD05','DOC01'],
  'graph':{'root':['error','status','recovery','navigation','submit-explanation']},'elements':{'OPT01':'shown','OPT02':'shown','error':'shown'},
  'validation':{f'VAL{i:02}':i<7 for i in range(1,8)},'dependencies':[['FLD04','FLD05']], 'navigation':[['ST04','ST03'],['ST04','ST05']], 'partition':[['FLD04','FLD05','DOC01']],
  'asset_content':['INFO-ST04'],'example_content':['EX-FLD05'],'ledger':m.Ledger('safely_retryable')}

def evidence(need,scope):
 if need=='N7':return ['C3.1',need,{'base':True,'relevant':True,'request':'OP01','classification':'Poor','scope':scope}]
 k=m.KINDS[int(need[1:])-1]
 return ['C1.3',need,{'state':'AssistanceNeeded','quality':'known','kind':k,'scope_ok':True,'relevant':True,'request':'help-'+scope}]

def nominate(need,scope,trace,conditions=None):
 # Every non-primary edge has its own manifest/scenario evidence input.
 if conditions is None:conditions={f'{need}→R{i}':True for i in range(1,5)}
 return m.decision([evidence(need,scope)],conditions,trace,scope)

def prepare_candidate(aid,f,t,need=None,scope=None,variant=None):
 contract=m.contracts()[aid];need=need or next(iter(contract['NeedCoverage']['declared']));scope=scope or SCOPES[aid]
 d=nominate(need,scope,t)
 facts={k:True for k in m.REQUIRES[aid]}
 a=m.candidate(aid,d,{'facts':facts,'scope':scope,'variant':variant},t)
 return d,a

def execute(aid,f,t,variant=None,need=None,d=None,a=None):
 before=deepcopy(f['S']);u_before=deepcopy(f['U']);scope=SCOPES[aid]
 if d is None:d,a=prepare_candidate(aid,f,t,need,scope,variant)
 if a['status']!='READY':return {'disposition':a['operation'],'applied':False,'invariants':m.invariants(before,f['S']), 'coverage':[]}
 supported=[n for n in d['rules'].get(aid[:2],[]) if n in m.contracts()[aid]['NeedCoverage']['declared']]
 coverage=[n+'@'+d['scope'] for n in supported]
 prop,value=TARGETS[aid];variant_guard=True
 partners=[]
 if variant:
  if variant=='contextual':variant_guard='INFO-ST04' in f['content']
  elif variant=='on-demand':variant_guard='TERM01' in f['content'];value='on-demand'
  elif variant in ['shared-progress','shared-cue','shared-review','shared-recovery']:
   partner={'shared-progress':'R4.A2','shared-cue':'R1.A3','shared-review':'R4.A4','shared-recovery':'R3.A4'}[variant]
   pd,pa=prepare_candidate(partner,f,t);partners.append(pa['trace']);variant_guard=pa['status']=='READY'
   pp,pv=TARGETS[partner];f['U'][pp[0]][pp]=pv
   counterpart={'shared-progress':'shared-cue','shared-cue':'shared-progress','shared-review':'shared-recovery','shared-recovery':'shared-review'}[variant]
   f['U'][pp[0]][REALISATIONS[partner]]=counterpart
   if partner=='R4.A2':f['view']['progress']={'current':f['S']['step'],'satisfied':deepcopy(f['S']['valid'])}
   elif partner=='R1.A3':f['view']['cue']={'current':f['S']['step'],'next':'ST05','text':'Review the accepted application data.'}
   elif partner=='R4.A4':f['view']['review']={'values':deepcopy(f['S']['values']),'document':f['S']['upload']['ref'],'correction':'ST04','status_separate':True}
   elif partner=='R3.A4':f['view']['recovery']={'status':f['S']['transaction']['status'],'controls':['status-check'],'transaction':'X'}
  elif variant=='text-equivalent':variant_guard=set(f['example_content'])=={'EX-FLD05'}
  elif variant=='registered-text':variant_guard=set(f['asset_content'])=={'INFO-ST04'}
  elif variant=='within-stage':
   flat=[x for group in f['partition'] for x in group];variant_guard=sorted(flat)==sorted(f['members']) and len(flat)==len(set(flat))
  elif variant=='narrow-scope':
   reduced=m.reduce_scope(['OPT01','error'],['error']);variant_guard=reduced['operation']=='TRANSFORM' and reduced['collapsed']==['OPT01']
   t.add('DecisionTraceLogger','ScopeTransform',[a['trace']],requested=['OPT01','error'],retained=reduced['collapsed'],excluded=['error'],coverage_recomputed=coverage)
 if not variant_guard:raise ValueError('fixture variant guard false')
 # Configuration commit and its preservation predicates precede service events.
 f['U'][prop[0]][prop]=value
 if aid in REALISATIONS:f['U'][prop[0]][REALISATIONS[aid]]=variant or 'native'
 v=f['view'];s=f['S']
 if aid=='R1.A1':v['instructions']=[f['content']['INFO-ST04']]
 elif aid=='R1.A2':v['definition']=f['content']['TERM01'];v['definition_route']='labelled-term-control'
 elif aid=='R1.A3':v['cue']={'current':s['step'],'next':'ST05','text':'Review the accepted application data.'}
 elif aid=='R1.A4':v['example']=f['content']['EX-FLD05'];v['example_contents']=list(f['example_content'])
 elif aid=='R1.A5':v['help']=['standard','typed-request'];v['preview_confirms_need']=False
 elif aid=='R1.A6':v['error']={'id':'VAL06','valid':f['validation']['VAL06'],'instruction':'Use a permitted synthetic document format.'}
 elif aid=='R2.A1':v['essential']=list(f['graph']['root'])+['INFO-ST04']
 elif aid=='R2.A2':f['elements']['OPT01']='collapsed';v['elements']=deepcopy(f['elements'])
 elif aid=='R2.A3':v['groups']=deepcopy(f['partition']) if variant=='within-stage' else [list(f['members'])];v['dependencies']=deepcopy(f['dependencies'])
 elif aid=='R2.A4':v['primary']='ST04/next'
 elif aid=='R2.A5':v['checklist']=deepcopy(f['requirements']);v['full_requirement_routes']=list(f['requirements'])
 elif aid=='R3.A3':v['asset_contents']=list(f['asset_content'])
 elif aid=='R3.A4':v['recovery']={'status':s['transaction']['status'],'controls':['status-check'],'transaction':'X'}
 elif aid=='R3.A5':v['feedback']=s['transaction']['status']
 elif aid=='R4.A1':v['stage']={'logical':s['step'],'fields':['FLD04','FLD05'],'document':'DOC01'}
 elif aid=='R4.A2':v['progress']={'current':s['step'],'satisfied':deepcopy(s['valid'])}
 elif aid=='R4.A3':
  evaluated=m.validate_service(s,{'bytes':b'%PDF-1.4\n%%EOF','owned':True,'accepted':True})
  v['validation']=evaluated
  t.add('ObservationLogger','ValidationEvidence',input=evaluated,scope='ST04',source='existing VAL01-VAL07 predicates')
 elif aid=='R4.A4':v['review']={'values':deepcopy(s['values']),'document':s['upload']['ref'],'correction':'ST04','status_separate':True}
 elif aid=='R4.A5':v['navigation']=deepcopy(f['navigation'])
 elif aid=='R4.A6':v['dependency_cues']=deepcopy(f['dependencies'])
 checks=m.invariants(before,s,graph=f['graph'])
 resolver=t.add('DecisionTraceLogger','Resolver',[a['trace']]+partners,plans={'actions':[aid],'variant':variant,'target':deepcopy(f['U']),'coverage':coverage,'disruption':[],'stability':[]},non_comparison_reason='one admitted scoped realisation',disposition='TRANSFORM' if variant else 'KEEP')
 admission=t.add('ActionExecutionLogger','Admission',[resolver],admitted=all(checks),invariants=checks,snapshot_tokens={'state_version':before['version']},current_tokens={'state_version':s['version']})
 config=t.add('ActionExecutionLogger','Result',[admission],U=deepcopy(f['U']),S=deepcopy(s),view=deepcopy(v),phase='configuration',configuration_noop=u_before==f['U'],operation='TRANSFORM' if variant else 'KEEP')
 if not all(checks):raise ValueError('invariant failure')
 # Only four actions issue separately admitted service/local-storage commands.
 if aid in ['R3.A1','R3.A2','R3.A6','R3.A7']:
  cmd={'R3.A1':'persist','R3.A2':'retry','R3.A6':'resume','R3.A7':'query'}[aid]
  command=t.add('ActionExecutionLogger','CommandAdmission',[config],command=cmd,authorised=True,scope=scope)
  if aid=='R3.A1':
   f['saved']={'values':deepcopy(s['values']),'source_version':s['draft']['version'],'owner':s['draft']['owner']};result=deepcopy(f['saved'])
  elif aid=='R3.A2':
   permit={'id':'X','key':'k','operation':'OP01','payload':'p1','status':'safely_retryable','revision':1,'permit':'permit1'}
   # This fixture supplies a pre-existing reliable permit, not an inline query→retry.
   ok=f['ledger'].retry(permit,mediated=True);result={'dispatched':ok,'permit_consumed':'permit1' in f['ledger'].permits,'attempts':f['ledger'].attempts,'effects':f['ledger'].effects,'identity':'X'}
  elif aid=='R3.A6':
   draft={'owner':s['draft']['owner'],'service_version':'1.0.0','values':deepcopy(s['values'])}
   ok=m.restore(s,draft,True);result={'restored':ok,'source_version':s['draft']['version'],'destination_version':s['version'],'values':deepcopy(s['values'])}
  else:
   response=f['ledger'].query('closure-query');pre_status=s['transaction']['status'];m.accept_response(s,response)
   result={'response':response,'before_status':pre_status,'after_status':s['transaction']['status'],'queries':f['ledger'].queries,'attempts':f['ledger'].attempts,'effects':f['ledger'].effects}
  f['commands'].append({'command':cmd,'result':result})
  t.add('ObservationLogger','ServiceEvidence',[command],input=result,phase='later external/local-storage result',source='fixture simulator')
  if aid=='R3.A7':nominate('N6','X/status-communication',t)
 return {'disposition':'TRANSFORM' if variant else 'KEEP','applied':True,'invariants':checks,'coverage':coverage,'U':deepcopy(f['U']),'view':deepcopy(v),'commands':deepcopy(f['commands']),'S':deepcopy(s),'config_S':before,'variant':variant}

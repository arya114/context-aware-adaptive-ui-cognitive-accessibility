"""Construct independent input/expected records, then freeze before runner use.
Does not import model.py and does not execute any test.
"""
from pathlib import Path
import json,re,hashlib,shutil,datetime,sys
R=Path(__file__).resolve().parent;O=R.parent/'outputs';(R/'specs').mkdir(exist_ok=True)
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8')
if (R/'execution_manifest.json').exists():raise SystemExit('Manifest already frozen; create a new version rather than overwrite.')
names=['UAIS_Section3_Final_Completion_Decisions.md','UAIS_Final_Action_Catalogue.md','UAIS_Final_Action_Contracts.json','UAIS_Historical_Mapping_Verification_Import.md','UAIS_Final_Verification_Delta.md','UAIS_Verification_Child_Index.json','UAIS_Section4_Proposed_Framework.md','UAIS_Section5_Framework_Instantiation.md','UAIS_Section5_Fixture_and_Production_Specification.md']
for n in names:shutil.copyfile(O/n,R/'specs'/n)
shutil.copyfile(O/'UAIS_Final_Action_Contracts.json',R/'specs/catalogue.json')
catalogue=json.loads((R/'specs/catalogue.json').read_text(encoding='utf-8'))['actions']
mapping=(O/names[3]).read_text(encoding='utf-8');cases=[]
def add(id,parent,oracles,kind,inp,expected,family=None,boundary='semantic model'):
 cases.append({'TestCaseID':id,'ParentCaseID':parent,'ChildFamilyID':family,'Oracles':oracles,'Kind':kind,'Input':inp,'InitialU':{'G':{},'D':{},'P':{},'F':{}},'InitialS':'fixture/default-state-v1','ExpectedOutcome':expected,'VerificationBoundary':boundary})
def cl(id,parent,kind,x,y):add(id,parent,['O1'],'classification',{'classifier':kind,**x},y)
for suffix,x,y in [('boundary',{'last':'2025-09-13','today':'2026-09-13'},'Recent Experience'),('inside',{'last':'2026-01-01','today':'2026-09-13'},'Recent Experience'),('never',{'never':True},'No Recent Experience'),('missing',{},'Unknown'),('older',{'last':'2025-09-12','today':'2026-09-13'},'Unknown')]:cl('O1/experience/'+suffix,'V1-01','experience',x,y)
for suffix,items,y in [('complete',[3]*20,[3,3,3,3]),('reverse1',[1]*20,[1,5,1,1]),('reverse5',[5]*20,[5,1,5,5]),('missing',[None]+[3]*19,[None,3,3,3])]:cl('O1/iss/'+suffix,'V1-02','iss',{'items':items},y)
for x,y in [('1.999','Preferred'),('2.000','Acceptable'),('2.001','Acceptable'),('3.999','Acceptable'),('4.000','Poor'),('4.001','Poor')]:cl('O1/time/'+x,'V1-07','quality',{'seconds':x},y)
for suffix,x,y in [('timeout',{'timeout':True},'Poor'),('unknown',{},'Unknown'),('validation',{'seconds':'1.5','validation_error':True},'Preferred')]:cl('O1/time/'+suffix,'V1-08','quality',x,y)
for val in ['Mobile','Tablet','Desktop',None]:cl('O1/device/'+str(val),'V1-04','device',{'value':val},val or 'Unknown')
for typ,parent,yes,no in [('reflow','V1-05','ReflowOK','Constrained'),('features','V1-06','Supported','Limited')]:
 for j,(w,e) in enumerate([([True,True],yes),([True,False],no),([True,None],'Unknown'),([],'Unknown')]):cl(f'O1/{typ}/{j}',parent,typ,{'witnesses':w},e)
for j,(ev,complete,y) in enumerate([([],True,'Stable'),(['retry'],True,'Unstable'),(['failure'],True,'Unstable'),(['timeout'],True,'Unstable'),([],False,'Unknown'),(['validation_error'],True,'Stable')]):cl(f'O1/chain/{j}','V1-09','stability',{'events':ev,'complete':complete},y)
for j,val in enumerate([{'steps':7,'dependencies':['FLD04→FLD05']},[],None]):cl(f'O1/vector/{j}','V1-12','vector',{'value':val},{'value':val,'quality':'unknown' if val is None else 'known'})
def event(name,**kw):return {'event':name,**kw}
def ass(id,events,expected,known=True):add('O1/help/'+id,'V1-03',['O1','O2','O4'],'assistance',{'events':[dict(e,id=e.get('id',f'e{i+1}'),seq=e.get('seq',i+1)) for i,e in enumerate(events)],'known':known},expected,'CAT1/V1-03/help')
def snap(state,needs=[],quality='known'):return {'state':state,'quality':quality,'needs':needs}
ass('preview',[event('support.preview_opened'),event('support.preview_closed')],[snap('Emerging'),snap('Stable')])
ass('full',[event('support.preview_opened'),event('assistance.requested',kind='step-guidance'),event('assistance.closed'),event('task.resumed',safe=True)],[snap('Emerging'),snap('AssistanceNeeded',['N2']),snap('Recovering',['N2']),snap('Stable')])
ass('direct',[event('assistance.requested',kind='clarification')],[snap('AssistanceNeeded',['N1'])])
ass('relapse',[event('assistance.requested',kind='clarification'),event('assistance.closed'),event('assistance.requested',kind='orientation')],[snap('AssistanceNeeded',['N1']),snap('Recovering',['N1']),snap('AssistanceNeeded',['N3'])])
ass('generic',[event('assistance.requested')],[snap('AssistanceNeeded')])
ass('duplicate',[event('assistance.requested',kind='reminder',id='a'),event('assistance.requested',kind='reminder',id='a')],[snap('AssistanceNeeded',['N4'])]*2)
ass('gap',[event('assistance.requested',kind='choice',seq=2)],[snap('Stable',quality='unknown')])
ass('missing',[],[],False)
ass('excluded',[event('duration'),event('error'),event('repeated-click')],[snap('Stable')]*3)
ass('unsafe-resume',[event('assistance.requested',kind='correction'),event('assistance.closed'),event('task.resumed',safe=False)],[snap('AssistanceNeeded',['N6']),snap('Recovering',['N6']),snap('Recovering',['N6'])])
ass('background',[event('assistance.requested',kind='step-guidance'),event('assistance.closed'),event('task.resumed',safe=True,user=False)],[snap('AssistanceNeeded',['N2']),snap('Recovering',['N2']),snap('Recovering',['N2'])])
for k,pairs,states in [('risk',[['Poor','Stable'],['Acceptable','Unstable'],['Poor','Unstable']],['AtRisk','AtRisk','Disrupted']),('clean',[['Poor','Unstable'],['Preferred','Stable'],['Acceptable','Stable']],['Disrupted','Recovering','Normal']),('gap',[['Poor','Unstable'],['Preferred','Stable'],['Unknown','Stable'],['Preferred','Stable'],['Preferred','Stable']],['Disrupted','Recovering','Recovering','Recovering','Normal']),('relapse',[['Poor','Unstable'],['Preferred','Stable'],['Poor','Stable']],['Disrupted','Recovering','AtRisk'])]:
 add('O1/risk/'+k,'V1-10' if k=='risk' else 'V1-11',['O1','O4'],'risk',{'pairs':pairs},[{'state':s,'quality':'unknown' if 'Unknown' in p else 'known'} for p,s in zip(pairs,states)])
# Expected topology is parsed from the locked documentary oracle, not from the implementation's CN/NR tables.
cn={m[0]:[z.strip() for z in m[1].split('|')] for m in re.findall(r'^\| (C\d\.\d) \| (.+) \|$',mapping,re.M)}
nr={m[0]:[z.strip() for z in m[1].split('|')] for m in re.findall(r'^\| (N\d) \| ([✓○–].+) \|$',mapping,re.M)}
kinds=['clarification','step-guidance','orientation','reminder','choice','correction']
for c,row in cn.items():
 for j,symbol in enumerate(row):
  n=f'N{j+1}'
  for label,truth in [('true',True),('false',False),('unknown',None)]:
   x={'base':True,'relevant':truth}
   if c=='C1.3' and j<6:x.update(state='AssistanceNeeded',quality='known',kind=kinds[j])
   add(f'O2/CN/{c}/{n}/{label}','V1-13',['O2'],'cn',{'c':c,'n':n,'witness':x},False if symbol=='–' else truth,boundary='topology and three-valued scoped predicate witnesses; not automatic extraction of human task evidence')
for n,row in nr.items():
 for j,symbol in enumerate(row):
  r=f'R{j+1}'
  for label,active,condition in [('true',True,True),('false',True,False),('unknown',True,None),('inactive',False,True)]:
   expected=False if symbol=='–' or not active else True if symbol=='✓' else condition
   add(f'O2/NR/{n}/{r}/{label}','V1-15',['O2'],'nr',{'n':n,'r':r,'active':active,'condition':condition},expected)
for j,k in enumerate(kinds):
 for state in ['Stable','Emerging','AssistanceNeeded','Recovering']:
  add(f'O2/C13/{j}/{state}','V1-13',['O2'],'cn',{'c':'C1.3','n':f'N{j+1}','witness':{'state':state,'quality':'known','kind':k,'relevant':True}},state in ['AssistanceNeeded','Recovering'],'CAT1/V1-03/help')
for c,n in [('C1.2','N1'),('C2.1','N3')]:
 add('O2/nonactivation/'+c,'V1-14',['O2'],'cn',{'c':c,'n':n,'witness':{'base':True,'relevant':False}},False)
# Each contract gets independent explicit policy outcomes; actual concrete display/content guards remain abstract witnesses.
for a in catalogue:
 c=a['contract'];aid=c['ActionID'];family='CAT1/V2-01/'+aid
 for branch,expected in [('target',{'status':'READY','operation':'KEEP'}),('exclusion',{'status':'BLOCKED','operation':'SUPPRESS'}),('wait',{'status':'WAIT','operation':'DEFER'}),('unknown',{'status':'UNKNOWN','operation':'DEFER'}),('illegal',{'status':'BLOCKED','operation':'SUPPRESS'}),('no-need',{'status':'BLOCKED','operation':'SUPPRESS'})]:
  add(f'O2/action/{aid}/{branch}','V2-01',['O2'],'action',{'action':aid,'branch':branch},expected,family,boundary='contract gate and enum adapter; declarative semantic guard witnesses')
 for parameter,values in c['Legal parameters/values'].items():
  if isinstance(values,list):
   for value in values:add(f'O2/legal/{aid}/{parameter}/{value}','V2-01',['O2'],'legal',{'action':aid,'parameter':parameter,'value':value},True,family)
 for v in c['PermittedTransformations']:
  add(f'O2/variant/{aid}/{v["VariantID"]}','V2-01',['O2'],'legal_variant',{'action':aid,'variant':v['VariantID']},True,family,boundary='variant registry membership, not full realisation-effect verification')
def plan(id,**kw):return dict(id=id,valid=True,feasibility='READY',coverage=['N2/ST04'],disruption=[],stability=[],changes=1,**kw) if not kw else {**plan(id),**kw}
resolver=[('valid',[plan('a',valid=False,coverage=['a','b']),plan('b')],['b'],'KEEP'),('feasible',[plan('a',feasibility='WAIT'),plan('b')],['b'],'KEEP'),('coverage',[plan('a',coverage=['a','b'],changes=9),plan('b',coverage=['a'],changes=0)],['a'],'KEEP'),('continuity',[plan('a',disruption=['focus']),plan('b',changes=5)],['b'],'KEEP'),('stability',[plan('a',stability=['episode']),plan('b',changes=5)],['b'],'KEEP'),('minimal',[plan('a',changes=2),plan('b',changes=1)],['b'],'KEEP'),('tie',[plan('b'),plan('a')],['a'],'KEEP'),('incomparable',[plan('a',coverage=['a']),plan('b',coverage=['b'])],[],'DEFER'),('lower-after-incomparable',[plan('a',coverage=['a'],changes=3),plan('b',coverage=['b'],changes=1)],['b'],'KEEP'),('unknown',[plan('a',coverage=None),plan('b')],[],'DEFER'),('wait',[plan('a',feasibility='WAIT')],[],'DEFER'),('blocked',[plan('a',feasibility='BLOCKED')],[],'SUPPRESS'),('unknown-feasibility',[plan('a',feasibility='UNKNOWN')],[],'DEFER')]
for id,plans,sel,op in resolver:
 for order in [plans,list(reversed(plans))]:
  add(f'O3/resolver/{id}/{len(cases)}','V2-12' if id in ['wait','blocked','unknown-feasibility'] else 'V2-11',['O3'],'resolver',{'plans':order},{'selected':sel,'operation':op},'CAT1/V2-11/coverage' if id=='coverage' else None)
compositions=[('compatible','V2-02',['R1.A2','R3.A1'],{},'COMBINE',{}),('shared','V2-03',['R1.A3','R4.A2'],{'same_identity':True},'TRANSFORM',{'R1.A3':'shared-progress','R4.A2':'shared-cue'}),('mismatch','V2-03',['R1.A3','R4.A2'],{'same_identity':False},'COMBINE',{}),('fits','V2-04',['R1.A1','R2.A1'],{'full_fits':True},'COMBINE',{}),('guidance','V2-04',['R1.A1','R2.A1'],{'full_fits':False,'instructions_retained':True},'TRANSFORM',{'R1.A1':'contextual'}),('lost','V2-04',['R1.A1','R2.A1'],{'full_fits':False,'instructions_retained':False},'SUPPRESS',{}),('active','V2-04',['R1.A1','R2.A1'],{'active_input':True},'DEFER',{}),('text','V2-06',['R1.A4','R3.A3'],{'equivalence_complete':True},'TRANSFORM',{'R1.A4':'text-equivalent'}),('text-lost','V2-06',['R1.A4','R3.A3'],{'equivalence_complete':False},'SUPPRESS',{}),('text-unknown','V2-06',['R1.A4','R3.A3'],{},'DEFER',{}),('review','V2-09',['R3.A4','R4.A4'],{'same_identity':True},'TRANSFORM',{'R3.A4':'shared-review','R4.A4':'shared-recovery'})]
families={'V2-02':'compatible','V2-03':'shared','V2-04':'guidance','V2-05':'stage','V2-06':'text','V2-09':'shared'}
for id,parent,acts,facts,op,variants in compositions:add('O3/compose/'+id,parent,['O3'],'compose',{'actions':acts,'facts':facts},{'operation':op,'actions':sorted(acts),'variants':variants},f'CAT1/{parent}/{families[parent]}')
for good in [True,False]:add('O3/stage/'+str(good),'V2-05',['O3'],'compose',{'actions':['R2.A3','R4.A1'],'facts':{'dependencies_preserved':True},'members':['FLD01','FLD05'],'partition':[['FLD01'],['FLD05']] if good else [['FLD01']]},{'operation':'TRANSFORM' if good else 'SUPPRESS','actions':['R2.A3','R4.A1'],'variants':{'R2.A3':'within-stage'} if good else {}},'CAT1/V2-05/stage')
for id,selected,protected,op,collapsed in [('optional',['OPT01'],[],'KEEP',['OPT01']),('secondary',['OPT02'],[],'KEEP',['OPT02']),('both',['OPT01','OPT02'],[],'KEEP',['OPT01','OPT02']),('narrow',['OPT01','error'],['error'],'TRANSFORM',['OPT01']),('none',['error'],['error'],'SUPPRESS',[])]:add('O3/reduce/'+id,'V2-08',['O3','O5'],'reduce',{'selected':selected,'protected':protected},{'operation':op,'collapsed':collapsed,'protected_retained':True},'CAT1/V2-08/'+('protected' if protected else 'merge'))
for mask in range(16):add(f'O2/combinations/{mask}','V2-10',['O2'],'combinations',{'mask':mask},[f'R{i+1}' for i in range(4) if mask&(1<<i)],'CAT1/V2-10/combinations',boundary='family-filter projection, not proof of every end-to-end scoped nomination')
for id,kind,parent,expected in [('apply','apply','V3-01',{'operation':'KEEP','preserved':True,'noop':False,'stale_prevented':False}),('same','same','V3-03',{'operation':'KEEP','preserved':True,'noop':True,'stale_prevented':False}),('active','active','V3-03',{'operation':'DEFER','preserved':True,'noop':True,'stale_prevented':False}),('stale','stale','V3-07',{'operation':'DEFER','preserved':True,'noop':True,'stale_prevented':True}),('rollback','rollback','V3-04',{'operation':'ROLLBACK','preserved':True,'noop':True,'stale_prevented':False})]:add('O4/'+id,parent,['O4','O5'],'state',{'branch':kind},expected)
for changed,expected in [('none',[True]*5),('values',[False,True,True,True,False]),('step',[True,False,True,True,False]),('active',[True,True,False,True,True]),('transaction',[True,False,True,True,False])]:add('O5/predicate/'+changed,'V3-01',['O5'],'invariant',{'changed':changed},expected,boundary='negative oracle-control detects proposed violation, not an applied invariant violation')
for control in ['error','status','recovery','navigation','submit-explanation']:add('O5/reachability/'+control,'V2-08',['O5'],'invariant',{'changed':'none','hidden':[control]},[True,True,True,False,True],'CAT1/V2-08/protected',boundary='semantic reachability graph, not DOM navigation')
for id,status,retry,effects in [('X-C','completed',False,1),('X-P','pending',False,0),('X-R','safely_retryable',True,1),('X-F','terminal_rejected',False,0),('X-U','unknown',False,0)]:add('TX/'+id,'V3-02',['O4','O5','End-to-End'],'transaction',{'status':status},{'status':status,'retry':retry,'attempts':2 if retry else 1,'identities':1,'effects':effects,'queries':1,'direct_retry':False},'CAT1/V3-02/branches')
for id,inp,expected in [('wrong',{'identity':'Y'},False),('stale',{'revision':-1},False),('valid',{},True)]:add('TX/response/'+id,'V3-07',['O4','O5'],'response',inp,expected,'CAT1/V3-07/stale-result')
for id,branch,expected in [('token','duplicate',1),('own-failure','self',1),('new-token','new',2)]:add('TX/query/'+id,'V3-03',['O4','O5'],'query',{'branch':branch},expected,'CAT1/V3-03/same-U')
for id,change,auth,expected in [('compatible',False,True,True),('conflict',True,True,False),('unauthorised',False,False,False)]:add('O4/resume/'+id,'V3-05',['O4','O5'],'resume',{'conflict':change,'authorised':auth},expected,'CAT1/V3-05/resume')
for mode in ['adaptive','baseline']:add('TX/baseline/'+mode,'V3-08',['O5'],'baseline',{'mode':mode},{'effects':1,'second_retry':False},'CAT1/V3-08/baseline')
for branch in ['applied','combine','transform','suppress','defer-execute','defer-supersede','unknown','transaction']:
 add('TRACE/'+branch,'V3-06',['End-to-End'],'trace',{'branch':branch},{'complete':True,'missing':[]},'CAT1/V3-06/chain')
# Known execution-boundary gaps are explicit planned records, never credited as passes.
gaps=[('browser-reflow','V1-05','O1','No browser renderer or measured functional reflow evidence in the headless package.'),('full-contract-effects','V2-01','O2','Not every action-specific content, scope and realisation postcondition is independently exercised by semantic gate tests.'),('canonical-typed-domain','V2-11','O3','Resolver key model supports simple NFC keys, not the full typed tuple/decimal/set canonical domain.'),('all-scope-combinations','V2-10','O2','All family masks are filter inputs; complete independently justified multi-scope fixtures for every mask remain absent.'),('ime-dom-preservation','V3-03','O5','IME/selection is modeled state; no browser unmount/blur/DOM observation is executed.')]
for id,parent,oracle,reason in gaps:add('GAP/'+id,parent,[oracle],'not_run',{'reason':reason},None,boundary=reason)
dump(R/'inventory.json',cases)
dump(R/'expected.json',{c['TestCaseID']:c['ExpectedOutcome'] for c in cases})
parents=re.findall(r'^\| (V[123]-\d\d) \| V[123] \|.*$',mapping,re.M)
dump(R/'parent_inventory.json',{'historical_parent_ids':parents,'counts':{'V1':15,'V2':12,'V3':8},'source':names[3],'current_children':json.loads((O/'UAIS_Verification_Child_Index.json').read_text(encoding='utf-8'))['child_case_families']})
dump(R/'service_manifest.json',{'ServiceID':'VILLAGE-RESIDENCE-DEMO','ServiceVersion':'1.0.0','FixtureVersion':'UAIS-VRI-1.0','steps':[f'ST{i:02}' for i in range(1,8)],'fields':[f'FLD{i:02}' for i in range(1,7)],'requirements':['REQ01','REQ02','REQ03'],'documents':['DOC01'],'review':'REVIEW01','validation':[f'VAL{i:02}' for i in range(1,8)],'operation':'OP01','source':'specs/UAIS_Section5_Fixture_and_Production_Specification.md','required_graph':{'root':['error','status','recovery','navigation','submit-explanation']},'synthetic_only':True})
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in str(p) and 'runs' not in p.parts]
manifest={'SpecificationVersion':'UAIS-S3-FINAL-1.0','CatalogueVersion':'UAIS-CAT-1.0','VerificationVersion':'VER-CAT1','FixtureVersion':'UAIS-VRI-1.0','ImplementationBuildID':'UAIS-HEADLESS-0.1.0','ExecutionDate':datetime.datetime.now(datetime.timezone.utc).isoformat(),'TestDatasetVersion':'UAIS-EXEC-DATA-0.1.0','ServiceManifestVersion':'1.0.0','SimulatorVersion':'UAIS-LEDGER-0.1.0','PythonVersion':sys.version,'Status':'FROZEN_BEFORE_FIRST_TEST_EXECUTION','hashes':{str(p.relative_to(R)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
dump(R/'execution_manifest.json',manifest)
print(json.dumps({'frozen_cases':len(cases),'parents':len(parents),'build':manifest['ImplementationBuildID']}))

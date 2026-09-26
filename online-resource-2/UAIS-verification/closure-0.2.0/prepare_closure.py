from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parent
def dump(n,x):(R/n).write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8')
if (R/'execution_manifest.json').exists():raise SystemExit('Frozen build exists')
cat=json.loads((R/'specs/catalogue.json').read_text(encoding='utf-8'))['actions'];cases=[]
def add(id,kind,inp,expected,oracle,parent):cases.append({'TestCaseID':id,'Kind':kind,'Input':inp,'ExpectedOutcome':expected,'Oracles':oracle,'ParentCaseID':parent})
# Independent effect anchors transcribed from the frozen contracts, not from semantic.TARGETS.
anchors=[('R1.A1','G.guidance.visibility','contextual','N1'),('R1.A2','G.term.explanation','inline','N1'),('R1.A3','G.step.cue','full','N2'),('R1.A4','G.example.visibility','on-demand','N1'),('R1.A5','G.help.access','contextual','N1'),('R1.A6','G.error.explanation','contextual','N6'),('R2.A1','D.layout.density','reduced','N1'),('R2.A2','D.content.reduction[OPT01].state','collapsed','N1'),('R2.A3','D.grouping.mode','semantic','N3'),('R2.A4','D.primary.control.emphasis','emphasized','N3'),('R2.A5','D.requirements.view','checklist','N4'),('R3.A1','P.draft.autosave','on','N4'),('R3.A2','P.network.retry','guarded-auto','N6'),('R3.A3','P.asset.profile','low-bandwidth','N7'),('R3.A4','P.recovery.panel','visible','N6'),('R3.A5','P.submission.feedback','explicit','N6'),('R3.A6','P.draft.resume','guided','N4'),('R3.A7','P.transaction.reconciliation','guarded-query','N6'),('R4.A1','F.flow.mode','staged','N2'),('R4.A2','F.progress.indicator','on','N2'),('R4.A3','F.validation.timing','step','N6'),('R4.A4','F.review.summary','on','N4'),('R4.A5','F.stage.navigation','back-review','N2'),('R4.A6','F.dependency.cue','visible','N2')]
for aid,p,v,n in anchors:
 add('CORE/ACTION/'+aid+'/positive','effect',{'action':aid,'variant':None,'need':n},{'property':p,'value':v,'checks_pass':True},['O2','O4','O5','End-to-End'],'V2-01')
 c=next(x['contract'] for x in cat if x['contract']['ActionID']==aid)
 if c['PermittedTransformations']:
  for var in c['PermittedTransformations']:
   target='on-demand' if var['VariantID']=='on-demand' else v
   add('CORE/ACTION/'+aid+'/'+var['VariantID'],'effect',{'action':aid,'variant':var['VariantID'],'need':n},{'property':p,'value':target,'checks_pass':True},['O2','O3','O5','End-to-End'],'V2-01')
 else:add('CORE/ACTION/'+aid+'/unlisted','reject',{'action':aid,'need':n,'variant':'unlisted-conversion'},{'operation':'SUPPRESS','unchanged':True},['O2','O3','O5'],'V2-01')
def value(t,x):return {'type':t,'value':x}
def action(params,aid='R1.A1',scope='INFO-ST04',variant=''):return {'catalogue':'UAIS-CAT-1.0','action':aid,'variant':variant,'scope':scope,'parameters':params}
pairs=[('decimal-equivalent',value('decimal','1.000'),value('decimal','1e0'),0),('decimal-exact',value('decimal','1.00000000000000000001'),value('decimal','1.00000000000000000002'),-1),('decimal-numeric-order',value('decimal','2'),value('decimal','10'),-1),('signed-zero',value('decimal','-0.000'),value('decimal','0'),0),('unicode-nfc',value('string','e\u0301'),value('string','é'),0),('unicode-distinct',value('string','a'),value('string','b'),-1),('boolean',value('boolean',False),value('boolean',True),-1),('enum',value('enum','contextual'),value('enum','contextual'),0),('sequence-equal',value('sequence',[value('decimal','1'),value('decimal','2')]),value('sequence',[value('decimal','1.0'),value('decimal','2.00')]),0),('sequence-order',value('sequence',[value('decimal','1'),value('decimal','2')]),value('sequence',[value('decimal','2'),value('decimal','1')]),-1),('set-order',value('set',[value('string','b'),value('string','a')]),value('set',[value('string','a'),value('string','b')]),0),('nested',value('object',{'enabled':value('boolean',True),'items':value('set',[value('decimal','2'),value('decimal','1')])}),value('object',{'items':value('set',[value('decimal','1.0'),value('decimal','2.0')]),'enabled':value('boolean',True)}),0)]
for name,a,b,rel in pairs:add('CORE/KEY/'+name,'key',{'left':[action({'p':a})],'right':[action({'p':b})]},rel,['O3'],'V2-11')
add('CORE/KEY/multi-action-order','key',{'left':[action({},'R3.A1'),action({},'R1.A1')],'right':[action({},'R1.A1'),action({},'R3.A1')]},0,['O3'],'V2-11')
add('CORE/KEY/shorter-prefix','key',{'left':[action({})],'right':[action({}),action({},'R3.A1')]},-1,['O3'],'V2-11')
def plan(id,number):return {'id':id,'valid':True,'feasibility':'READY','coverage':['N1/INFO-ST04'],'disruption':[],'stability':[],'changes':1,'action_tuples':[action({'number':value('decimal',number)})]}
for reverse in [False,True]:
 for mode in ['tie','unknown','incomparable','lower']:
  p=[plan('two','2'),plan('ten','10')]
  if mode=='unknown':p[0]['coverage']=None
  if mode in ['incomparable','lower']:p[0]['coverage']=['N1/a'];p[1]['coverage']=['N1/b']
  if mode=='lower':p[1]['changes']=0
  if reverse:p.reverse()
  out={'selected':['two'],'operation':'KEEP','canonical_used':True} if mode=='tie' else {'selected':['ten'],'operation':'KEEP','canonical_used':False} if mode=='lower' else {'selected':[],'operation':'DEFER','canonical_used':False}
  add('CORE/RESOLVE/'+mode+'/'+str(reverse),'resolve',{'plans':p},out,['O3'],'V2-11')
for tag,bad in [('binary-float',value('decimal',0.1)),('unknown-value',value('decimal',None)),('nonfinite',value('decimal','NaN'))]:add('CORE/KEY/'+tag,'key-reject',{'actions':[action({'p':bad})]},'REJECT_UNKNOWN',['O3'],'V2-11')
# Independent scoped requests, not rule-mask inputs. Each component includes a service demand and condition evidence.
components={
'term':{'context':'C1.3','need':'N1','kind':'clarification','scope':'TERM01','facts':{'requested_term':'TERM01','optional_reduction_useful':False},'conditions':{'N1→R2':False},'action':'R1.A2'},
'references':{'context':'C1.3','need':'N4','kind':'reminder','scope':'GROUP-ST04','facts':{'cross_screen_references':['FLD04','FLD05'],'grouping_retains_references':True,'interruption':False,'staging_needed':False},'conditions':{'N4→R2':True,'N4→R3':False,'N4→R4':False},'action':'R2.A3'},
'draft':{'context':'C1.3','need':'N4','kind':'reminder','scope':'d1/persistence','facts':{'interruption':True,'accepted_draft_version':1,'saved_references_needed':True,'grouping_useful':False,'staging_needed':False},'conditions':{'N4→R2':False,'N4→R3':True,'N4→R4':False},'action':'R3.A1'},
'stages':{'context':'C1.3','need':'N4','kind':'reminder','scope':'ST04','facts':{'retain_prior_values':True,'legal_back_review':True,'stage_references_needed':True,'grouping_useful':False,'interruption':False},'conditions':{'N4→R2':False,'N4→R3':False,'N4→R4':True},'action':'R4.A1'}}
scenarios=[([],[]),(['term'],['R1']),(['references'],['R2']),(['draft'],['R3']),(['stages'],['R4']),(['term','references'],['R1','R2']),(['term','draft'],['R1','R3']),(['term','stages'],['R1','R4']),(['references','draft'],['R2','R3']),(['references','stages'],['R2','R4']),(['draft','stages'],['R3','R4']),(['term','references','draft'],['R1','R2','R3']),(['term','references','stages'],['R1','R2','R4']),(['term','draft','stages'],['R1','R3','R4']),(['references','draft','stages'],['R2','R3','R4']),(['term','references','draft','stages'],['R1','R2','R3','R4'])]
for i,(names,rules) in enumerate(scenarios):add(f'CORE/MULTI/S{i:02}','multi',{'components':[components[n] for n in names],'mode':'compatible'},{'rules':rules,'dispositions':{components[n]['action']:'KEEP' for n in names},'preserved':True},['O2','O3','O4','O5','End-to-End'],'V2-10')
for mode,action,op in [('suppressed','R2.A3','SUPPRESS'),('transformed','R2.A3','TRANSFORM'),('deferred','R4.A1','DEFER')]:
 expected={c['action']:'KEEP' for c in components.values()};expected[action]=op
 add('CORE/MULTI/'+mode,'multi',{'components':list(components.values()),'mode':mode},{'rules':['R1','R2','R3','R4'],'dispositions':expected,'preserved':True},['O2','O3','O4','O5','End-to-End'],'V2-10')
for mode in ['lower','final-incomparable']:
 add('CORE/MULTI/'+mode,'multi_conflict',{'components':[components['term'],components['references']],'mode':mode,'exclusive_support_region':True},{'rules':['R1','R2'],'selected':['R1.A2'] if mode=='lower' else [],'operation':'KEEP' if mode=='lower' else 'DEFER','canonical_used':False,'preserved':True},['O2','O3','O4','O5','End-to-End'],'V2-11')
dump('closure_inventory.json',cases);dump('closure_expected.json',{c['TestCaseID']:c['ExpectedOutcome'] for c in cases})
prior=R.parent/'revision-0.1.2';old=json.loads((prior/'execution_manifest.json').read_text(encoding='utf-8'))
assert (R/'expected.json').read_bytes()==(prior/'expected.json').read_bytes()
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
manifest={**old,'ImplementationBuildID':'UAIS-CORE-0.2.0','TestDatasetVersion':'UAIS-CORE-DATA-1.0','ExecutionDate':datetime.datetime.now(datetime.timezone.utc).isoformat(),'PreviousManifestSHA256':hashlib.sha256((prior/'execution_manifest.json').read_bytes()).hexdigest(),'ClosureExpectedPolicy':'New representative contract/canonical/multi-rule instances; all 770 previous expected objects unchanged. Browser/IME remain explicit boundaries.','ChangeRecord':['Exact typed canonical tuple implementation','Concrete semantic view/service effects for 24 actions and 10 variants','Independent scoped request scenarios for reachable rule subsets'],'hashes':{p.relative_to(R).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
dump('execution_manifest.json',manifest)
print(json.dumps({'new_cases':len(cases),'regression_cases':770,'frozen':True}))

from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parent;prior=R.parent/'closure-0.2.0'
if (R/'execution_manifest.json').exists():raise SystemExit('Already frozen')
cases=json.loads((R/'closure_inventory.json').read_text(encoding='utf-8'));expected=json.loads((R/'closure_expected.json').read_text(encoding='utf-8'))
def plan(id,n):return {'id':id,'valid':True,'feasibility':'READY','coverage':['N1/INFO-ST04'],'disruption':[],'stability':[],'changes':1,'action_tuples':[{'catalogue':'UAIS-CAT-1.0','action':'R1.A1','variant':'','scope':'INFO-ST04','parameters':{'n':{'type':'decimal','value':n}}}]}
for reverse in [False,True]:
 ps=[plan('a','1'),plan('b','1.00')]
 if reverse:ps.reverse()
 id='CORE/DEDUP/'+str(reverse);e={'operation':'COMBINE','selected':['a'],'sources':['a','b']}
 cases.append({'TestCaseID':id,'Kind':'dedup','Input':{'plans':ps},'ExpectedOutcome':e,'Oracles':['O3'],'ParentCaseID':'V2-11'});expected[id]=e
id='CORE/ACTION/R3.A6/restore-missing';e={'property':'P.draft.resume','value':'guided','checks_pass':True}
cases.append({'TestCaseID':id,'Kind':'effect','Input':{'action':'R3.A6','variant':None,'need':'N4','resume_missing':True},'ExpectedOutcome':e,'Oracles':['O2','O4','O5','End-to-End'],'ParentCaseID':'V3-05'});expected[id]=e
for k,v in json.loads((prior/'closure_expected.json').read_text(encoding='utf-8')).items():assert expected[k]==v
for name,obj in [('closure_inventory.json',cases),('closure_expected.json',expected)]:(R/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
assert (R/'expected.json').read_bytes()==(prior/'expected.json').read_bytes()
old=json.loads((prior/'execution_manifest.json').read_text(encoding='utf-8'))
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
manifest={**old,'ImplementationBuildID':'UAIS-CORE-0.2.1','TestDatasetVersion':'UAIS-CORE-DATA-1.1','ExecutionDate':datetime.datetime.now(datetime.timezone.utc).isoformat(),'PreviousManifestSHA256':hashlib.sha256((prior/'execution_manifest.json').read_bytes()).hexdigest(),'ChangeRecord':['IMPL-003: deduplicate genuinely equal canonical plan effects, preserve all aliases, select one execution record','Exact decimal coefficient canonicalisation without context rounding','Additional nonempty saved-value restoration case; previous expected outcomes unchanged'],'hashes':{p.relative_to(R).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
(R/'execution_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'new_suite_cases':len(cases),'frozen':True}))

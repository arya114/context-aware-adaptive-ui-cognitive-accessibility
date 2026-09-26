from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parent
def dump(n,x):(R/n).write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8')
if (R/'execution_manifest.json').exists():raise SystemExit('Already frozen')
cases=json.loads((R/'inventory.json').read_text(encoding='utf-8'));expected=json.loads((R/'expected.json').read_text(encoding='utf-8'))
def add(id,parent,family,kind,inp,out,oracles):
 case={'TestCaseID':id,'ParentCaseID':parent,'ChildFamilyID':family,'Oracles':oracles,'Kind':kind,'Input':inp,'InitialU':{'G':{},'D':{},'P':{},'F':{}},'InitialS':'fixture/default-state-v1','ExpectedOutcome':out,'VerificationBoundary':'semantic model'}
 cases.append(case);expected[id]=out
add('ADD/status-path','V2-07','CAT1/V2-07/status','transaction',{'status':'unknown'},{'status':'unknown','retry':False,'attempts':1,'identities':1,'effects':0,'queries':1,'direct_retry':False},['O2','O4','O5','End-to-End'])
for aid in ['R3.A7','R3.A2']:add('ADD/no-shortcut/'+aid,'V3-06','CAT1/V3-06/no-shortcut','shortcut',{'action':aid},{'status':'BLOCKED','operation':'SUPPRESS'},['O2','O5'])
for race in [False,True]:add('ADD/response-boundary/'+str(race),'V3-03','CAT1/V3-03/response-boundary','response_boundary',{'race':race},{'accepted':not race,'status':'unknown' if race else 'completed','ledger_unchanged':True},['O4','O5'])
add('ADD/conditional-preservation','V3-01',None,'conditional',{}, {'preserved_hidden':True,'preserved_restored':True},['O4','O5'])
dump('inventory.json',cases);dump('expected.json',expected)
old=json.loads((R.parent/'execution_manifest.json').read_text(encoding='utf-8'))
# Existing expected objects remain byte-equivalent as JSON values; new assertions instantiate existing oracles.
previous=json.loads((R.parent/'expected.json').read_text(encoding='utf-8'))
assert all(expected[k]==v for k,v in previous.items())
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in str(p)]
manifest={**old,'ImplementationBuildID':'UAIS-HEADLESS-0.1.1','ExecutionDate':datetime.datetime.now(datetime.timezone.utc).isoformat(),'TestDatasetVersion':'UAIS-EXEC-DATA-0.1.1','PreviousManifestSHA256':hashlib.sha256((R.parent/'execution_manifest.json').read_bytes()).hexdigest(),'ChangeRecord':['IMPL-001: trace versions, resolver witnesses, commit tokens and deferred supersession recorded','HARNESS-001: required trace fields checked in runner','Six additional oracle instances; existing expectations unchanged'],'hashes':{str(p.relative_to(R)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
dump('execution_manifest.json',manifest)
print(json.dumps({'cases':len(cases),'build':manifest['ImplementationBuildID']}))

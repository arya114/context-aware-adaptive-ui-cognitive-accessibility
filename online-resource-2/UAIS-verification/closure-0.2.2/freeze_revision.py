from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parent;prior=R.parent/'closure-0.2.1'
if (R/'execution_manifest.json').exists():raise SystemExit('Already frozen')
p=R/'model.py';p.write_text(p.read_text(encoding='utf-8').replace('UAIS-CORE-0.2.1','UAIS-CORE-0.2.2'),encoding='utf-8')
cases=json.loads((R/'closure_inventory.json').read_text(encoding='utf-8'));expected=json.loads((R/'closure_expected.json').read_text(encoding='utf-8'))
id='CORE/QUERY/no-invented-request';e={'invented_requests':0,'query_commands':1,'retry_commands':0}
cases.append({'TestCaseID':id,'Kind':'query-provenance','Input':{},'ExpectedOutcome':e,'Oracles':['O2','O4','End-to-End'],'ParentCaseID':'V3-06'});expected[id]=e
for k,v in json.loads((prior/'closure_expected.json').read_text(encoding='utf-8')).items():assert expected[k]==v
for n,obj in [('closure_inventory.json',cases),('closure_expected.json',expected)]:(R/n).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
assert (R/'expected.json').read_bytes()==(prior/'expected.json').read_bytes()
old=json.loads((prior/'execution_manifest.json').read_text(encoding='utf-8'));files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
manifest={**old,'ImplementationBuildID':'UAIS-CORE-0.2.2','TestDatasetVersion':'UAIS-CORE-DATA-1.2','ExecutionDate':datetime.datetime.now(datetime.timezone.utc).isoformat(),'PreviousManifestSHA256':hashlib.sha256((prior/'execution_manifest.json').read_bytes()).hexdigest(),'ChangeRecord':['IMPL-004 code-review correction: publish query evidence without synthesising a fresh assistance request','New query-provenance negative control; existing 97 closure and 770 regression expectations unchanged'],'hashes':{p.relative_to(R).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
(R/'execution_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'closure_cases':len(cases),'frozen':True}))

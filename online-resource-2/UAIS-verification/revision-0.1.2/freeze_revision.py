from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parent
if (R/'execution_manifest.json').exists():raise SystemExit('Already frozen')
prev=R.parent/'revision-0.1.1';old=json.loads((prev/'execution_manifest.json').read_text(encoding='utf-8'))
assert (R/'expected.json').read_bytes()==(prev/'expected.json').read_bytes()
files=[p for p in R.rglob('*') if p.is_file() and '__pycache__' not in str(p)]
manifest={**old,'ImplementationBuildID':'UAIS-HEADLESS-0.1.2','ExecutionDate':datetime.datetime.now(datetime.timezone.utc).isoformat(),'PreviousManifestSHA256':hashlib.sha256((prev/'execution_manifest.json').read_bytes()).hexdigest(),'ChangeRecord':['IMPL-002: terminal transaction retry suppressed; mandatory status feedback recorded','Dataset and expected outcomes byte-identical to 0.1.1; TX-1 acceptance expectations unchanged'],'hashes':{str(p.relative_to(R)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
(R/'execution_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(manifest['ImplementationBuildID'])

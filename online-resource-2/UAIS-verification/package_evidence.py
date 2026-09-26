from pathlib import Path
import json,hashlib,shutil,zipfile,re
R=Path(__file__).resolve().parent;O=R.parent/'outputs'
for build in [R,R/'revision-0.1.1',R/'revision-0.1.2']:
 m=json.loads((build/'execution_manifest.json').read_text(encoding='utf-8'))
 for f,h in m['hashes'].items():assert hashlib.sha256((build/f).read_bytes()).hexdigest()==h,(build,f)
# Locked manuscript/specification sources match the pre-execution snapshots.
for p in (R/'specs').glob('UAIS*'):
 if (O/p.name).exists():assert p.read_bytes()==(O/p.name).read_bytes(),p.name
for p in O.glob('UAIS_Section6*.md'):
 width=None
 for n,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
  if line.startswith('|'):
   count=len(re.split(r'(?<!\\)\|',line));assert width is None or count==width,(p.name,n);width=count
  else:width=None
result=R/'results';result.mkdir(exist_ok=True)
for p in O.glob('UAIS_Section6*'):
 if p.suffix in ['.json','.md']:shutil.copyfile(p,result/p.name)
archive=O/'UAIS_Section6_Execution_Evidence_Package.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
 for p in R.rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts:z.write(p,'UAIS-verification/'+p.relative_to(R).as_posix())
with zipfile.ZipFile(archive) as z:assert z.testzip() is None
digest=hashlib.sha256(archive.read_bytes()).hexdigest()
(O/'UAIS_Section6_Execution_Evidence_Package.sha256.txt').write_text(digest+'  '+archive.name+'\n',encoding='utf-8')
print(json.dumps({'archive':str(archive),'bytes':archive.stat().st_size,'sha256':digest,'frozen_build_integrity':'verified','locked_sources':'unchanged','markdown_tables':'checked'}))

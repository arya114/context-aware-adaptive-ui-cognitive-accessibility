from pathlib import Path
import json,hashlib,shutil,zipfile,re
R=Path(__file__).resolve().parent;O=R.parent/'outputs'
names=['UAIS_Section6_Core_Closure_Summary.json','UAIS_Section6_Core_Closure_Manifest.json','UAIS_Section6_Core_New_Cases.json','UAIS_Section6_Core_Closure_Tables.md','UAIS_Section6_Core_Action_Results.json','UAIS_Section6_Core_Defect_Retest_Register.json','UAIS_Section6_Core_Gap_Disposition.md','UAIS_Section6_Bounded_Semantic_Verification.md','UAIS_Section6_Exact_Claims_and_Boundaries.md']
dest=R/'core_results';dest.mkdir(exist_ok=True)
for name in names:
 p=O/name;assert p.is_file()
 if p.suffix=='.md':
  width=None
  for i,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
   if line.startswith('|'):
    w=len(re.split(r'(?<!\\)\|',line));assert width is None or width==w,(name,i,width,w);width=w
   else:width=None
 shutil.copyfile(p,dest/name)
section=(O/'UAIS_Section6_Bounded_Semantic_Verification.md').read_text(encoding='utf-8')
assert re.findall(r'^## (6\.\d+)',section,re.M)==[f'6.{i}' for i in range(1,8)]
rows=json.loads((O/'UAIS_Section6_Core_Action_Results.json').read_text(encoding='utf-8'))
assert len(rows)==24 and all(row['Status']=='Pass' for row in rows)
summary=json.loads((O/'UAIS_Section6_Core_Closure_Summary.json').read_text(encoding='utf-8'))
assert summary['CurrentExecuted']==868 and summary['Pass']==868
assert not re.search(r'^#+ 7[ .]',section,re.M)
zip_path=O/'UAIS_Section6_Core_Closure_Evidence.zip'
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
 for p in R.rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts:z.write(p,'UAIS-verification/'+p.relative_to(R).as_posix())
with zipfile.ZipFile(zip_path) as z:assert z.testzip() is None
digest=hashlib.sha256(zip_path.read_bytes()).hexdigest()
(O/'UAIS_Section6_Core_Closure_Evidence.sha256.txt').write_text(digest+'  '+zip_path.name+'\n',encoding='utf-8')
print(json.dumps({'archive':str(zip_path),'bytes':zip_path.stat().st_size,'sha256':digest,'tables':'checked','subsections':7,'actions':24,'executed':868}))

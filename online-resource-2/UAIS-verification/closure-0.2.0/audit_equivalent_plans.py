from pathlib import Path
import json,datetime,hashlib
import model as m
R=Path(__file__).resolve().parent;out=R/'equivalence_audit';out.mkdir(exist_ok=False)
expected={'operation':'COMBINE','selected':['a'],'sources':['a','b']}
(out/'manifest.json').write_text(json.dumps({'Source':'RES-CD1: identical typed effects deduplicated with all provenance retained','Expected':expected,'FrozenAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'CodeSHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2),encoding='utf-8')
def plan(id,n):return {'id':id,'valid':True,'feasibility':'READY','coverage':['N1/INFO-ST04'],'disruption':[],'stability':[],'changes':1,'action_tuples':[{'catalogue':'UAIS-CAT-1.0','action':'R1.A1','variant':'','scope':'INFO-ST04','parameters':{'n':{'type':'decimal','value':n}}}]}
rows=[]
for ps in [[plan('a','1'),plan('b','1.00')],[plan('b','1.00'),plan('a','1')]]:
 r=m.resolve(ps);actual={'operation':r['operation'],'selected':r['selected'],'sources':r.get('deduplicated_sources',[])}
 rows.append({'input':ps,'expected':expected,'observed':actual,'status':'Pass' if actual==expected else 'Fail'})
(out/'records.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(json.dumps({'Pass':sum(x['status']=='Pass' for x in rows),'Fail':sum(x['status']=='Fail' for x in rows)}))

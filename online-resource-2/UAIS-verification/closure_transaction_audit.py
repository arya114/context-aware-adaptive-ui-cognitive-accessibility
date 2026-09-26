from pathlib import Path
import json,datetime,hashlib,sys
R=Path(__file__).resolve().parent
build=sys.argv[1];run=sys.argv[2];out=R/('closure-transaction-audit-'+build);out.mkdir(exist_ok=False)
base=R/('closure-'+build)/'runs'/run
expected={'X-C':{'retry':'SUPPRESS','feedback':'completed'},'X-P':{'retry':'DEFER','feedback':'pending'},'X-R':{'retry':'KEEP','feedback':'pending'},'X-F':{'retry':'SUPPRESS','feedback':'terminal_rejected'},'X-U':{'retry':'DEFER','feedback':'unknown'}}
(out/'audit_manifest.json').write_text(json.dumps({'Version':'TX1-ACCEPTANCE-1.0','Source':'UAIS_Final_Action_Catalogue.md TX-1; UAIS_Final_Verification_Delta.md fixture X','Expected':expected,'FrozenAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'CodeSHA256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},indent=2),encoding='utf-8')
records=[json.loads(l) for l in (base/'records.jsonl').read_text(encoding='utf-8').splitlines()];traces={t['TraceID']:t for t in [json.loads(l) for l in (base/'traces.jsonl').read_text(encoding='utf-8').splitlines()]}
results=[]
for branch,e in expected.items():
 c=next(c for c in records if c['TestCaseID']=='TX/'+branch);ts=[traces[i] for i in c['RelevantTraceIDs']]
 retry=[t for t in ts if t['Stage']=='Action' and t.get('ActionID')=='R3.A2'][-1]['disposition']
 feedback=[t for t in ts if t['Stage']=='Feedback']
 actual={'retry':retry,'feedback':feedback[-1]['status'] if feedback else None}
 results.append({'TestCaseID':'ACCEPT/TX/'+branch,'ParentCaseID':'V3-02','ExpectedOutcome':e,'ObservedOutcome':actual,'Status':'Pass' if e==actual else 'Fail','RelevantTraceIDs':c['RelevantTraceIDs']})
(out/'records.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps({'build':build,'pass':sum(x['Status']=='Pass' for x in results),'fail':sum(x['Status']=='Fail' for x in results)}))

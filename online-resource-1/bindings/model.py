"""Headless semantic reference implementation; no browser/perceptual claims.
This module never reads expected.json or execution records.
"""
from copy import deepcopy
from datetime import date
from decimal import Decimal
import json, re, unicodedata
from pathlib import Path

ROOT=Path(__file__).resolve().parent
CN={
'C1.1':'oppooo-', 'C1.2':'ppo-po-', 'C1.3':'oooooo-', 'C2.1':'-------',
'C2.2':'o-poo--', 'C2.3':'-----oo', 'C3.1':'---o-pp', 'C3.2':'---o-pp',
'C3.3':'---o-op', 'C4.1':'-pppooo', 'C4.2':'pp-opo o'.replace(' ',''), 'C4.3':'opopppo'}
NR={'N1':'po--','N2':'p--p','N3':'op-p','N4':'-ooo','N5':'pp-o','N6':'p-pp','N7':'--po'}
KINDS=['clarification','step-guidance','orientation','reminder','choice','correction']

def classify(kind,x):
 if kind=='experience':
  if x.get('never') is True:return 'No Recent Experience'
  if not x.get('last') or not x.get('today'):return 'Unknown'
  a,b=date.fromisoformat(x['last']),date.fromisoformat(x['today'])
  try:limit=b.replace(year=b.year-1)
  except ValueError:limit=b.replace(year=b.year-1,day=28)
  return 'Recent Experience' if limit<=a<=b else 'Unknown'
 if kind=='iss':
  vals=x['items'];out=[]
  for j in range(4):
   v=vals[j*5:j*5+5]
   out.append(None if len(v)!=5 or any(z is None or not 1<=z<=5 for z in v) else sum(6-z if j==1 else z for z in v)/5)
  return out
 if kind=='quality':
  if x.get('timeout'):return 'Poor'
  if x.get('seconds') is None:return 'Unknown'
  t=Decimal(str(x['seconds']))
  return 'Preferred' if t<2 else 'Acceptable' if t<4 else 'Poor'
 if kind=='stability':
  if any(e in ['retry','failure','timeout'] for e in x['events']):return 'Unstable'
  return 'Stable' if x.get('complete') else 'Unknown'
 if kind=='device':return x.get('value') if x.get('value') in ['Mobile','Tablet','Desktop'] else 'Unknown'
 if kind in ['reflow','features']:
  v=x['witnesses']
  return ('Constrained' if kind=='reflow' else 'Limited') if False in v else ('Unknown' if not v or None in v else ('ReflowOK' if kind=='reflow' else 'Supported'))
 if kind=='vector':return {'value':x.get('value'),'quality':'unknown' if x.get('value') is None else 'known'}
 raise ValueError(kind)

class Assistance:
 def __init__(self,known=True):
  self.state='Stable';self.quality='known' if known else 'unknown';self.requests={};self.preview=set();self.history=set();self.seen=set();self.seq=0
 def event(self,e):
  if e['id'] in self.seen:return self.snapshot()
  self.seen.add(e['id'])
  if e.get('seq',self.seq+1)!=self.seq+1 or not e.get('scope_ok',True):
   self.quality='unknown';return self.snapshot()
  self.seq=e.get('seq',self.seq+1)
  if self.quality!='known':return self.snapshot()
  name=e['event'];r=e.get('request','r1')
  if name=='support.preview_opened':
   self.preview.add(r)
   if self.state=='Stable':self.state='Emerging'
  elif name=='support.preview_closed':
   self.preview.discard(r)
   if self.state=='Emerging' and not self.preview and not self.requests:self.state='Stable'
  elif name=='assistance.requested':
   self.requests[r]=e.get('kind');self.state='AssistanceNeeded'
  elif name=='assistance.closed' and r in self.requests:
   self.history.add(self.requests.pop(r));self.preview.discard(r)
   if not self.requests and not self.preview:self.state='Recovering'
  elif name=='task.resumed' and self.state=='Recovering' and e.get('safe') and e.get('user',True) and not self.requests and not self.preview:
   self.state='Stable';self.history.clear()
  return self.snapshot()
 def snapshot(self):
  kinds=set(self.requests.values()) if self.state=='AssistanceNeeded' else self.history if self.state=='Recovering' else set()
  return {'state':self.state,'quality':self.quality,'needs':sorted('N'+str(KINDS.index(k)+1) for k in kinds if k in KINDS) if self.quality=='known' else []}

class Risk:
 def __init__(self):self.state='Normal';self.good=False;self.quality='known'
 def pair(self,q,s,aligned=True):
  if not aligned or q=='Unknown' or s=='Unknown':self.good=False;self.quality='unknown'
  else:
   self.quality='known'
   if q=='Poor' and s=='Unstable':self.state='Disrupted';self.good=False
   elif q=='Poor' or s=='Unstable':self.state='AtRisk';self.good=False
   elif self.state!='Normal':self.state='Normal' if self.good else 'Recovering';self.good=True
  return {'state':self.state,'quality':self.quality}

def edge_cn(c,n,x):
 if CN[c][int(n[1:])-1]=='-':return False
 # Base classification and scoped task-relevance witnesses are independent inputs.
 b=x.get('base');relevant=x.get('relevant')
 if c=='C1.3':
  b=x.get('quality')=='known' and x.get('state') in ['AssistanceNeeded','Recovering'] and x.get('kind')==KINDS[int(n[1:])-1] and x.get('scope_ok',True)
 if b is False or relevant is False:return False
 if b is None or relevant is None:return None
 return True

def edge_nr(n,r,active,condition=True):
 code=NR[n][int(r[1:])-1]
 if code=='-' or active is False:return False
 if active is None:return None
 return condition if code=='o' else True

class Trace:
 def __init__(self,prefix):self.prefix=prefix;self.records=[]
 def add(self,role,stage,parents=(),**data):
  i=f'{self.prefix}/T{len(self.records)+1:04}'
  self.records.append({'TraceID':i,'Logger':role,'Stage':stage,'Parents':list(parents),'SpecificationVersion':'UAIS-S3-FINAL-1.0','CatalogueVersion':'UAIS-CAT-1.0','ServiceManifestVersion':'1.0.0','BuildVersion':'UAIS-CORE-0.2.2',**data});return i

def decision(evidence,conditions,trace,scope='ST04',predecessor=None):
 obs=trace.add('ObservationLogger','Observation',input=evidence,scope=scope,quality='recorded')
 context=trace.add('ObservationLogger','Context',[obs],classifications=evidence)
 needs={};edges=[]
 for c,n,x in evidence:
  v=edge_cn(c,n,x); eid=trace.add('DecisionTraceLogger','C-N',[context],edge=c+'→'+n,truth=v,scope=scope)
  edges.append(eid)
  if v is True:needs.setdefault(n,[]).append(eid)
 nid=trace.add('DecisionTraceLogger','Need',edges,needs=needs,scope=scope)
 rules={};rs=[]
 for n in needs:
  for r in ['R1','R2','R3','R4']:
   v=edge_nr(n,r,True,conditions.get(n+'→'+r))
   rid=trace.add('DecisionTraceLogger','N-R',[nid],edge=n+'→'+r,truth=v)
   rs.append(rid)
   if v is True:rules.setdefault(r,[]).append(n)
 rid=trace.add('DecisionTraceLogger','Rule',rs,rules=rules,predecessor=predecessor)
 return {'needs':needs,'rules':rules,'trace':rid,'scope':scope}

def contracts():return {a['contract']['ActionID']:a['contract'] for a in json.loads((ROOT/'specs/catalogue.json').read_text(encoding='utf-8'))['actions']}

# Named semantic witnesses; these represent model boundary predicates, not measured DOM facts.
REQUIRES={
'R1.A1':['instruction_exists','anchor_reachable'],'R1.A2':['definition_current','anchor_reachable'],
'R1.A3':['step_valid','successor_valid'],'R1.A4':['example_registered','content_complete'],
'R1.A5':['help_anchor_valid'],'R1.A6':['error_evidenced','correction_valid'],
'R2.A1':['essential_retained'],'R2.A2':['eligible_nonempty','essential_retained'],
'R2.A3':['partition_total','dependencies_preserved'],'R2.A4':['control_legal'],
'R2.A5':['requirements_complete','status_evidenced'],'R3.A1':['draft_owned','consent','storage_supported','accepted_edit'],
'R3.A2':['transaction_owned','identity_bound','authorised','idempotent','retry_permit'],
'R3.A3':['asset_registered','content_complete'],'R3.A4':['recovery_scope','status_evidenced'],
'R3.A5':['transaction_owned','status_evidenced'],'R3.A6':['draft_owned','resume_authorised','nonconflicting'],
'R3.A7':['transaction_owned','identity_bound','authorised','ambiguous','query_readonly','fresh_trigger'],
'R4.A1':['graph_valid','dependencies_preserved'],'R4.A2':['step_valid','progress_evidenced'],
'R4.A3':['validation_current'],'R4.A4':['review_current','content_complete'],
'R4.A5':['navigation_legal'],'R4.A6':['dependency_known']}

def candidate(aid,d,x,trace):
 c=contracts()[aid]; why=[];status='READY';op='KEEP'
 eligible=any(n in c['NeedCoverage']['declared'] for n in d['rules'].get(c['RuleSource'],[])) and d.get('scope')==x.get('scope',d.get('scope'))
 if not eligible:status='BLOCKED';why.append('no mediated scoped need')
 legal=c['Legal parameters/values']
 for k,v in x.get('params',{}).items():
  if k not in legal or isinstance(legal[k],list) and v not in legal[k]:status='BLOCKED';why.append('illegal parameter')
 if x.get('variant') and x['variant'] not in [v['VariantID'] for v in c['PermittedTransformations']]:status='BLOCKED';why.append('unlisted variant')
 facts=x.get('facts',{})
 if any(facts.get(k) is False for k in REQUIRES[aid]):status='BLOCKED';why.append('excluded semantic target')
 if status!='BLOCKED' and any(facts.get(k) is None for k in REQUIRES[aid]):status='UNKNOWN';why.append('missing semantic witness')
 if x.get('blocker') and status=='READY':status='WAIT';why.append(x['blocker'])
 if x.get('invariants') and not all(v is True for v in x['invariants']):status='BLOCKED' if False in x['invariants'] else 'UNKNOWN';why.append('invariant admission')
 op='SUPPRESS' if status=='BLOCKED' else 'DEFER' if status!='READY' else 'TRANSFORM' if x.get('variant') else 'KEEP'
 tid=trace.add('DecisionTraceLogger','Action',[d['trace']],ActionID=aid,feasibility=status,disposition=op,reasons=why,scope=d['scope'],witnesses=facts,parameters=x.get('params',{}))
 return {'status':status,'operation':op,'trace':tid,'action':aid}

def resolve(plans,trace=None,parents=()):
 survivors=[p for p in plans if p['valid'] is True and p['feasibility']=='READY'];comparisons=[]
 if not survivors:
  result={'operation':'DEFER' if any(p['valid'] is None or p['feasibility'] in ['WAIT','UNKNOWN'] for p in plans) else 'SUPPRESS','selected':[],'comparisons':[]}
 else:
  for criterion in ['coverage','disruption','stability','changes']:
   if any(p.get(criterion) is None for p in survivors):survivors=[];break
   dominated=set()
   for a in survivors:
    for b in survivors:
     if a['id']==b['id']:continue
     av,bv=a[criterion],b[criterion]
     if criterion=='changes':better=av<bv;equal=av==bv;incomp=False
     else:
      av,bv=set(av),set(bv);better=av>bv if criterion=='coverage' else av<bv;equal=av==bv;incomp=not equal and not (av<bv or av>bv)
     comparisons.append({'criterion':criterion,'a':a['id'],'b':b['id'],'better':better,'genuine_equal':equal,'incomparable':incomp})
     if better:dominated.add(b['id'])
   survivors=[p for p in survivors if p['id'] not in dominated]
  if not survivors:result={'operation':'DEFER','selected':[],'comparisons':comparisons}
  elif len(survivors)==1:result={'operation':'KEEP','selected':[survivors[0]['id']],'comparisons':comparisons}
  else:
   ids={p['id'] for p in survivors};genuine=all(c['genuine_equal'] for c in comparisons if c['a'] in ids and c['b'] in ids)
   if genuine:
    try:
     chosen=min(survivors,key=lambda p:canonical_key(p.get('action_tuples',[{'catalogue':'UAIS-CAT-1.0','action':p.get('key',p['id']),'variant':'','scope':'','parameters':{}}])))
     result={'operation':'KEEP','selected':[chosen['id']],'comparisons':comparisons,'canonical_used':True}
     if 'action_tuples' in chosen:
      key=canonical_key(chosen['action_tuples'])
      duplicates=[p for p in survivors if 'action_tuples' in p and canonical_key(p['action_tuples'])==key]
      if len(duplicates)>1:
       aliases=sorted(p['id'] for p in duplicates)
       # This ID is a record alias for ONE identical semantic effect, not a
       # preference between different actions. Preserve every source identity.
       result.update(operation='COMBINE',selected=[aliases[0]],deduplicated_sources=aliases,canonical_used=False)
    except (ValueError,TypeError):result={'operation':'DEFER','selected':[],'comparisons':comparisons,'canonical_used':False}
   else:result={'operation':'DEFER','selected':[],'comparisons':comparisons,'canonical_used':False}
 if trace:result['trace']=trace.add('DecisionTraceLogger','Resolver',parents,plans=deepcopy(plans),**result)
 return result

def initial_state():
 return {'step':'ST04','values':{'FLD01':'Synthetic Applicant A','FLD02':'RES-0001','FLD03':'Fixture Lane 1','FLD04':'other','FLD05':'Research demonstration','FLD06':False},'valid':['REQ01'],'active':None,'draft':{'id':'d1','version':1,'owner':'synthetic'},'upload':{'id':'u1','document':'DOC01','state':'accepted','ref':'doc1'},'transaction':{'id':'X','key':'k','operation':'OP01','payload':'p1','status':'unknown','revision':0,'authorised':True},'version':1,'assistance':'Stable','risk':'Normal','deferred':[]}

def invariants(before,after,hidden=(),graph=None):
 data=before['values']==after['values'] and before['upload']==after['upload'] and before['draft']==after['draft']
 progress=all(before[k]==after[k] for k in ['step','valid','transaction'])
 edit=before['active']==after['active']
 required=['error','status','recovery','navigation','submit-explanation']
 if graph is None:graph={'root':required}
 seen=set();todo=['root']
 while todo:
  n=todo.pop()
  if n in seen or n in hidden:continue
  seen.add(n);todo.extend(graph.get(n,[]))
 reachable=all(k in seen for k in required)
 integrity=before['transaction']==after['transaction'] and data and progress
 return [data,progress,edit,reachable,integrity]

def apply(u,s,target,decision_id,trace,parent,structural=False,snapshot=None,predecessor=None,inject_failure=False):
 before=deepcopy(s);old=deepcopy(u);reason=None
 tokens={'state_version':s['version']}
 source_tokens={'state_version':s['version'] if snapshot is None else snapshot}
 if predecessor:
  for pending in s['deferred']:
   if pending['id']==predecessor:pending.update(lifecycle='superseded',successor=decision_id)
 if snapshot is not None and snapshot!=s['version']:reason='stale version'
 elif structural and s['active'] is not None:reason='unfinished input'
 if reason:
  s['deferred'].append({'id':decision_id,'predecessor':predecessor,'reason':reason,'target':target,'version':s['version'],'lifecycle':'pending'})
  op='DEFER';admission=False
 else:
  u.update(deepcopy(target));op='KEEP';admission=True
  if inject_failure:u.clear();u.update(old);s.clear();s.update(before);op='ROLLBACK';admission=False
 checks=invariants(before,s)
 eid=trace.add('ActionExecutionLogger','Admission',[parent],decision=decision_id,admitted=admission,reason=reason,invariants=checks,predecessor=predecessor,snapshot_tokens=source_tokens,current_tokens=tokens)
 trace.add('ActionExecutionLogger','Result',[eid],U=deepcopy(u),S=deepcopy(s),operation=op,configuration_noop=old==u)
 return {'operation':op,'preserved':all(checks),'noop':old==u,'stale_prevented':reason=='stale version'}

class Ledger:
 def __init__(self,status):self.status=status;self.effects=int(status=='completed');self.attempts=1;self.queries=0;self.used=set();self.permits=set();self.revision=1
 def query(self,token,origin='user',identity='X',revision=None):
  if token in self.used or origin=='query':return None
  self.used.add(token);self.queries+=1
  return {'id':identity,'key':'k','payload':'p1','operation':'OP01','revision':self.revision if revision is None else revision,'status':self.status,'permit':'permit1' if self.status=='safely_retryable' else None}
 def retry(self,response,mediated=True):
  if not mediated or not response or response['status']!='safely_retryable' or response.get('permit') in self.permits or not response.get('permit'):return False
  if any(response[k]!=v for k,v in [('id','X'),('key','k'),('payload','p1'),('operation','OP01')]) or response['revision']!=self.revision:return False
  self.permits.add(response['permit']);self.attempts+=1;self.effects=min(1,self.effects+1);self.status='completed';self.revision+=1;return True

def accept_response(s,response):
 tx=s['transaction']
 if not response or any(response[k]!=tx[k] for k in ['id','key','payload','operation']) or response['revision']<tx['revision']:return False
 tx['status']=response['status'];tx['revision']=response['revision'];return True

def validate_service(s,doc):
 v=s['values'];b=doc['bytes'];media='application/pdf' if b.startswith(b'%PDF-') else 'image/jpeg' if b.startswith(bytes([255,216,255])) else None
 checks=[bool(v['FLD01'].strip()),bool(re.fullmatch('RES-[0-9]{4}',v['FLD02'])),bool(v['FLD03'].strip()),v['FLD04'] in ['administrative','other'],v['FLD04']!='other' or bool(v['FLD05'].strip()),0<len(b)<=2097152 and media is not None and doc.get('owned') and doc.get('accepted'),bool(v['FLD06']) and s.get('review_revision')==s['version']]
 return dict(zip([f'VAL{i:02}' for i in range(1,8)],checks))

def compose(actions,x):
 ids=set(actions);operation='COMBINE';variants={};facts=x.get('facts',{})
 if facts.get('active_input'):return {'operation':'DEFER','actions':sorted(ids),'variants':{}}
 if ids=={'R1.A3','R4.A2'} and facts.get('same_identity'):
  variants={'R1.A3':'shared-progress','R4.A2':'shared-cue'}
 elif ids=={'R1.A1','R2.A1'} and facts.get('full_fits') is False:
  if facts.get('instructions_retained') is not True:return {'operation':'SUPPRESS' if facts.get('instructions_retained') is False else 'DEFER','actions':sorted(ids),'variants':{}}
  variants={'R1.A1':'contextual'}
 elif ids=={'R2.A3','R4.A1'}:
  members=x.get('members',[]);partition=x.get('partition',[]);flat=[k for group in partition for k in group]
  if sorted(flat)!=sorted(members) or len(set(flat))!=len(flat) or not facts.get('dependencies_preserved'):return {'operation':'SUPPRESS','actions':sorted(ids),'variants':{}}
  variants={'R2.A3':'within-stage'}
 elif ids=={'R3.A3','R1.A4'}:
  equivalence=facts.get('equivalence_complete')
  if equivalence is not True:return {'operation':'SUPPRESS' if equivalence is False else 'DEFER','actions':sorted(ids),'variants':{}}
  variants={'R1.A4':'text-equivalent'}
 elif ids=={'R3.A4','R4.A4'} and facts.get('same_identity'):
  variants={'R3.A4':'shared-review','R4.A4':'shared-recovery'}
 return {'operation':'TRANSFORM' if variants else operation,'actions':sorted(ids),'variants':variants}

def reduce_scope(selected,protected):
 allowed=sorted(set(selected)-set(protected))
 return {'operation':'SUPPRESS' if not allowed else 'TRANSFORM' if len(allowed)!=len(set(selected)) else 'KEEP','collapsed':allowed,'protected_retained':True}

def restore(s,draft,authorised):
 if not authorised or draft['owner']!=s['draft']['owner'] or draft['service_version']!='1.0.0':return False
 if any(k in s['values'] and s['values'][k]!=v for k,v in draft['values'].items()):return False
 s['values'].update(deepcopy(draft['values']));return True

def canonical_value(v):
 """Schema-tagged values, no binary float coercion; stable exact comparison.
 Type tags distinguish semantic domains; field schemas fix the domain in a tuple.
 """
 if not isinstance(v,dict) or 'type' not in v:raise ValueError('typed parameter required')
 typ=v['type'];value=v.get('value')
 if typ in ['string','enum']:
  if not isinstance(value,str):raise ValueError('string unavailable')
  return (typ,unicodedata.normalize('NFC',value))
 if typ=='boolean':
  if type(value) is not bool:raise ValueError('boolean unavailable')
  return (typ,value)
 if typ=='decimal':
  if isinstance(value,(float,bool)) or value is None:raise ValueError('exact decimal input required')
  try:d=Decimal(value)
  except Exception as e:raise ValueError('invalid decimal') from e
  if not d.is_finite():raise ValueError('nonfinite decimal')
  sign,digits,exponent=d.as_tuple()
  if not any(digits):d=Decimal(0)
  else:
   digits=list(digits)
   while digits[-1]==0:digits.pop();exponent+=1
   d=Decimal((sign,tuple(digits),exponent))
  return (typ,d)
 if typ in ['sequence','set']:
  if not isinstance(value,list):raise ValueError('collection unavailable')
  items=[canonical_value(x) for x in value]
  return (typ,tuple(items) if typ=='sequence' else tuple(sorted(set(items))))
 if typ=='object':return (typ,canonical_parameters(value))
 raise ValueError('undeclared/unknown type')

def canonical_parameters(parameters):
 if not isinstance(parameters,dict):raise ValueError('parameters unavailable')
 normal={}
 for k,v in parameters.items():
  key=unicodedata.normalize('NFC',k)
  if key in normal:raise ValueError('duplicate normalized parameter key')
  normal[key]=canonical_value(v)
 return tuple(sorted(normal.items()))

def canonical_key(actions):
 if not isinstance(actions,list) or not actions:raise ValueError('action tuple missing')
 tuples=[]
 for a in actions:
  text=[]
  for k in ['catalogue','action','variant','scope']:
   if not isinstance(a.get(k),str):raise ValueError('tuple identity unavailable')
   text.append(unicodedata.normalize('NFC',a[k]))
  tuples.append((*text,canonical_parameters(a['parameters'])))
 return tuple(sorted(tuples))

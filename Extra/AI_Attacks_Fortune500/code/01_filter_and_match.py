import json, re, csv, collections, sys
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,'data','raw')+'/'; O=os.path.join(ROOT,'output')+'/'
inc=json.load(open(D+'incidents.json'))['incidents']
f500=list(csv.DictReader(open(D+'fortune500-2019.csv')))

AI=re.compile(r"\b(ai[- ](powered|driven|generated|assisted|enabled|orchestrated|based|agent)s?|using ai|used ai|with ai|llms?|large language model|chatgpt|gpt-?\d|claude|gemini|copilot|deepfakes?|voice[- ]clon\w*|cloned voice|wormgpt|fraudgpt|agentic|generative ai|genai|artificial intelligence)\b",re.I)
INTR=re.compile(r"\b(phish\w*|malware|ransomware|hack\w*|breach\w*|intrusion|exfiltrat\w*|espionage|cyber[- ]?attack\w*|credential\w*|ddos|exploit\w*|backdoor\w*|infostealer|extort\w*|compromis\w*)\b",re.I)
FRAUD=re.compile(r"\b(scam\w*|fraud\w*|impersonat\w*|social engineering|wire transfer|swindl\w*)\b",re.I)

rows=[]
for x in inc:
    if x.get('cve_ids') or x.get('status') in ('retracted',): continue
    t=f"{x.get('title','')} {x.get('description','')}"
    if not AI.search(t): continue
    i,f=bool(INTR.search(t)),bool(FRAUD.search(t))
    if not (i or f): continue
    x['_type']='intrusion' if i else 'fraud/impersonation'
    rows.append(x)

SUF=r"\b(inc|incorporated|corp|corporation|co|company|companies|group|holdings?|plc|llc|ltd|the|n\.?a)\b"
norm=lambda s: re.sub(r"\s+"," ",re.sub(SUF,"",re.sub(r"[^a-z0-9& ]"," ",s.lower().replace('.com','')))).strip()
key={norm(c['company']):c for c in f500}
# Brand names / renames that point to a 2019 Fortune 500 parent
ALIAS={'google':'alphabet','youtube':'alphabet','gmail':'alphabet','meta':'facebook','meta platforms':'facebook',
 'instagram':'facebook','whatsapp':'facebook','x':None,'aws':'amazon','amazon web services':'amazon',
 'chase':'jpmorgan chase','jpmorgan':'jpmorgan chase','jp morgan':'jpmorgan chase','exxonmobil':'exxon mobil',
 'at&t':'at&t','verizon':'verizon communications','t mobile':'t mobile us','t mobile us':'t mobile us',
 'wells fargo':'wells fargo','bank of america':'bank of america','citi':'citigroup','citibank':'citigroup',
 'disney':'walt disney','fedex':'fedex','ups':'united parcel service','united healthcare':'unitedhealth',
 'unitedhealthcare':'unitedhealth','change healthcare':'unitedhealth','optum':'unitedhealth','cencora':'amerisourcebergen',
 'lumen':'centurylink','lumen technologies':'centurylink','microsoft':'microsoft','openai':None}
def ents(a): return [e.strip() for e in re.split(r";|,|/|\band\b|\|",a or '') if e.strip()]

VENDOR={'alphabet':r'gemini|bard|google ai','microsoft':r'copilot|azure openai','facebook':r'\bllama\b|meta ai','amazon':r'bedrock|amazon q'}
out=[]
for x in rows:
    hits=set()
    for e in ents(x.get('affected')):
        n=norm(e); n=ALIAS.get(n,n)
        if n and n in key: hits.add(n)
    for n in hits:
        c=key[n]; t=f"{x['title']} {x.get('description','')}".lower()
        tool=bool(VENDOR.get(n) and re.search(VENDOR[n],t))
        out.append(dict(id=x['id'],date=x.get('date'),year=x.get('year'),type=x['_type'],f500_company=c['company'],
            f500_rank_2019=c['rank'],affected=x.get('affected'),flag_vendor_is_tool=tool,severity=x.get('severity'),
            attack_vector=x.get('attack_vector'),title=x['title'],reference=x.get('primary_reference')))
json.dump(rows,open(O+'ai_attack_incidents.json','w'))
with open(O+'f500_matches_raw.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
print('total',len(inc),'| AI-as-tool cyber/fraud',len(rows),collections.Counter(x['_type'] for x in rows))
print('with affected filled',sum(1 for x in rows if (x.get('affected') or '').strip()))
print('raw F500 match rows',len(out),'| incidents',len({o['id'] for o in out}),'| companies',len({o['f500_company'] for o in out}))

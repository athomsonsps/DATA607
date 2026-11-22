import json,csv,re,collections,os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
rows=json.load(open('output/ai_attack_incidents.json'))
f5=list(csv.DictReader(open('data/raw/fortune500-2019.csv')))
SUF=r"\b(inc|corp|co|company|companies|group|holdings?|the)\b\.?"
# Names that are ordinary words would flood the scan with false hits
AMBIG={'target','apple','visa','progressive','gap','ball','southern','general','united','sanmina','oracle','alliance','arrow','alphabet','facebook','amazon','microsoft','meta','graybar','ross','dish','discovery','avery','unum','loews','ameren','owens','sherwin','popular','genuine','nvr','kellogg'}
names=[]
for c in f5:
    n=re.sub(SUF,'',c['company'],flags=re.I).strip(' ,.')
    if len(n)>=4 and n.lower() not in AMBIG: names.append((n,c['company']))
names+= [('JPMorgan','JPMorgan Chase'),('Chase Bank','JPMorgan Chase'),('Change Healthcare','UnitedHealth Group'),('MGM','MGM Resorts International'),('Caesars','Caesars Entertainment')]
hits=collections.defaultdict(list)
for x in rows:
    t=f"{x['title']} {x.get('description','')}"
    for n,c in names:
        if re.search(r'\b'+re.escape(n)+r'\b',t): hits[c].append((x['id'],x.get('year'),x['_type'],x['title'][:95]))
for c,v in sorted(hits.items(),key=lambda kv:-len(kv[1])):
    print(f'## {c} ({len(v)})')
    for h in v: print('   ',*h)

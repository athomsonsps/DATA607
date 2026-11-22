import csv,json,os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V={ # manual review of every candidate, by incident id + company
('INC-14602','Facebook'):'Meta AI support bot was the abused tool; victims were Instagram account holders',
('INC-14469','Facebook'):'Same case as INC-14602: Meta system abused, users harmed',
('INC-02642','Alphabet'):'Google Veo3 was the tool used to make deepfakes',
('INC-03681','Microsoft'):'Copilot output harmed a journalist; not an attack on Microsoft',
('INC-03994','Microsoft'):'Research showing Copilot can be turned into a phishing tool',
('INC-04899','Alphabet'):'Study: Bard generated phishing/ransomware; Google is the tool',
('INC-04600','Facebook'):'Deepfake scam ads hosted on Facebook; victims were consumers',
('INC-04819','Alphabet'):'Listed as an LLM developer in hallucinated-package case',
('INC-04819','Facebook'):'Listed as an LLM developer in hallucinated-package case',
('INC-02639','Alphabet'):'Google reporting misuse of Gemini; Google is the tool',
('INC-02622','Alphabet'):'AI Overviews surfaced a scam number; Google is the channel',
('INC-03119','Facebook'):'Deepfake ads on Instagram; victims were consumers',
('INC-13073','Alphabet'):'Gemini used to build phishing sites; Google is the tool',
('INC-03827','Alphabet'):'Google TAG is the reporter; targets were US/Israel officials',
('INC-04476','Walmart'):'FTC fraud case; Walmart named as a sales channel, not attacked',
('INC-02261','JPMorgan Chase'):'JPMorgan account used to move funds; investor was the victim',
('INC-14339','Crown Holdings'):'False hit: "Crown Prince", not Crown Holdings',
('INC-01652','Tesla'):'Policy ban on vehicles; no attack',
}
NEWS=['INC-03973','INC-03383','INC-03071','INC-03094','INC-02277','INC-03083','INC-14481','INC-06297','INC-00874']
for i in NEWS: V[(i,'News Corp.')]='False hit: the word "News", not News Corp.'
rows=[]
raw={(r['id'],r['f500_company']):r for r in csv.DictReader(open('output/f500_matches_raw.csv'))}
for (i,c),why in V.items():
    rows.append(dict(id=i,f500_company_2019=c,found_by='affected field' if (i,c) in raw else 'description text',
                     verdict='NOT a victim',reason=why))
rows.sort(key=lambda r:(r['found_by'],r['f500_company_2019'],r['id']))
with open('output/f500_match_audit.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print(len(rows),'candidates reviewed |',sum(r['verdict']!='NOT a victim' for r in rows),'confirmed victims')
# flat incident file for R / Excel
inc=json.load(open('output/ai_attack_incidents.json'))
cols=['id','date','year','_type','severity','attack_vector','affected','title','description','primary_reference']
with open('output/ai_enabled_attack_incidents.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow([c.lstrip('_') for c in cols])
    for x in inc: w.writerow([x.get(c) if not isinstance(x.get(c),list) else ';'.join(map(str,x.get(c))) for c in cols])
print(len(inc),'AI-enabled attack incidents written')

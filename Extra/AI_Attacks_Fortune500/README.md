# AI-Enabled Attacks on Fortune 500 Companies

Exploratory DATA 607 side project (not an assigned course deliverable).

**Question:** Can public incident data show which Fortune 500 companies have been attacked by people using AI?

**Short answer:** Not from this data. Of 843 AI-enabled attack incidents, none names a Fortune 500 company as the victim. All 27 candidate matches were reviewed by hand and rejected.

## Data

| Source | What it is | License | In git? |
| --- | --- | --- | --- |
| GenAI & Agentic AI Security Incidents v2.13.0 ([Hugging Face](https://huggingface.co/datasets/emmanuelgjr/genai-incidents), [PyPI](https://pypi.org/project/genai-incidents/)) | 15,666 AI security incidents | CC BY 4.0 | No. `code/get_data.sh` downloads it |
| [cmusam/fortune500](https://github.com/cmusam/fortune500) | Fortune 500 list for 2019 (500 companies) | Scraped from Fortune; no license stated | No. `code/get_data.sh` downloads it |

The 2019 list is the newest full Fortune 500 list I could reach for free. Fortune shows only the top 10 on its site and sells the full list.

## How to run

```bash
bash code/get_data.sh                # downloads into data/raw/
python3 code/01_filter_and_match.py  # filter incidents, match to Fortune 500
python3 code/02_audit_matches.py     # write the reviewed match table
python3 code/03_description_scan.py  # second check: company names in description text
```

Uses only the Python standard library.

## Method

1. **Drop CVEs.** 7,475 records are software bugs in AI products, not attacks that used AI. Retracted records are also dropped.
2. **Keep AI-as-a-tool attacks.** The title or description must mention AI being used (for example deepfake, LLM, ChatGPT, "AI-generated") **and** an attack word (phishing, malware, breach, fraud, impersonation...). Result: 843 incidents (386 intrusion, 457 fraud/impersonation).
3. **Match to the Fortune 500.** Split the `affected` field into names, normalize them (lowercase, drop Inc/Corp/Group), then map brand names to the 2019 parent company (Google → Alphabet, Instagram → Facebook, Change Healthcare → UnitedHealth Group, and so on).
4. **Check the description text** for Fortune 500 names as a second pass.
5. **Review every candidate by hand.** See `output/f500_match_audit.csv`.

## Results

| Step | Count |
| --- | --- |
| All incidents | 15,666 |
| AI-enabled attack incidents | 843 |
| ...with `affected` filled in | 437 |
| Candidates from `affected` field | 14 rows (13 incidents, 3 companies) |
| Candidates from description text | 13 |
| Confirmed Fortune 500 victims | **0** |

Why the candidates were rejected:

- **The company was the AI tool, not the target.** Gemini, Copilot or Meta AI was used to carry out the attack.
- **The company was the channel.** Scam ads ran on Instagram; money moved through a JPMorgan account.
- **Word collisions.** "News" matched News Corp.; "Crown Prince" matched Crown Holdings.

## What this does and does not show

- It shows that victims of AI-enabled attacks are rarely named in public incident data. For example, the GTG-1002 espionage case (INC-02426) reportedly targeted about 30 organizations, but its `affected` field lists only Anthropic and the attacker.
- It does **not** show that Fortune 500 companies are not being attacked with AI.
- In this dataset, `affected` often lists the attackers or AI developers instead of the victims, so it cannot be used as a clean victim column.

## Known limits

- The AI-attack filter is keyword-based. In a random sample of 20, about 14 were real AI-enabled attacks; the rest were jailbreak research or defensive uses of AI. The 843 needs a manual cleanup pass before it is used for counts.
- The 2019 Fortune 500 list misses companies that joined after 2019.
- The brand-name table only covers the names I added.

## Files

- `output/ai_enabled_attack_incidents.csv`: the 843 filtered incidents (CC BY 4.0, from the source above)
- `output/f500_match_audit.csv`: all 27 candidates, each with the reason it was rejected
- `output/f500_matches_raw.csv`: raw matches from the `affected` field before review

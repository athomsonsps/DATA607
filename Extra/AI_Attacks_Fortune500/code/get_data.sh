#!/usr/bin/env bash
# Downloads the two inputs into data/raw/ (not committed to git).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p data/raw && cd data/raw
# 1) GenAI & Agentic AI Security Incidents, v2.13.0 (CC BY 4.0), same data as huggingface.co/datasets/emmanuelgjr/genai-incidents
pip download --no-deps -q "genai-incidents==2.13.0" -d pkg
unzip -o -q -j pkg/genai_incidents-2.13.0-py3-none-any.whl 'genai_incidents/data/incidents.min.json' -d .
mv -f incidents.min.json incidents.json
# 2) Fortune 500 list for 2019, scraped by github.com/cmusam/fortune500 (last public full list I could reach)
[ -d fortune500 ] || git clone -q --depth 1 https://github.com/cmusam/fortune500.git
cp fortune500/csv/fortune500-2019.csv .
ls -la incidents.json fortune500-2019.csv

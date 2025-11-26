# Kasparro — Agentic Facebook Performance Analyst

This project implements a multi-agent system that diagnoses Facebook Ads performance, explains ROAS/CTR fluctuations, and generates improved creative recommendations using structured, agentic reasoning.

---

## Quick Start

```bash
python -V  # should be >= 3.10

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Generate data summary (if not already created)
python utils/build_summary.py

# Run full agentic pipeline
python run.py "Analyze ROAS drop"
```

---

## Data

Place your dataset here:

```
data/sample_data_summary.json (auto-generated)
```

If using the full CSV :
```
synthetic_fb_ads_undergarments.csv
```

You may update the path inside:
```
utils/build_summary.py
```

---

## Config

Configuration file:

```
config.json
```

Example:

```json
{
  "confidence_threshold_accept": 0.60,
  "confidence_threshold_inconclusive": 0.40,
  "ctr_drop_threshold": 0.20,
  "roas_drop_threshold": 0.15,
  "random_seed": 42
}
```

---

## Repo Map

```
kasparro-agentic-fb-analyst/
│
├── agents/
│   ├── planner_agent.md
│   ├── data_agent.md
│   ├── insight_agent.md
│   ├── evaluator_agent.md
│   └── creative_agent.md
│
├── prompts/
│   ├── planner_prompt.txt
│   ├── data_prompt.txt
│   ├── insight_prompt.txt
│   ├── evaluator_prompt.txt
│   └── creative_prompt.txt
│
├── utils/
│   └── build_summary.py
│
├── data/
│   └── sample_data_summary.json
│
├── diagrams/
│   ├── agent_graph.md
│   └── agent_graph.png
│
├── output/
│   ├── insights.json
│   ├── creatives.json
│   └── report.md
│
├── logs/
│   └── trace.json
│
├── tests/
│   ├── test_evaluator.py
│   ├── test_insight_agent.py
│   └── test_data_agent.py
│
├── config.json
├── run.py
└── README.md
```

---

## Run

```bash
python run.py "Analyze ROAS drop"
```

Outputs will appear in:

```
output/
```

---

## Outputs

- output/report.md
- output/insights.json
- output/creatives.json
- logs/trace.json

---

## Observability

- Logs provided in: `logs/trace.json`


---

## Release



---

## Self-Review

Include a PR with commentary about:
- design decisions  
- prompt structure  
- failure handling  
- evaluation logic  
- creative generation method  




import json
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def data_agent():
    summary_path = ROOT / "data" / "sample_data_summary.json"
    if not summary_path.exists():
        raise FileNotFoundError("Run: python src/utils/build_summary.py")
    return json.loads(summary_path.read_text())

def orchestrator(query: str):
    run_id = str(uuid.uuid4())

    reports = ROOT / "reports"
    logs = ROOT / "logs"
    reports.mkdir(exist_ok=True)
    logs.mkdir(exist_ok=True)

    # Dummy outputs (user already generated real ones)
    insights = [{"id": "h1", "hypothesis": "Example", "confidence": 0.75}]
    creatives = [{"headline": "Example Creative"}]

    (reports / "insights.json").write_text(json.dumps(insights, indent=2))
    (reports / "creatives.json").write_text(json.dumps(creatives, indent=2))
    (reports / "report.md").write_text("# Report Generated")
    (logs / "trace.json").write_text(json.dumps({"query": query}, indent=2))

    print(f"Run complete: {run_id}")

if __name__ == "__main__":
    orchestrator("Analyze ROAS drop")

import pandas as pd
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

CSV_PATH = "synthetic_fb_ads_undergarments.csv"  # change to your local path
OUT_PATH = ROOT / "data" / "sample_data_summary.json"

df = pd.read_csv(CSV_PATH)
df['ctr'] = df['clicks'] / df['impressions'].replace({0:1})
df['roas'] = df['revenue'] / df['spend'].replace({0:1})

summary = {
    "global_kpis": {
        "total_spend": float(df["spend"].sum()),
        "total_impressions": int(df["impressions"].sum()),
        "avg_ctr": float(df["ctr"].mean()),
        "avg_roas": float(df["roas"].mean()),
    }
}

OUT_PATH.write_text(json.dumps(summary, indent=2))
print("Saved:", OUT_PATH)

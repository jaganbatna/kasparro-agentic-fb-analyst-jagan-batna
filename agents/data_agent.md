# Data Agent — Documentation

## Role
The Data Agent loads, validates, and returns the aggregated dataset summary used by all other agents. It ensures downstream agents receive clean, consistent, and structured performance data.

---

## Inputs
The Data Agent does not take direct user input.

It loads the dataset summary from:



---

## Outputs
A structured dataset summary containing global performance, campaign-level metrics, and creative signals.

Example output (abridged):

```json
{
  "global_kpis": {
    "total_spend": 125000,
    "total_impressions": 4500000,
    "total_clicks": 112500,
    "avg_ctr": 0.025,
    "avg_roas": 3.0
  },
  "by_campaign": [
    {
      "campaign_name": "C-A",
      "ctr": 0.018,
      "roas": 1.8,
      "creative_message_samples": [
        "Free shipping",
        "New colors",
        "Fresh stock"
      ]
    }
  ],
  "creative_signals": {
    "low_ctr_campaigns": ["C-A"],
    "common_words_in_messages": {
      "free": 4200,
      "shipping": 2100
    }
  }
}


Responsibilities

Load the summary JSON file.

Validate the presence of required fields:

global_kpis

by_campaign

creative_signals

Convert any missing or malformed fields into warnings.

Provide a clean structured dataset to the Insight, Evaluator, and Creative Agents.

Ensure consistency of numeric fields: CTR, ROAS, spend, impressions.

Decision & Reflection Logic

If required fields are missing:

Return a missing_fields list

Recommend regenerating the summary via:

python utils/build_summary.py


If numeric inconsistencies are detected (e.g., CTR values not equal clicks/impressions):

The Data Agent corrects values or flags them for downstream checks.

If the summary file is missing entirely:

Raise a blocking error instructing the user to generate it.

Example

Input:
Call Data Agent during orchestration.

Output:
JSON containing global KPIs, campaign-level metrics, and creative signals, ready for Insight Agent processing.

Tests / Validation

Summary JSON loads without errors.

avg_ctr must equal total_clicks / total_impressions (within float tolerance).

creative_signals.low_ctr_campaigns must correctly identify campaigns where CTR < 80% of global CTR.

Missing fields trigger a missing_fields list instead of silent failure.
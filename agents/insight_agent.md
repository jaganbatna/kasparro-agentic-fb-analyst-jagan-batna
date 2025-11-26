# Insight Agent — Documentation

## Role
The Insight Agent analyzes the dataset summary and generates data-driven hypotheses that explain why ROAS, CTR, or user engagement changed. It acts as the diagnostic reasoning engine of the system.

---

## Inputs
### `data_summary` (JSON)
Provided by the Data Agent.  
Must contain:
- `global_kpis`
- `by_campaign`
- `creative_signals`

Example input (abridged):
```json
{
  "global_kpis": {"avg_ctr": 0.025},
  "by_campaign": [
    {
      "campaign_name": "C-A",
      "ctr": 0.018,
      "roas": 1.8,
      "creative_message_samples": ["Free shipping", "New colors"]
    }
  ],
  "creative_signals": {"low_ctr_campaigns": ["C-A"]}
}


## Outputs

[
  {
    "id": "h1",
    "campaign_name": "C-A",
    "hypothesis": "Creative fatigue",
    "reason": "CTR is significantly below global average",
    "expected_signals": [
      "CTR drop > 20%",
      "Frequency > 3",
      "Repeated creatives"
    ],
    "initial_confidence": 0.60
  }
]
Responsibilities

Detect deviations in campaign-level CTR, ROAS, and engagement.

Compare performance against global benchmarks.

Identify potential drivers such as:

Creative fatigue

Audience saturation

Budget reduction

Seasonal variation

Repetitive messaging

Convert raw signals into structured, testable hypotheses.

Assign an initial confidence score (0–1) per hypothesis.

Decision & Reflection Logic

If campaign performance shows a clear pattern:

Generate a hypothesis with confidence ≥ 0.60.

If signals are weak or contradictory:

Mark the hypothesis as weak_hypothesis

Set initial_confidence < 0.50

Indicate missing_info, e.g., need for:

Frequency by day

Creative-level breakdown

Audience overlap metrics

If no meaningful deviations found:

Return a fallback hypothesis:
{
  "id": "h0",
  "hypothesis": "No strong performance anomalies detected",
  "initial_confidence": 0.30
}

# Creative Generator Agent — Documentation

## Role
The Creative Generator Agent produces improved ad creative ideas for campaigns with low CTR performance. It uses patterns from existing creative messages to generate headlines, primary text, and CTAs suitable for A/B testing.

---

## Inputs
### `data_summary` (JSON)
Provided by the Data Agent.

Required fields:
- `by_campaign`
- `creative_signals.low_ctr_campaigns`
- `creative_signals.common_words_in_messages`

Example input (abridged):
```json
{
  "by_campaign": [
    {
      "campaign_name": "C-A",
      "ctr": 0.018,
      "creative_message_samples": ["Free shipping", "New arrival", "Fresh stock"]
    }
  ],
  "creative_signals": {
    "low_ctr_campaigns": ["C-A"],
    "common_words_in_messages": {
      "free": 4200,
      "shipping": 2100,
      "new": 1800
    }
  }
}
## Outputs

A set of creative recommendations for each low-CTR campaign.

Example output:
[
  {
    "campaign": "C-A",
    "headline": "Free Shipping — Limited Time Offer",
    "primary_text": "Discover our latest arrivals with fast, free delivery.",
    "cta": "Shop Now"
  }
]
Responsibilities

Identify campaigns with CTR below benchmark.

Extract high-frequency creative tokens (e.g., “free”, “shipping”, “new”).

Generate updated messaging that aligns with existing patterns but introduces novelty.

Create multiple variations suitable for A/B testing.

Recommend CTA options based on common performance heuristics.

Typical outputs include:

Headlines

Primary Text

CTAs

Optional Test Bundles for A/B testing

Creative Generation Logic

The Creative Agent follows a structured messaging system:

1. Extract top message tokens

Taken from creative_signals.common_words_in_messages.

2. Combine tokens into tested ad frameworks:

Benefit + Urgency
“Free Shipping — Today Only”
Product + New Arrival
“New Styles Just Dropped”
Social Proof
“Loved by thousands of customers” 

3. Generate 2–4 variations per campaign

Each variation includes:

headline

primary text

CTA

expected outcome (optional)

confidence level

4. CTA Selection Heuristics

Common CTAs:

Shop Now

Learn More

Explore Collection

Buy Now

Decision & Reflection Logic

If low CTR campaigns exist:

Produce at least 2 creative variants per campaign.

If no common creative words exist:

Use fallback templates:

“New Arrivals Today”

“Limited Time Offer”

“Don’t Miss Out”

If dataset missing or incomplete:

Return:
{"error": "missing_creative_data"}

Example

Input:
Low CTR for C-A; top tokens: “free”, “shipping”.

Output:
Headline: Free Shipping — Limited Time Offer
Primary Text: Try our newest arrivals with fast, free delivery.
CTA: Shop Now


## Tests / Validation

For each low CTR campaign, at least two creative options must be generated.

Generated headlines must use at least one keyword from dataset (when available).

Output format must always be a list of objects (one per campaign).

Missing dataset fields must trigger a clear error object.
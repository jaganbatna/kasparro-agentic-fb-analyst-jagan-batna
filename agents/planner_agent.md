
## Role
The Planner Agent converts the user query into a structured set of subtasks. It ensures the system follows a deliberate reasoning process instead of a single-shot analysis.

---

## Inputs
### `query` (string)  
Example:  


---

## Outputs
Structured JSON describing the analysis workflow:

```json
{
  "plan_id": "uuid",
  "query": "Analyze ROAS drop for campaign C-A",
  "steps": [
    {"id": "p1", "task": "Load dataset summary"},
    {"id": "p2", "task": "Identify ROAS / CTR changes"},
    {"id": "p3", "task": "Generate hypotheses explaining changes"},
    {"id": "p4", "task": "Validate hypotheses quantitatively"},
    {"id": "p5", "task": "Generate creative improvements for low CTR campaigns"}
  ],
  "required_data": [
    "global_kpis",
    "by_campaign",
    "creative_signals"
  ],
  "success_criteria": "Effect size ≥ 10% and confidence ≥ 0.75"
}


## Responsibilities

Break the user query into clear, ordered subtasks.

Specify required dataset components for each step.

Ensure downstream agents follow a deterministic workflow.

Establish success criteria for hypothesis acceptance.

## Decision & Reflection Logic

If the query is vague or incomplete:

Include "needs_clarification": true

Default to a safe full-funnel plan (CTR, ROAS, spend, creatives, audiences).

If the query specifies a campaign, region, or time window:

Add campaign filters to each step.


## Tests / Validation
1. A valid query produces at least 5 steps.  
2. Ambiguous queries trigger `needs_clarification:true`.  
3. Output must include `required_data` and `success_criteria`.  


---


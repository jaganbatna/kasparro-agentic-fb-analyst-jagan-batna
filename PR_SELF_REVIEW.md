# PR Self-Review Checklist

Before submitting this PR, ensure:

## Code Quality
- [ ] All agents return valid JSON
- [ ] Inputs/outputs match documentation
- [ ] No hardcoded file paths
- [ ] No unused imports or dead code

## Architecture
- [ ] Planner → Data → Insight → Evaluator → Creative chain works
- [ ] Evaluator feedback loop implemented
- [ ] Prompts are modular and stored in /prompts

## Outputs
- [ ] insights.json generated correctly
- [ ] creatives.json includes 2–3 variations
- [ ] report.md readable and complete

## Documentation
- [ ] README updated
- [ ] agent_graph.md updated with diagram
- [ ] config.json included

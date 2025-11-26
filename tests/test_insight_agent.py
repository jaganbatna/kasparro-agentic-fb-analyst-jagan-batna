import json

def test_insight_confidence_range():
    hypothesis = {"initial_confidence": 0.55}
    assert 0.0 <= hypothesis["initial_confidence"] <= 1.0

def test_insight_required_fields():
    hypothesis = {
        "id": "h1",
        "campaign_name": "C-A",
        "hypothesis": "Creative fatigue",
        "reason": "CTR below average",
        "expected_signals": ["ctr_drop > 20%"],
        "initial_confidence": 0.62
    }
    required = ["id", "campaign_name", "hypothesis", "reason", "expected_signals", "initial_confidence"]
    for r in required:
        assert r in hypothesis

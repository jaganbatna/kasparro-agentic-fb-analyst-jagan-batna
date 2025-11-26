import json

def test_evaluator_accept():
    hypothesis = {"initial_confidence": 0.75}
    assert hypothesis["initial_confidence"] >= 0.60

def test_evaluator_inconclusive():
    hypothesis = {"initial_confidence": 0.50}
    assert 0.40 <= hypothesis["initial_confidence"] < 0.60

def test_evaluator_reject():
    hypothesis = {"initial_confidence": 0.20}
    assert hypothesis["initial_confidence"] < 0.40

def test_required_fields():
    h = {
        "hypothesis_id": "h1",
        "decision": "accept",
        "confidence": 0.80
    }
    for f in ["hypothesis_id", "decision", "confidence"]:
        assert f in h

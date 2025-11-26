import json

def test_summary_keys_exist():
    summary = {
        "global_kpis": {},
        "by_campaign": [],
        "creative_signals": {}
    }
    assert "global_kpis" in summary
    assert "by_campaign" in summary
    assert "creative_signals" in summary

def test_ctr_calculation():
    clicks = 50
    impressions = 1000
    ctr = clicks / impressions
    assert round(ctr, 4) == 0.05

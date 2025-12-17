from src.app.cli import run_zero_ground

def test_zero_ground_passes():
    result = run_zero_ground()
    assert result["crucible"]["pass"] is True
    assert result["diagnostics"]["chemistry"]["tone"] == "calm"
    assert result["blue_team"]["tone"] == "calm"

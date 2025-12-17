def soldier_alert_thresholds():
    return {
        "hydration_low": True,
        "stress_high": True,
        "calibration_drift": True
    }

def notify_medics_minimal():
    return {"alert": "Soldier requires assistance", "data_exposed": "minimal"}

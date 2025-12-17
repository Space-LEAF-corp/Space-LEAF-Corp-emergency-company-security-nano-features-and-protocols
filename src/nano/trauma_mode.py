def trauma_mode_cues():
    return [
        "Stay calm.",
        "Stay still. Help is en route.",
        "Breathe gently. Await your team."
    ]

def stabilize(scaffold: NanoScaffoldSim):
    scaffold.enter_safe_mode()
    return {"stabilized": True, "cues": trauma_mode_cues()}

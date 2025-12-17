class NanoScaffoldSim:
    def __init__(self):
        self.state = "idle"

    def bridge_mode(self):
        self.state = "bridging"
        return {"status": "ok", "latency_ms": 3.2, "fidelity": 0.98}

    def enter_safe_mode(self):
        self.state = "safe-mode"
        return {"status": "ok", "caps_tightened": True}

from dataclasses import dataclass
from typing import Optional

@dataclass
class Principal:
    name: str  # "Patient" or "MedicalRole"

@dataclass
class Session:
    patient_present: bool
    medical_present: bool
    proximity_ok: bool
    timebox_minutes: int
    scope: str

class ZeroTrustGate:
    def __init__(self, timebox_minutes: int = 20):
        self.timebox_minutes = timebox_minutes

    def allow(self, session: Session) -> bool:
        return (
            session.patient_present
            and session.medical_present
            and session.proximity_ok
            and session.timebox_minutes <= self.timebox_minutes
            and session.scope in ["bridge_mode", "trauma_stabilize", "calibration_check"]
        )

    def deny(self) -> dict:
        return {"allowed": False, "reason": "Dual control or constraints not satisfied."}

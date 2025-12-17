import uuid
from datetime import datetime

def dual_consent_handshake(patient_key_attested: bool,
                           medical_key_attested: bool,
                           device_attested: bool,
                           scope: str) -> dict:
    if not (patient_key_attested and medical_key_attested and device_attested):
        return {"ok": False, "error": "Attestation failure"}
    if scope not in ["bridge_mode", "trauma_stabilize", "calibration_check"]:
        return {"ok": False, "error": "Scope not permitted"}
    return {
        "ok": True,
        "sessionId": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "scope": scope
    }

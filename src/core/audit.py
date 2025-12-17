import hashlib
from datetime import datetime

def audit_event(principal: str, action: str, scope: str, result: str) -> dict:
    payload = f"{principal}|{action}|{scope}|{result}|{datetime.utcnow().isoformat()}"
    return {
        "eventId": hashlib.sha256(payload.encode()).hexdigest(),
        "timestamp": datetime.utcnow().isoformat(),
        "principal": principal,
        "action": action,
        "scope": scope,
        "result": result,
        "hash": hashlib.sha256(payload.encode()).hexdigest()
    }

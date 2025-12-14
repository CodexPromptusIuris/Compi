from datetime import datetime

def generate_evidence(control_id, status):
    return {
        "control": control_id,
        "status": status,
        "timestamp": datetime.utcnow().isoformat(),
        "source": "Compliance App"
    }

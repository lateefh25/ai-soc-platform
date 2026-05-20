import uuid

def create_incident(log, analysis):

    return {
        "incident_id": str(uuid.uuid4())[:8],
        "log": log,
        "severity": analysis["severity"],
        "threat": analysis["threat"],
        "status": "OPEN"
    }

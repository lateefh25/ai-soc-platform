def analyze(log):

    log = log.lower()

    if "failed" in log:
        return {
            "severity": "HIGH",
            "threat": "Brute Force Attempt"
        }

    elif "malware" in log:
        return {
            "severity": "CRITICAL",
            "threat": "Malware Infection"
        }

    elif "port scan" in log:
        return {
            "severity": "MEDIUM",
            "threat": "Recon Activity"
        }

    else:
        return {
            "severity": "LOW",
            "threat": "Normal Activity"
        }

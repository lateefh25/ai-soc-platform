from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random
import asyncio

app = FastAPI()


logs = []


fake_logs = [
    "FAILED LOGIN from 192.168.1.12",
    "MALWARE DETECTED on HOST-22",
    "PORT SCAN DETECTED from 45.33.21.9",
    "SUCCESSFUL LOGIN from 192.168.1.20",
    "RANSOMWARE ACTIVITY DETECTED",
    "MULTIPLE PASSWORD FAILURES",
    "UNAUTHORIZED ACCESS ATTEMPT",
]


def analyze_log(log):

    log = log.lower()

    if "failed" in log:
        return "⚠️ Brute Force Attempt"

    elif "malware" in log:
        return "🚨 Malware Threat"

    elif "port scan" in log:
        return "🔍 Recon Activity"

    elif "ransomware" in log:
        return "☠️ Critical Threat"

    else:
        return "✅ Normal Activity"


async def generate_logs():

    while True:

        new_log = random.choice(fake_logs)

        threat = analyze_log(new_log)

        logs.insert(0, {
            "log": new_log,
            "threat": threat
        })

        if len(logs) > 15:
            logs.pop()

        await asyncio.sleep(3)


@app.on_event("startup")
async def startup_event():

    asyncio.create_task(generate_logs())


@app.get("/", response_class=HTMLResponse)
async def dashboard():

    html_logs = ""

    for item in logs:

        html_logs += f"""

        <div style="
            border:1px solid lime;
            padding:15px;
            margin-bottom:15px;
            border-radius:10px;
        ">

            <h3>{item['log']}</h3>

            <p>{item['threat']}</p>

        </div>
        """


    return f"""

    <html>

    <head>

        <title>AI SOC Dashboard</title>

        <meta http-equiv="refresh" content="3">

    </head>

    <body style="
        background:black;
        color:lime;
        font-family:Arial;
        padding:30px;
    ">

        <h1>🛡️ LIVE AI SOC DASHBOARD</h1>

        <h3>Real-Time Threat Monitoring</h3>

        {html_logs}

    </body>

    </html>
    """
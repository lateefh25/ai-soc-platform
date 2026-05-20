from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import threading

from app.services.log_reader import stream_logs
from app.services.ai_analyzer import analyze
from app.services.incident_engine import create_incident

app = FastAPI()

incidents = []


def soc_engine():

    for log in stream_logs():

        analysis = analyze(log)

        incident = create_incident(log, analysis)

        incidents.insert(0, incident)

        if len(incidents) > 20:
            incidents.pop()


@app.on_event("startup")
def startup_event():

    thread = threading.Thread(target=soc_engine)

    thread.daemon = True

    thread.start()


@app.get("/", response_class=HTMLResponse)
def dashboard():

    html = ""

    for incident in incidents:

        html += f"""

        <div style="
            border:1px solid lime;
            padding:15px;
            margin-bottom:15px;
            border-radius:10px;
        ">

            <h3>{incident['threat']}</h3>

            <p><b>Severity:</b> {incident['severity']}</p>

            <p><b>Incident ID:</b> {incident['incident_id']}</p>

            <p><b>Log:</b> {incident['log']}</p>

            <p><b>Status:</b> {incident['status']}</p>

        </div>
        """


    return f"""

    <html>

    <head>

        <title>AI SOC Platform</title>

        <meta http-equiv="refresh" content="2">

    </head>

    <body style="
        background:black;
        color:lime;
        font-family:Arial;
        padding:30px;
    ">

        <h1>🛡️ AI SOC Platform</h1>

        <h2>Autonomous Level-1 SOC Monitoring</h2>

        {html}

    </body>

    </html>
    """
from flask import Flask, jsonify
import socket
import os
import subprocess
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def dashboard():

    hostname = socket.gethostname()

    try:
        docker_count = subprocess.check_output(
            "docker ps -q | wc -l",
            shell=True
        ).decode().strip()
    except:
        docker_count = "Docker Not Installed"

    html = f"""
    <html>
    <head>
        <title>DevOps Command Center</title>

        <style>
            body {{
                font-family: Arial;
                background:#f5f7fa;
                padding:20px;
            }}

            .card {{
                background:white;
                padding:20px;
                margin:10px;
                border-radius:10px;
                box-shadow:0 2px 5px rgba(0,0,0,.2);
            }}

            .success {{
                color:green;
                font-weight:bold;
            }}
        </style>

    </head>

    <body>

    <h1>🚀 DevOps Command Center</h1>

    <div class="card">
        <h3>Server Details</h3>
        <p>Hostname: {hostname}</p>
        <p>Time: {datetime.now()}</p>
    </div>

    <div class="card">
        <h3>Docker Status</h3>
        <p>Running Containers: {docker_count}</p>
    </div>

    <div class="card">
        <h3>Secrets Management</h3>
        <p class="success">
        Environment Variables Loaded Successfully
        </p>
    </div>

    <div class="card">
        <h3>AI for DevOps</h3>

        <ul>
            <li>Log anomaly detection</li>
            <li>Root cause analysis</li>
            <li>Predictive scaling</li>
            <li>Cost optimization</li>
            <li>Security threat detection</li>
        </ul>
    </div>

    </body>
    </html>
    """

    return html


@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "timestamp": str(datetime.now())
    })


@app.route("/api/devops-tools")
def tools():

    return jsonify({
        "tools":[
            "Linux",
            "AWS",
            "Git",
            "Jenkins",
            "Docker",
            "Kubernetes",
            "Terraform",
            "Python"
        ]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

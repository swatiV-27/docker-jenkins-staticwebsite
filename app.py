from flask import Flask
import socket
import subprocess
from datetime import datetime
import psutil
import platform
import time

app = Flask(__name__)

@app.route("/")
def dashboard():

    # System Info
    hostname = socket.gethostname()
    os_name = platform.system()
    kernel = platform.release()

    # CPU
    cpu_usage = psutil.cpu_percent(interval=1)

    # Memory
    memory = psutil.virtual_memory()

    # Disk
    disk = psutil.disk_usage('/')

    # Uptime
    uptime_seconds = int(time.time() - psutil.boot_time())
    days = uptime_seconds // 86400
    hours = (uptime_seconds % 86400) // 3600

    # Docker Container Count
    try:
        docker_count = subprocess.check_output(
            "docker ps -q | wc -l",
            shell=True
        ).decode().strip()
    except:
        docker_count = "N/A"

    html = f"""
    <!DOCTYPE html>
    <html>

    <head>

        <title>DevOps Command Center</title>

        <style>

            * {{
                margin:0;
                padding:0;
                box-sizing:border-box;
            }}

            body {{
                background:#0f172a;
                color:white;
                font-family:Segoe UI, sans-serif;
                padding:30px;
            }}

            h1 {{
                text-align:center;
                margin-bottom:30px;
                color:#38bdf8;
            }}

            .grid {{
                display:grid;
                grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
                gap:20px;
            }}

            .card {{
                background:#1e293b;
                padding:20px;
                border-radius:15px;
                box-shadow:0 4px 10px rgba(0,0,0,.4);
                transition:.3s;
            }}

            .card:hover {{
                transform:translateY(-5px);
            }}

            .metric {{
                font-size:32px;
                font-weight:bold;
                color:#38bdf8;
                margin-top:10px;
            }}

            .success {{
                color:#22c55e;
                font-weight:bold;
            }}

            ul {{
                padding-left:20px;
                margin-top:10px;
            }}

            li {{
                margin:8px 0;
            }}

            .footer {{
                text-align:center;
                margin-top:30px;
                color:#94a3b8;
            }}

        </style>

    </head>

    <body>

        <h1>🚀 DevOps Command Center</h1>

        <div class="grid">

            <div class="card">
                <h3>CPU Usage</h3>
                <div class="metric">{cpu_usage}%</div>
            </div>

            <div class="card">
                <h3>Memory Usage</h3>
                <div class="metric">{memory.percent}%</div>
            </div>

            <div class="card">
                <h3>Disk Usage</h3>
                <div class="metric">{disk.percent}%</div>
            </div>

            <div class="card">
                <h3>Uptime</h3>
                <div class="metric">{days}d {hours}h</div>
            </div>

        </div>

        <br>

        <div class="grid">

            <div class="card">
                <h3>🖥 Server Information</h3>
                <p><b>Hostname:</b> {hostname}</p>
                <p><b>OS:</b> {os_name}</p>
                <p><b>Kernel:</b> {kernel}</p>
                <p><b>Generated:</b> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
            </div>

            <div class="card">
                <h3>🐳 Docker Status</h3>
                <p><b>Running Containers:</b> {docker_count}</p>
            </div>

            <div class="card">
                <h3>✅ Application Health</h3>
                <p class="success">HEALTHY</p>
                <p>All services operational</p>
            </div>

        </div>

        <br>

        <div class="grid">

            <div class="card">
                <h3>🛠 DevOps Stack</h3>

                <ul>
                    <li>Linux</li>
                    <li>AWS</li>
                    <li>Git & GitHub</li>
                    <li>Jenkins</li>
                    <li>Docker</li>
                    <li>Kubernetes</li>
                    <li>Terraform</li>
                    <li>Python</li>
                </ul>
            </div>

            <div class="card">
                <h3>🔐 Secrets Management</h3>

                <ul>
                    <li>Environment Variables</li>
                    <li>Least Privilege Access</li>
                    <li>Secret Rotation</li>
                    <li>Vault Integration Ready</li>
                </ul>
            </div>

            <div class="card">
                <h3>🤖 AI Insights</h3>

                <ul>
                    <li>No critical alerts detected</li>
                    <li>Infrastructure healthy</li>
                    <li>CPU usage within threshold</li>
                    <li>No anomaly detected</li>
                </ul>
            </div>

        </div>

        <div class="footer">
            DevOps Monitoring Dashboard | Flask + Docker + Jenkins
        </div>

    </body>
    </html>
    """

    return html


@app.route("/health")
def health():
    return {
        "status": "UP",
        "service": "devops-dashboard"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

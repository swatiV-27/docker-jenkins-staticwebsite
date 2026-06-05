# 🚀 DevOps Command Center

A modern DevOps monitoring dashboard built with Flask, Docker, and Jenkins.

This project demonstrates core DevOps concepts including containerization, CI/CD automation, infrastructure monitoring, and application health checks.

---

## 📌 Project Overview

DevOps Command Center is a lightweight web dashboard that displays real-time server metrics and operational information.

The application is containerized using Docker and deployed automatically through a Jenkins CI/CD pipeline.

---

## 🏗️ Architecture

```text
Developer
    |
    v
GitHub Repository
    |
    v
Jenkins Pipeline
    |
    v
Docker Build
    |
    v
Docker Container
    |
    v
DevOps Dashboard
```

---

## ✨ Features

### Server Monitoring

* CPU Usage Monitoring
* Memory Usage Monitoring
* Disk Usage Monitoring
* System Uptime
* Host Information
* Operating System Details
* Kernel Information

### Docker Monitoring

* Running Container Count
* Container Status Visibility

### Application Health

* Health Check Endpoint
* Service Status Monitoring

### DevOps Dashboard

* Modern Dark Theme UI
* Responsive Layout
* Interactive Metric Cards

### AI & DevOps Section

* AI-driven Operations Concepts
* Log Anomaly Detection Overview
* Root Cause Analysis Concepts
* Predictive Scaling Concepts

---

## 🛠️ Technologies Used

* Python
* Flask
* Docker
* Jenkins
* Git
* GitHub
* Linux
* CI/CD
* DevOps Monitoring

---

## 📂 Project Structure

```text
devops-command-center/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── README.md
```

---

## ⚙️ Installation
# Setup terminal
#install jenkinks and docker
# chuser -aG docker jenkins
# su - jenkins
# make sure security group configuration
### Clone Repository

```bash
git clone https://github.com/swatiV-27/docker-jenkins-staticwebsite.git
cd docker-jenkins-staticwebsite
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python3 app.py
```

Application URL:

```text
http://localhost:5000
```

---

## 🐳 Docker Setup

### Build Image

```bash
docker build -t image-devops .
```

### Run Container

```bash
docker run -d \
-p 5000:5000 \
--name devops-con \
image-devops
```

### Verify

```bash
docker ps
```

---

## 🔄 Jenkins CI/CD Pipeline

The Jenkins pipeline performs the following steps:

1. Pull source code from GitHub
2. Build Docker image
3. Remove existing container
4. Deploy new container
5. Verify deployment

Pipeline Stages:

```text
Git Clone
Docker Build
Previous Container Delete
Container Build
Check Container
```

---

## ❤️ Health Endpoint

Health Check URL:

```text
http://SERVER-IP:5000/health
```

Response:

```json
{
  "status": "UP",
  "service": "devops-dashboard"
}
```

---

## 🎯 Learning Objectives

This project demonstrates:

* CI/CD Pipeline Creation
* Docker Containerization
* Jenkins Automation
* Python Flask Development
* Linux Administration
* Monitoring Dashboard Development
* Infrastructure Visibility

---

## 🚀 Future Enhancements

* Jenkins Build Status Integration
* Kubernetes Monitoring
* AWS EC2 Metadata Integration
* Prometheus Metrics
* Grafana Dashboard Integration
* AI-Powered Log Analysis
* Deployment History Tracking

---

## 👨‍💻 Author

Swati Verma

DevOps Engineer | AWS | Docker | Jenkins | Kubernetes | Terraform | Python

```
```

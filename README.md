# 🚀 Cloud Deployed Task Management API

## 🌐 Live Deployment

Production style backend API deployed on AWS EC2 with Docker, nginx reverse proxy, HTTPS/TLS, and AWS RDS PostgreSQL.

---

# 📌 Overview

This project is a production style Task Management REST API built using FastAPI and PostgreSQL.

The application is fully containerized using Docker and orchestrated with Docker Compose. It is deployed on AWS EC2 with nginx configured as a reverse proxy and HTTPS enabled using Let's Encrypt certificates.

This project helped me gain hands on experience with:

* Backend Engineering
* Cloud Infrastructure
* DevOps Fundamentals
* Linux Server Management
* Reverse Proxy Architecture
* HTTPS/TLS Configuration
* Containerized Deployments
* Production Debugging Workflows

---

# ⚙️ Tech Stack

## Backend

* FastAPI
* SQLAlchemy ORM
* JWT Authentication

## Database

* PostgreSQL
* AWS RDS

## Infrastructure & DevOps

* Docker
* Docker Compose
* nginx Reverse Proxy
* AWS EC2
* Linux (Ubuntu)
* HTTPS/TLS
* Let's Encrypt
* Certbot

---

# 📌 Features

* User Authentication with JWT
* Create Tasks
* Read Tasks
* Update Tasks
* Delete Tasks
* PostgreSQL Integration
* Dockerized Infrastructure
* Reverse Proxy Configuration
* HTTPS Enabled Deployment
* Environment Variable Management

---

# 🏗️ Architecture

```text
User Browser
      ↓ HTTPS/TLS
nginx Reverse Proxy
      ↓
Docker Compose
      ↓
FastAPI Container
      ↓
AWS RDS PostgreSQL
```

---

# 🚀 API Endpoints

| Method | Endpoint    | Description   |
| ------ | ----------- | ------------- |
| POST   | /login      | User Login    |
| POST   | /tasks      | Create Task   |
| GET    | /tasks      | Get All Tasks |
| PUT    | /tasks/{id} | Update Task   |
| DELETE | /tasks/{id} | Delete Task   |

---

# 🔧 Infrastructure Concepts Learned

* Docker containerization
* Docker Compose orchestration
* nginx reverse proxy configuration
* HTTPS/TLS certificate flow
* Linux service management
* Environment variable isolation
* AWS EC2 deployment workflows
* AWS RDS connectivity
* JWT authentication basics
* Reverse proxy vs forward proxy

---

# 🧠 Deployment Challenges & Debugging

During deployment, I solved several real world backend and infrastructure issues including:

* 502 Bad Gateway errors
* nginx upstream configuration problems
* Docker container crashes
* Port conflicts
* PostgreSQL connectivity troubleshooting
* RDS security group configuration
* TLS certificate configuration
* Container networking issues
* Environment variable management
* Service restart and deployment debugging

---

# 📂 Project Structure

```text
task-api/
│
├── app/
├── nginx/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
```

---

# 🚀 Running Locally

## Clone Repository

```bash
git clone https://github.com/Abdullah-source78/task-api.git
cd task-api
```

---

## Start Services with Docker Compose

```bash
docker compose up --build
```

---

# 🌐 Access API Documentation

using public domain with HTTPS:
```text id="4h7j2x"
https://peertask.duckdns.org/docs
```

OR if using EC2 public IP with HTTP:

```text id="x8m1qa"
http://3.253.66.71:8000/docs
```

---

# 🔐 HTTPS & Security

* HTTPS enabled using Let's Encrypt certificates
* nginx configured for TLS termination
* Environment variables used for sensitive configurations
* JWT authentication implemented for secure access

---

# 📈 Current Focus

Currently learning and improving:

* API Authorization
* Docker Security Hardening
* CI/CD Pipelines
* Vulnerability Scanning
* Kubernetes
* Cloud Security
* DevSecOps Workflows

---

# 👨‍💻 Author

Muhammad Abdullah

Backend Engineering • Cloud Infrastructure • DevOps • DevSecOps

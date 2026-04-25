# 🚀 Cloud Deployed Task Management API

## 🌐 Live Deployment
Deployed on AWS EC2 and accessible via public IP

## 📌 Overview
This project is a RESTful Task Management API built using FastAPI and PostgreSQL.  
The application is containerized using Docker and deployed on AWS EC2.

It demonstrates real-world backend development including deployment, debugging, and system-level understanding.

---

## ⚙️ Tech Stack
- Backend: FastAPI  
- Language: Python  
- Database: PostgreSQL  
- ORM: SQLAlchemy  
- Containerization: Docker  
- Cloud: AWS EC2  

---

## 📌 Features
- Create, Read, Update, Delete tasks  
- PostgreSQL database integration  
- Dockerized application  
- Public API deployment on cloud  
- Background service using systemd  

---

## 📊 Architecture
User → EC2 → Docker Container → PostgreSQL

---

## 🚀 API Endpoints

| Method | Endpoint        | Description      |
|--------|----------------|------------------|
| POST   | /tasks         | Create task      |
| GET    | /tasks         | Get all tasks    |
| PUT    | /tasks/{id}    | Update task      |
| DELETE | /tasks/{id}    | Delete task      |

---

## 🧠 Challenges & Learnings

- Fixed app stopping issue by using systemd instead of running in foreground  
- Solved Docker networking issue (localhost inside container ≠ host machine)  
- Resolved PostgreSQL connection errors using listen_addresses and pg_hba.conf  
- Configured EC2 security groups for external access  

---

## 🔧 Setup Instructions

### 1.Clone repo
```bash
git clone https://github.com/Abdullah-source78/task-api.git
cd task-api

---

### 2.Install dependencies
pip install fastapi uvicorn sqlalchemy psycopg2-binary

---

### 3.Run app
uvicorn main:app --reload

---

### Future Improvements
Move database to AWS RDS
Add Docker Compose
Implement Nginx
Add HTTPS and domain
Setup CI/CD pipeline

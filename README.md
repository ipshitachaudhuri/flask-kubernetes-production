# Flask Kubernetes Production Deployment 🚀

A production-style Flask API deployment running on AWS EC2 using Docker, Kubernetes, PostgreSQL, NGINX Ingress, and Let's Encrypt HTTPS.

This project demonstrates containerization, Kubernetes orchestration, database deployment, SSL configuration, DNS setup, and production-style API hosting.

---

## 🌐 Live Application

API Health Check:

```
https://api.ipshitechnology.com/health
```

Response:

```json
{
  "status": "healthy"
}
```

---

# 🏗️ Architecture

```
                 Internet
                    |
                    |
        api.ipshitechnology.com
                    |
                    |
              AWS EC2 Instance
                    |
                    |
          NGINX Ingress Controller
                    |
                    |
              Flask API Service
                    |
                    |
              Flask Application
                    |
                    |
          PostgreSQL Database
```

---

# 🛠️ Technology Stack

## Backend

- Python
- Flask
- Gunicorn

## Containerization

- Docker
- Docker Images

## Kubernetes

- Kubernetes Deployments
- Kubernetes Services
- ConfigMaps
- Persistent Volume Claims
- Ingress Controller
- TLS Secrets

## Cloud

- AWS EC2
- Ubuntu Linux
- Security Groups
- DNS Configuration

## Security

- HTTPS
- Let's Encrypt SSL
- cert-manager

## Version Control

- Git
- GitHub

---

# ✨ Features

✅ Flask REST API  
✅ Docker containerization  
✅ Kubernetes deployment  
✅ PostgreSQL database  
✅ Persistent storage  
✅ Kubernetes service discovery  
✅ NGINX Ingress routing  
✅ Custom domain setup  
✅ HTTPS SSL certificate  
✅ Health monitoring endpoint  

---

# 📂 Project Structure

```
flask-kubernetes-production/

├── app/
│   ├── app.py
│   └── requirements.txt
│
├── k8s/
│   ├── deployments.yaml
│   ├── services.yaml
│   ├── ingress.yaml
│   ├── certificate.yaml
│   └── configmaps.yaml
│
├── Dockerfile
├── README.md
└── .gitignore
```

---

# ☸️ Kubernetes Deployment

Namespace:

```
flask-app
```

Components:

```
Flask API Deployment
        |
        |
Flask API Service
        |
        |
PostgreSQL Deployment
        |
        |
PostgreSQL Service
        |
        |
Persistent Storage
```

---

# 🚀 Deployment Steps

## Clone Repository

```bash
git clone https://github.com/ipshitachaudhuri/flask-kubernetes-production.git

cd flask-kubernetes-production
```

---

## Build Docker Image

```bash
docker build -t flask-api .
```

---

## Deploy Kubernetes Resources

```bash
kubectl apply -f k8s/
```

---

## Check Pods

```bash
kubectl get pods -n flask-app
```

Example:

```
flask-api       Running
postgres-db     Running
```

---

## Check Services

```bash
kubectl get svc -n flask-app
```

---

## Check Ingress

```bash
kubectl get ingress -n flask-app
```

Expected:

```
api.ipshitechnology.com
```

---

## Check SSL Certificate

```bash
kubectl get certificate -n flask-app
```

Expected:

```
flask-api-tls     True
```

---

# 🔍 API Testing

Command:

```bash
curl https://api.ipshitechnology.com/health
```

Response:

```json
{
  "status": "healthy"
}
```

---

# Useful Kubernetes Commands

View resources:

```bash
kubectl get all -n flask-app
```

View logs:

```bash
kubectl logs deployment/flask-api -n flask-app
```

Enter container:

```bash
kubectl exec -it deployment/flask-api -n flask-app -- sh
```

---

# 🔐 Security Implementation

Implemented:

- HTTPS encryption
- Let's Encrypt certificate
- cert-manager automation
- Kubernetes TLS secrets
- Internal PostgreSQL ClusterIP service
- Environment-based configuration

---

# 🔮 Future Improvements

- GitHub Actions CI/CD pipeline
- Automated Docker image build
- Kubernetes rolling deployment
- Prometheus monitoring
- Grafana dashboards
- Helm charts
- Horizontal Pod Autoscaling

---

# 💻 Skills Demonstrated

- AWS EC2
- Linux Administration
- Docker
- Kubernetes
- Flask
- PostgreSQL
- NGINX
- SSL/TLS
- DNS
- Git/GitHub
- DevOps Practices

---

# 👤 Author

**Ipshita Chaudhuri**

GitHub:

https://github.com/ipshitachaudhuri

---

⭐ Production-style Flask Kubernetes deployment project


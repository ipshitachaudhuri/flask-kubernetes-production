# Flask API Kubernetes Deployment

Production-style Flask API deployment using Kubernetes.

## Architecture

Client
 |
HTTPS
 |
NGINX Ingress Controller
 |
Flask API Service
 |
Flask Pod
 |
PostgreSQL Database


## Technologies

- Python Flask
- Docker
- Kubernetes
- PostgreSQL
- NGINX Ingress
- cert-manager
- Let's Encrypt SSL
- AWS EC2


## Deployment

Domain:

https://api.ipshitechnology.com


Health Check:

GET /health


Response:

{
  "status": "healthy"
}


## Kubernetes Components

- Flask Deployment
- PostgreSQL Deployment
- Services
- Ingress
- TLS Certificate


## Security

- HTTPS enabled
- PostgreSQL internal ClusterIP only
- Kubernetes service networking
- Restricted SSH access



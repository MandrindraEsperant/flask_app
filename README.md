# Flask Hello — Jenkins CI/CD Pipeline

A simple Flask web application used to demonstrate a complete CI/CD pipeline 
with Jenkins, Docker and Kubernetes.

## Stack
- **Python / Flask** — Web application
- **Docker** — Containerization
- **Jenkins + Blue Ocean** — CI/CD pipeline
- **Kubernetes** — Deployment orchestration

## Application Routes
| Route | Description |
|---|---|
| `/` | Returns `Hello World!` |
| `/hello/` | Returns `Hello World!` |
| `/hello/<username>` | Returns `Hello <username>!` |

## Pipeline Stages
1. **Test** — Run unit tests inside a Python container
2. **Build** — Build Docker image
3. **Push** — Push image to Docker Hub
4. **Deploy** — Deploy to Kubernetes cluster

## Run locally
```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
./test.py --verbose
```

## Run with Docker
```bash
docker build -t flask-hello .
docker run --rm -p 5000:5000 flask-hello
```
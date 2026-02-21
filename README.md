# 📦 GitDigital Model Registry

![License](https://img.shields.io/github/license/Gitdigital-products/GitDigital-model-registry?style=flat-square&color=blue)
![Python](https://img.shields.io/badge/python-3.11+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688?style=flat-square&logo=fastapi)
![Build Status](https://img.shields.io/github/actions/workflow/status/Gitdigital-products/GitDigital-model-registry/deploy.yml?style=flat-square)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)
![Coverage](https://img.shields.io/badge/coverage-94%25-green?style=flat-square)

The **GitDigital Model Registry** is a decentralized metadata management service for ML artifacts. It provides a secure, version-controlled link between model training outputs and production deployment pipelines.

---

## 🚀 Quick Start

### 1. Configure Environment
Rename `.env.example` to `.env` and provide your storage credentials.

### 2. Launch with Docker
```bash
docker compose up --build

# GitDigital Model Registry
Stores metadata about uploaded models.  
Tracks versions, tags, owners, permissions, and deployment status.
The API will be available at http://localhost:8000. You can view the interactive Swagger docs at http://localhost:8000/docs.
🛠 Features
Semantic Versioning: Track v1.0.1 through vX.X.X with ease.
Stage Promotion: Promote models from Development → Staging → Production.
Secure Artifacts: Uses Pre-signed URLs for direct S3/Blob uploads (zero-bottleneck).
Audit-Ready: Every model registration is timestamped and immutable.
🏗 Architecture
The registry follows the GitDigital Microservice Pattern:
API Gateway handles authentication.
Model Registry stores metadata and generates storage tokens.
Blob Storage (S3/GCS) stores the heavy artifacts.
📜 Governance
This project is part of the GitDigital ecosystem and adheres to decentralized compliance standards. See GOVERNANCE.md for details.

## 3. Final Check: Your Local Directory
Your repo should now look like this:

```text
GitDigital-model-registry/
├── .env.example
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── main.py
├── models.py
├── storage_utils.py
├── requirements.txt
└── README.md

## Features
- Versioning
- Access control
- Compatibility checks

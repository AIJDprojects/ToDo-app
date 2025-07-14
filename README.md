# ✅ AI-Powered ToDo Manager - FastAPI + React

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black)](https://react.dev)
[![Docker](https://img.shields.io/badge/Docker-✓-blue?logo=docker)](https://docker.com)

**Intelligent task management with AI suggestions**  
A Dockerized full-stack application featuring:
- FastAPI backend with CRUD operations
- React frontend with responsive UI
- Gemini/CodeGPT integration for smart task analysis
- SQLite database persistence


## 🚀 Key Features
- **Smart Task Management**  
  Create, update, and organize tasks with completion tracking
- **AI-Powered Insights**  
  Get intelligent suggestions using Gemini or CodeGPT APIs
- **Seamless Integration**  
  Pre-configured CORS for frontend-backend communication
- **Production-Ready**  
  Dockerized environment with single-command setup
- **Flexible AI Backends**  
  Switch between Gemini and CodeGPT with environment variables


## ⚙️ Installation
### 1. Configure Environment
Create backend/todo_ai/.env with your API keys:

#### Required for Gemini
GEMINI_API_KEY="your_gemini_key"

#### Required for CodeGPT
CODEGPT_API_BASE="https://api.codegpt.co/api/v1/chat/completions"

AGENT_ID="your_agent_id"

ORGANIZATION_ID="your_org_id"

#### Select AI provider (gemini or codegpt)

API_MODEL="gemini"  

### 2. Start Services

docker-compose up --build

## 🚦 Usage
### Access Applications:

Frontend: http://localhost:8090

Backend: http://localhost:8070

### Task Management:

- Add tasks with titles/descriptions

- Mark tasks as complete

- Edit or delete existing tasks

## 🌐 API Endpoints
### CRUD Operations (/crud)

Endpoint	Method	Description

- /tasks	GET	List all tasks

- /tasks	POST	Create new task

- /tasks/{id}	GET	Get task details

- /tasks/{id}	PUT	Update task

- /tasks/{id}	DELETE	Remove task


## 🧩 Tech Stack
```mermaid
graph LR
    A[React Frontend] --> B[FastAPI Backend]
    B --> C[SQLite Database]
    B --> D[AI Services]
    D --> E[Gemini API]
    D --> F[CodeGPT API]

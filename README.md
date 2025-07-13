# ToDo List Application - FastAPI & React Dockerized Implementation

## Overview  
A full-stack ToDo application featuring a FastAPI backend and React frontend, containerized using Docker. The backend provides robust CRUD operations for task management and integrates AI-powered features through dedicated API endpoints. The application is designed for easy setup.

## Key Features  
- **Task Management**  
  - Create/Read/Update/Delete tasks  
  - Track task details: Title, Description, Creation/End Time, Completion Status  
  - SQLite database persistence  
- **AI Integration**  
  - LLM-powered endpoints for smart task suggestions/analysis  
- **RESTful API Endpoints**  
  - CRUD Operations: `/crud`  
  - AI Features: `/llm`  
- **CORS Configuration**  
  - Pre-configured for seamless frontend-backend communication  

## Project Structure  

├── backend/ # FastAPI server
│ ├── api.py # Core API setup & routing
│ ├── main.py # Uvicorn server launcher
│ ├── todo_db/ # Database operations (CRUD, models)
│ ├── todo_ai/ # AI integration
│ └── .env # Environment configuration
├── frontend/ # React application
└── docker-compose.yaml # Multi-container orchestration

## Setup with Docker Compose  

The app gives you the option to use gemini or CodeGPT APIs, but in order of those to work the APIkeys must be in the next file as follows:

### 1. Create Environment File  
Add `backend/todo_ai/.env` with these variables: 

OPENAI_API_KEY=
CODEGPT_API_BASE=https://api.codegpt.co/api/v1/chat/completions
AGENT_ID=
ORGANIZATION_ID=
API_MODEL=               # variable that set up the usage of the model values: gemini or codegpt 
GEMINI_API_KEY=

### 2. Build and Launch

docker-compose up --build

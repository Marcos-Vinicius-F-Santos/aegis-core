# Aegis-Core

![Status](https://img.shields.io/badge/status-development-orange)

Aegis-Core is a local AI orchestration framework designed to run personal AI agents on local hardware.

The goal of this project is to provide a functional and extensible core where each user can deploy, configure and customize their own local AI environment, maintaining their own context, models and workflows.

The philosophy behind Aegis-Core:

> Provide the engine. Each user builds their own intelligence.

---

# Overview

Aegis-Core is being developed as a local AI ecosystem, similar to a personal assistant architecture, where specialized agents can work together to execute different types of tasks.

The system is designed around independent AI services:

| Agent | Responsibility |
|---|---|
| Vex | System control, API gateway and orchestration |
| Cortex | Conversation and contextual interaction |
| Cortana | Programming and software development assistance |
| Rick | Research and information gathering |

---

# Project Status

Current development stage:

**Foundation layer completed.**

Implemented:

- Ubuntu server environment
- Remote administration through SSH
- Local network communication
- Docker environment
- Ollama local LLM runtime
- FastAPI service foundation
- Vex core service
- Basic agent structure
- GitHub repository and version control

---

# Hardware Environment

Aegis-Core currently runs on a dedicated notebook configured as a local AI server.

Operating system:

```
Ubuntu 26.04 LTS
```

Device hostname:

```
aegis-core
```

Network:

```
Desktop
   |
   | SSH / HTTP
   |
Aegis-Core Notebook
```

The notebook works as the local intelligence host while other devices can communicate with it through the network.

---

# Infrastructure Setup

## SSH Remote Access

Configured:

- SSH server
- Remote terminal access
- Secure communication between desktop and notebook

The desktop can access Aegis-Core remotely:

```bash
ssh marcos-santos@192.168.0.10
```

---

# Docker Environment

Docker was installed and configured.

Implemented:

- Docker Engine
- Docker Compose V2
- Docker service enabled on startup
- User permissions configured

Verification:

```bash
docker --version
```

Current environment:

```
Docker 29.1.3
```

---

# Local AI Runtime

Ollama was installed as the local model execution layer.

Current API:

```
http://0.0.0.0:11434
```

The service was tested externally from the desktop machine.

Example:

```powershell
curl http://192.168.0.10:11434/api/generate
```

Result:

```
HTTP 200 OK
```

The local AI inference pipeline is operational.

---

# Aegis Directory Structure

Main project directory:

```
/opt/aegis
```

Current architecture:

```
/opt/aegis

├── api
├── config
├── data
├── logs
├── models
├── prompts
├── scripts
├── services
│
│   ├── cortana
│   ├── cortex
│   ├── rick
│   └── vex
│
└── shared
```

---

# Vex Service

Vex is the first implemented service in Aegis-Core.

Purpose:

- Receive requests
- Manage communication
- Connect agents
- Interface with local AI models

Technology stack:

```
Python 3.14
FastAPI
Uvicorn
Pydantic
Requests
Ollama API
```

Location:

```
/opt/aegis/services/vex
```

Virtual environment:

```
.venv
```

Installed dependencies:

```
fastapi
uvicorn
pydantic
requests
```

---

# Current Vex Structure

```
aegis-core/

└── aegis/

    ├── config/

    │   └── vex/

    │       └── config.json


    └── services/

        └── vex/

            ├── agents/

            │   └── cortex.py

            ├── app.py
            ├── config.py
            ├── main.py
            ├── models.py
            ├── ollama.py
            └── router.py
```

---

# API Execution

The Vex service runs using:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Current communication flow:

```
User
 |
Vex API
 |
Agent Layer
 |
Ollama
 |
Local Model
 |
Response
```

---

# Development Problems Solved

## Docker Permission Error

Problem:

```
permission denied while trying to connect to docker API
```

Cause:

User did not have Docker group permissions.

Solution:

```bash
sudo usermod -aG docker $USER
```

After restarting the session Docker commands worked normally.

---

## Python Dependencies

Problem:

```
No module named pydantic
```

Cause:

Packages were installed outside the virtual environment.

Solution:

Created and configured:

```
.venv
```

Installed dependencies inside the environment.

---

## Python Structure Error

Problem:

```
Return outside function
```

Cause:

Incorrect indentation and function structure.

Solution:

Reviewed Python file structure and corrected implementation.

---

## Ollama Remote Access

Problem:

Need to validate communication from another machine.

Solution:

Configured Ollama network exposure.

Result:

```
HTTP 200 OK
```

---

## GitHub Authentication

Problem:

SSH key authentication was not accepted by GitHub.

Solution:

Moved authentication to GitHub CLI.

Current state:

- GitHub CLI authenticated
- Repository connected
- Push working

---

# Git Repository

Repository:

```
aegis-core
```

Branch:

```
main
```

Initial commit:

```
Initial Aegis Core structure
```

Current tracked files:

```
.gitignore

aegis/config/vex/config.json

aegis/services/vex/
    agents/cortex.py
    app.py
    config.py
    main.py
    models.py
    ollama.py
    router.py
```

---

# Development Philosophy

Aegis-Core is designed as an open local AI framework.

The project provides:

- Core infrastructure
- Agent architecture
- Communication layer
- Local execution environment

Each user can define:

- Personal context
- Local memory
- Models
- Prompts
- Specialized behaviors

The goal is privacy, customization and extensibility.

---

# Roadmap

## Phase 1 - Foundation

Completed:

- [x] Ubuntu environment
- [x] Device configuration
- [x] SSH access
- [x] Docker installation
- [x] Ollama integration
- [x] Vex API foundation
- [x] GitHub repository

---

## Phase 2 - Intelligence Core

Next:

- [ ] Agent communication system
- [ ] Persistent memory
- [ ] Context management
- [ ] Prompt system
- [ ] Model management
- [ ] Local knowledge base

---

## Phase 3 - Specialized Agents

Planned:

- [ ] Cortex conversational agent
- [ ] Cortana coding agent
- [ ] Rick research agent
- [ ] Advanced Vex orchestration

---

# License

To be defined.

---

# Author

Marcos Vinicius

Aegis-Core Project

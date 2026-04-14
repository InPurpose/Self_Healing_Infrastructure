## Structure


```
self-healing-infrastructure/
│
├── 1-chaos-app-target/          # Person A's Domain: The "Patient"
│   ├── api/                     # Tool: FastAPI
│   ├── database/                # Tool: PostgreSQL + SQLModel
│   ├── chaos_injector/          # Tool: Python (Custom fault logic)
│   └── Dockerfile               # Tool: Docker
│
├── 2-observability-pipeline/    # Person B's Domain: The "Monitor"
│   ├── log_collector/           # Tool: Promtail or FluentBit
│   ├── log_storage/             # Tool: Grafana Loki or Elasticsearch
│   └── dashboards/              # Tool: Grafana
│
├── 3-agentic-healer/            # Person C's Domain: The "Doctor"
│   ├── llm_orchestrator/        # Tool: LangChain or LlamaIndex
│   ├── vector_store/            # Tool: ChromaDB (for storing past fixes/docs)
│   ├── mcp_tools/               # Tool: Model Context Protocol (to execute commands)
│   └── Dockerfile
│
└── docker-compose.yml           # Tool: Docker Compose (Spins up everything together)
```

```
self-healing-infrastructure/
├── docker-compose.yml           # Orchestrates all 3 systems
├── README.md
│
├── 1-chaos-app-target/          # The "Patient" (FastAPI Backend)
│   ├── Dockerfile               # Config lives outside src/
│   ├── pyproject.toml           # Dependency management 
│   └── src/                     # ALL actual Python code goes in here
│       ├── api/                 # FastAPI routers
│       ├── database/            # SQLAlchemy models and connections
│       ├── chaos_injector/      
│       └── main.py              
│
├── 2-observability-pipeline/    # The "Monitor" (Infrastructure)
│   ├── loki-config.yaml         # Config files, no src/ needed here
│   ├── promtail-config.yaml     # since it's mostly yaml configurations
│   └── grafana-dashboards/      
│
└── 3-agentic-healer/            # The "Doctor" (AI Agent)
    ├── Dockerfile               
    ├── pyproject.toml           
    └── src/                     # Python code goes in here
        ├── llm_orchestrator/    
        ├── mcp_tools/           
        └── main.py

```

### What is the "Chaos App" and what should it look like?
You mentioned knowing what a chaos app does (injects failure), but not what it looks like in the context of an auto-fixing agent.

Think of the Chaos App as your Target Environment. If your RAG Agent is the immune system, the Chaos App is a normal body that you are intentionally infecting with viruses to see if the immune system works.

It should look like a completely standard, boring application—for example, a simple E-commerce Inventory API or a Financial Transaction Service. It needs normal endpoints (GET /inventory, POST /checkout).

However, you will build a "secret" set of endpoints—the Chaos Controller—that intentionally breaks the app.


```
CREATE DATABASE ChaosApp;
CREATE USER chaos_app_user WITH PASSWORD '123456';
GRANT ALL ON SCHEMA public TO chaos_app_user;
```
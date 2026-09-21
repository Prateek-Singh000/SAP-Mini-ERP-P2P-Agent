🚀 SAP Mini-ERP P2P (Procure-to-Pay) AI Assistant🌱 About SAP Mini-ERP P2P AISAP Mini-ERP P2P AI Assistant is a comprehensive, production-ready procurement management platform built to bridge the gap between heavy enterprise database workflows and intelligent automation.Instead of requiring complex enterprise GUI navigation or deep SQL expertise, this platform gives stakeholders two unified ways to interact with supply chain data:Traditional UI Form Layer: A real-time Streamlit dashboard to create, track, and manage purchase orders.Autonomous AI Assistant Layer: A conversational ReAct agent powered by Google Gemini and LangChain that parses natural language questions to query, inspect, and audit your live SAP HANA database securely.Plaintext       💬 User Prompt / Sidebar Form
                  ↓
       🌐 Streamlit Frontend UI
                  ↓
       🚀 FastAPI Backend REST Layer
                  ↓
       🧠 LangChain ReAct AI Agent ──→ 🤖 Google Gemini LLM
                  ↓
       🗄️ SQLAlchemy Core Engine
                  ↓
       🏢 SAP HANA Cloud Database
✨ Key Features🏢 Enterprise SAP HANA BackendConnected natively to an SAP HANA database using SQLAlchemy and the sqlalchemy-hana dialect for robust relational procurement management.⚡ Asynchronous FastAPI REST LayerClean, modular backend architecture handling REST routing, data serialization, transaction commits, and approval state transitions.🤖 Autonomous LangChain ReAct AI AgentLeverages advanced LLM agents to dynamically translate unstructured user queries (e.g., "What is the status and total amount for PO ID 1?") into precise SQL executions.📊 Interactive Streamlit FrontendProvides both a dynamic transactional sidebar form for quick purchase order generation and a sleek, responsive conversational dashboard.🔄 End-to-End Procurement LifecycleManages the full supplier-to-settlement pipeline—tracking Vendors, Raw Materials, Purchase Orders (PENDING_APPROVAL), and approval execution states (APPROVED).🗄️ Database Schema ArchitectureThe core application data layer is structured around four primary relational models:Plaintext ┌───────────────┐       1:N       ┌───────────────┐
 │    Vendor     │ ──────────────> │ PurchaseOrder │
 └───────────────┘                 └───────┬───────┘
                                           │ 1:N
                                           ▼
 ┌───────────────┐                 ┌───────────────┐
 │   Material    │ ──────────────> │    POItem     │
 └───────────────┘       1:N       └───────────────┘
Vendor: Manages supplier identifiers, company profiles, and metadata.Material: Tracks inventory stock items, unit descriptions, and pricing.PurchaseOrder (PO): Records high-level order metadata, calculated financial totals, and lifecycle tracking states (PENDING_APPROVAL, APPROVED).POItem: Detailed line-item mappings connecting individual purchase orders to specific materials and quantities.🏗️ System ArchitecturePlaintext                               ┌─────────────────────────┐
                               │       User / Peer       │
                               └────────────┬────────────┘
                                            │
                                            ▼
                               ┌─────────────────────────┐
                               │   Streamlit Web UI      │
                               │        (app.py)         │
                               └───────┬───────────┬─────┘
                                       │           │
                          Chat Queries │           │ PO Creation Forms
                                       ▼           ▼
                       ┌───────────────────┐   ┌───────────────────┐
                       │  LangChain Agent  │   │  FastAPI Backend  │
                       │   (ai_agent.py)   │   │     (main.py)     │
                       └─────────┬─────────┘   └─────────┬─────────┘
                                 │                       │
                                 └───────────┬───────────┘
                                             │
                                             ▼
                               ┌─────────────────────────┐
                               │   SQLAlchemy & Schema   │
                               │    (database/models)    │
                               └─────────────┬───────────┘
                                             │
                                             ▼
                               ┌─────────────────────────┤
                               │    SAP HANA Database    │
                               └─────────────────────────┘
🛠️ Technology StackCore Engine & FrameworksTechnologyPurpose🐍 Python 3.11+Core runtime environment🚀 FastAPIHigh-performance asynchronous REST API backend🌐 StreamlitInteractive Python web application framework for the UI🧠 LangChainReAct agent framework & LLM orchestration🤖 Google GeminiAdvanced conversational and reasoning intelligence model🗄️ SAP HANA / SQLAlchemyEnterprise relational data storage & ORM layer📂 Project StructurePlaintextSAP-Mini-ERP-P2P-Agent/
│
├── 📄 main.py               # FastAPI backend server & API endpoints
├── 📄 app.py                # Streamlit interactive frontend dashboard & chat UI
├── 📄 ai_agent.py           # LangChain ReAct agent logic & Gemini LLM integration
├── 📄 database.py           # SQLAlchemy database engine setup & session scopes
├── 📄 models.py             # Relational schema mappings (Vendor, Material, PO, POItem)
├── 📄 check_models.py       # Diagnostic script for validating model connectivity
├── 📄 requirements.txt      # Project Python package dependencies
└── 📄 .gitignore            # Git exclusion rules
🚀 Getting Started & InstallationPrerequisitesEnsure you have the following installed on your machine:Python 3.11 or higherGitA valid Google Gemini API key1️⃣ Clone the RepositoryBashgit clone https://github.com/Prateek-Singh000/SAP-Mini-ERP-P2P-Agent.git
cd SAP-Mini-ERP-P2P-Agent
2️⃣ Set Up a Virtual EnvironmentWindows (Git Bash)Bashpython -m venv venv
source venv/Scripts/activate
macOS / LinuxBashpython3 -m venv venv
source venv/bin/activate
3️⃣ Install DependenciesBashpip install -r requirements.txt
4️⃣ Configure Environment VariablesCreate a .env file in the root directory of your project and populate your connection credentials:Code snippetSAP_DATABASE_URL=hana+hdbcli://username:password@host:port
GOOGLE_API_KEY=your_gemini_api_key_here
🚀 Running the ApplicationBecause this project utilizes a decoupled client-server architecture, run the backend and the frontend in two separate terminal windows:Terminal 1: Start the FastAPI BackendBashuvicorn main:app --reload --port 8000
Terminal 2: Launch the Streamlit FrontendBashstreamlit run app.py
Open your browser and navigate to http://localhost:8501.💡 Usage GuideTransactional Entry: Use the Streamlit sidebar form to choose a Vendor ID, Material ID, and desired quantity, then click Generate PO to commit a live transaction to SAP HANA.Conversational AI Auditing: Use the primary chat interface to interrogate your supply chain database in plain English:"What is the status, total amount, and vendor name for Purchase Order ID 1?""How many vendors do we currently manage in the SAP HANA procurement database?"

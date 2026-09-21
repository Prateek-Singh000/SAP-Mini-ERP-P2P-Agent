<h1>🚀 SAP Mini-ERP P2P (Procure-to-Pay) AI Assistant</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Enterprise-SAP%20HANA-0FA958?style=for-the-badge&logo=sap&logoColor=white" alt="SAP HANA">
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/AI-LangChain%20%2F%20Gemini-336791?style=for-the-badge&logo=google&logoColor=white" alt="LangChain">
  <img src="https://img.shields.io/badge/Database-SQLAlchemy-CC292B?style=for-the-badge&logo=python&logoColor=white" alt="SQLAlchemy">
</p>

<p align="center">
  <b>An enterprise-grade, full-stack Procure-to-Pay (P2P) Mini-ERP system powered by an autonomous ReAct AI agent that translates natural language into live SAP HANA database operations.</b>
</p>

<p align="center">
  <i>Bridging traditional enterprise resource planning with generative AI intelligence.</i>
</p>

<hr>

<h2>🌱 About SAP Mini-ERP P2P AI</h2>

<p><b>SAP Mini-ERP P2P AI Assistant</b> is a comprehensive, production-ready procurement management platform built to bridge the gap between heavy enterprise database workflows and intelligent automation.</p>

<p>Instead of requiring complex enterprise GUI navigation or deep SQL expertise, this platform gives stakeholders two unified ways to interact with supply chain data:</p>
<ol>
  <li><b>Traditional UI Form Layer:</b> A real-time Streamlit dashboard to create, track, and manage purchase orders.</li>
  <li><b>Autonomous AI Assistant Layer:</b> A conversational ReAct agent powered by Google Gemini and LangChain that parses natural language questions to query, inspect, and audit your live SAP HANA database securely.</li>
</ol>

<pre><code>       💬 User Prompt / Sidebar Form
                  ↓
       🌐 Streamlit Frontend UI
                  ↓
       🚀 FastAPI Backend REST Layer
                  ↓
       🧠 LangChain ReAct AI Agent ──→ 🤖 Google Gemini LLM
                  ↓
       🗄️ SQLAlchemy Core Engine
                  ↓
       🏢 SAP HANA Cloud Database</code></pre>

<hr>

<h1>✨ Key Features</h1>

<h3>🏢 Enterprise SAP HANA Backend</h3>
<p>Connected natively to an SAP HANA database using SQLAlchemy and the <code>sqlalchemy-hana</code> dialect for robust relational procurement management.</p>

<h3>⚡ Asynchronous FastAPI REST Layer</h3>
<p>Clean, modular backend architecture handling REST routing, data serialization, transaction commits, and approval state transitions.</p>

<h3>🤖 Autonomous LangChain ReAct AI Agent</h3>
<p>Leverages advanced LLM agents to dynamically translate unstructured user queries (e.g., <i>"What is the status and total amount for PO ID 1?"</i>) into precise SQL executions.</p>

<h3>📊 Interactive Streamlit Frontend</h3>
<p>Provides both a dynamic transactional sidebar form for quick purchase order generation and a sleek, responsive conversational dashboard.</p>

<h3>🔄 End-to-End Procurement Lifecycle</h3>
<p>Manages the full supplier-to-settlement pipeline—tracking Vendors, Raw Materials, Purchase Orders (<code>PENDING_APPROVAL</code>), and approval execution states (<code>APPROVED</code>).</p>

<hr>

<h1>🗄️ Database Schema Architecture</h1>

<p>The core application data layer is structured around four primary relational models:</p>

<pre><code> ┌───────────────┐       1:N       ┌───────────────┐
 │    Vendor     │ ──────────────> │ PurchaseOrder │
 └───────────────┘                 └───────┬───────┘
                                           │ 1:N
                                           ▼
 ┌───────────────┐                 ┌───────────────┐
 │   Material    │ ──────────────> │    POItem     │
 └───────────────┘       1:N       └───────────────┘</code></pre>

<ul>
  <li><b>Vendor:</b> Manages supplier identifiers, company profiles, and metadata.</li>
  <li><b>Material:</b> Tracks inventory stock items, unit descriptions, and pricing.</li>
  <li><b>PurchaseOrder (PO):</b> Records high-level order metadata, calculated financial totals, and lifecycle tracking states (<code>PENDING_APPROVAL</code>, <code>APPROVED</code>).</li>
  <li><b>POItem:</b> Detailed line-item mappings connecting individual purchase orders to specific materials and quantities.</li>
</ul>

<hr>

<h1>🏗️ System Architecture</h1>

<pre><code>                               ┌─────────────────────────┐
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
                               ┌─────────────────────────┐
                               │    SAP HANA Database    │
                               └─────────────────────────┘</code></pre>

<hr>

<h1>🛠️ Technology Stack</h1>

<h2>Core Engine & Frameworks</h2>
<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th>Technology</th>
      <th>Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>🐍 <b>Python 3.11+</b></td>
      <td>Core runtime environment</td>
    </tr>
    <tr>
      <td>🚀 <b>FastAPI</b></td>
      <td>High-performance asynchronous REST API backend</td>
    </tr>
    <tr>
      <td>🌐 <b>Streamlit</b></td>
      <td>Interactive Python web application framework for the UI</td>
    </tr>
    <tr>
      <td>🧠 <b>LangChain</b></td>
      <td>ReAct agent framework & LLM orchestration</td>
    </tr>
    <tr>
      <td>🤖 <b>Google Gemini</b></td>
      <td>Advanced conversational and reasoning intelligence model</td>
    </tr>
    <tr>
      <td>🗄️ <b>SAP HANA / SQLAlchemy</b></td>
      <td>Enterprise relational data storage & ORM layer</td>
    </tr>
  </tbody>
</table>

<hr>

<h1>📂 Project Structure</h1>

<pre><code>SAP-Mini-ERP-P2P-Agent/
│
├── 📄 main.py               # FastAPI backend server & API endpoints
├── 📄 app.py                # Streamlit interactive frontend dashboard & chat UI
├── 📄 ai_agent.py           # LangChain ReAct agent logic & Gemini LLM integration
├── 📄 database.py           # SQLAlchemy database engine setup & session scopes
├── 📄 models.py             # Relational schema mappings (Vendor, Material, PO, POItem)
├── 📄 check_models.py       # Diagnostic script for validating model connectivity
├── 📄 requirements.txt      # Project Python package dependencies
└── 📄 .gitignore            # Git exclusion rules</code></pre>

<hr>

<h1>🚀 Getting Started & Installation</h1>

<h2>Prerequisites</h2>
<p>Ensure you have the following installed on your machine:</p>
<ul>
  <li>Python 3.11 or higher</li>
  <li>Git</li>
  <li>A valid Google Gemini API key</li>
</ul>

<hr>

<h2>1️⃣ Clone the Repository</h2>
<pre><code>git clone https://github.com/Prateek-Singh000/SAP-Mini-ERP-P2P-Agent.git
cd SAP-Mini-ERP-P2P-Agent</code></pre>

<hr>

<h2>2️⃣ Set Up a Virtual Environment</h2>

<h3>Windows (Git Bash)</h3>
<pre><code>python -m venv venv
source venv/Scripts/activate</code></pre>

<h3>macOS / Linux</h3>
<pre><code>python3 -m venv venv
source venv/bin/activate</code></pre>

<hr>

<h2>3️⃣ Install Dependencies</h2>
<pre><code>pip install -r requirements.txt</code></pre>

<hr>

<h2>4️⃣ Configure Environment Variables</h2>
<p>Create a <code>.env</code> file in the root directory of your project and populate your connection credentials:</p>
<pre><code>SAP_DATABASE_URL=hana+hdbcli://username:password@host:port
GOOGLE_API_KEY=your_gemini_api_key_here</code></pre>

<hr>

<h1>🚀 Running the Application</h1>
<p>Because this project utilizes a decoupled client-server architecture, run the backend and the frontend in <b>two separate terminal windows</b>:</p>

<h3>Terminal 1: Start the FastAPI Backend</h3>
<pre><code>uvicorn main:app --reload --port 8000</code></pre>

<h3>Terminal 2: Launch the Streamlit Frontend</h3>
<pre><code>streamlit run app.py</code></pre>
<p><i>Open your browser and navigate to <code>http://localhost:8501</code>.</i></p>

<hr>

<h1>💡 Usage Guide</h1>
<ol>
  <li><b>Transactional Entry:</b> Use the Streamlit sidebar form to choose a Vendor ID, Material ID, and desired quantity, then click <b>Generate PO</b> to commit a live transaction to SAP HANA.</li>
  <li><b>Conversational AI Auditing:</b> Use the primary chat interface to interrogate your supply chain database in plain English:
    <ul>
      <li><i>"What is the status, total amount, and vendor name for Purchase Order ID 1?"</i></li>
      <li><i>"How many vendors do we currently manage in the SAP HANA procurement database?"</i></li>
    </ul>
  </li>
</ol>

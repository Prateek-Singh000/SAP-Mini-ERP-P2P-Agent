\# 🚀 SAP Mini-ERP P2P (Procure-to-Pay) AI Assistant



A full-stack, enterprise-grade Mini-ERP procurement system featuring an \*\*SAP HANA\*\* database backend, an asynchronous \*\*FastAPI\*\* REST API layer, an interactive \*\*Streamlit\*\* web UI, and an autonomous \*\*LangChain ReAct AI Agent\*\* powered by Google Gemini.



This project bridges traditional enterprise resource planning with generative AI, allowing users to execute backend procurement transactions via a graphical dashboard or query live database records dynamically using natural language.



\---



\## 🏗️ Architecture \& Tech Stack



\* \*\*Database Layer:\*\* SAP HANA Cloud managed via SQLAlchemy and the `sqlalchemy-hana` dialect.

\* \*\*Backend API:\*\* FastAPI asynchronously handling REST endpoints for master data retrieval, Purchase Order (PO) creation, and approval workflows.

\* \*\*Frontend UI:\*\* Streamlit providing an intuitive sidebar form for transactional entry and a real-time conversational chatbot interface.

\* \*\*AI \& Agentic Layer:\*\* LangChain ReAct framework utilizing Google Gemini models to dynamically translate natural language prompts into secure, executable SQL queries against the enterprise schema.



\---



\## 🗄️ Database Schema



The core procurement model consists of four primary relational entities:

1\. \*\*Vendor:\*\* Manages supplier details, contact info, and business metadata.

2\. \*\*Material:\*\* Tracks inventory items, unit descriptions, and pricing.

3\. \*\*PurchaseOrder (PO):\*\* Records high-level order metadata, total calculated amounts, and workflow status (`PENDING\_APPROVAL`, `APPROVED`).

4\. \*\*POItem:\*\* Line-item mapping connecting purchase orders to specific materials and ordered quantities.



\---



\## 📂 Project Structure



```text

SAP-Mini-ERP-P2P-Agent/

│

├── main.py              # FastAPI backend server \& API routes

├── app.py               # Streamlit frontend web interface \& chat dashboard

├── ai\_agent.py          # LangChain ReAct agent logic \& Gemini integration

├── database.py          # SQLAlchemy engine setup \& SAP HANA session management

├── models.py            # SQLAlchemy database models (Vendor, Material, PO, etc.)

├── requirements.txt     # Python package dependencies

└── .env.example         # Template for environment variables



⚙️ Getting Started \& Installation

1\. Clone the Repository

git clone \[https://github.com/Prateek-Singh000/SAP-Mini-ERP-P2P-Agent.git](https://github.com/Prateek-Singh000/SAP-Mini-ERP-P2P-Agent.git)

cd SAP-Mini-ERP-P2P-Agent



2\. Set Up a Virtual Environment

python -m venv venv

source venv/Scripts/activate  # On Windows Git Bash



3\. Install Dependencies

pip install -r requirements.txt



4\. Configure Environment Variables

Create a .env file in the root directory using your credentials:

SAP\_DATABASE\_URL=hana+hdbcli://username:password@host:port

GOOGLE\_API\_KEY=your\_gemini\_api\_key\_here



🚀 Running the Application

Because this is a decoupled full-stack architecture, run the backend and frontend in two separate terminal windows:



Terminal 1: Start the FastAPI Backend

uvicorn main:app --reload --port 8000



Terminal 2: Launch the Streamlit Frontend

streamlit run app.py

Open your browser and navigate to http://localhost:8501.



💡 Usage Guide

Generate Transactions: Use the interactive sidebar form in Streamlit to select a Vendor ID, Material ID, and Quantity, then click Generate PO to commit a live order to SAP HANA.



AI-Driven Data Retrieval: Use the main chat interface to ask questions about your live enterprise data in plain English, such as:



"What is the status, total amount, and vendor name for Purchase Order ID 1?"



"How many active vendors do we currently manage in the database?"


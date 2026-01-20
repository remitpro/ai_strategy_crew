# AI Strategy Architect

An **enterprise-grade** application that leverages a crew of **6 autonomous AI agents** to transform digital strategy documents into comprehensive, board-ready AI adoption roadmaps. Built with **CrewAI**, **FastAPI**, and a premium **React** frontend.

![Project Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-blue)
![Version](https://img.shields.io/badge/version-2.0-blue)

## 🚀 Overview

AI Strategy Architect automates the sophisticated process of enterprise strategic planning. By uploading your existing digital strategy documents (PDF, TXT, MD), an orchestrated team of **6 specialized AI agents** working through **10 comprehensive tasks** analyzes your goals, identifies high-impact AI opportunities, and produces a **50-70 page enterprise-grade strategy document** that rivals top-tier consulting firms (McKinsey, BCG, Bain).

### Key Capabilities

✨ **Strategic Analysis**: Deep analysis of digital strategies with gap identification and stakeholder mapping  
🎯 **AI Opportunity Discovery**: 10-15 detailed use cases across all business functions with ROI projections  
🏗 **Infrastructure Planning**: Complete technical architecture with cloud platform recommendations and TCO analysis  
💰 **Financial Modeling**: 5-year financial projections with NPV, IRR, and scenario analysis  
⚖️ **Risk & Compliance**: Comprehensive risk assessment with governance frameworks (GDPR, AI Act, SOC2)  
👥 **Change Management**: Organizational readiness assessment with training programs and adoption strategies  
📊 **Executive Reporting**: Board-ready deliverables with executive summaries and implementation roadmaps  

### What's New in Version 2.0

🆕 **6 Specialized Agents** (up from 3):
- Senior Digital Transformation Strategist
- Chief AI Strategy Officer
- Enterprise AI Infrastructure Architect & CDO
- AI Investment & ROI Analyst
- AI Ethics, Risk & Compliance Officer
- Organizational Change & Adoption Strategist

🆕 **10 Comprehensive Tasks** (up from 4):
- Strategic Analysis & Competitive Intelligence
- AI Use Case Identification & Prioritization
- Technical Architecture Design
- Financial Modeling & Business Case Development
- Risk Assessment & Governance Framework
- Change Management Planning
- Implementation Roadmap Creation
- Executive Summary Generation
- Final Strategy Document Compilation

🆕 **Enterprise-Grade Output**: 50-70 page comprehensive strategy documents (up from 5-10 pages)

## 🏗 Architecture

The project consists of two main components:

1.  **Backend (Python/FastAPI)**:
    *   **CrewAI**: Orchestrates the multi-agent system with 6 specialized agents
    *   **FastAPI**: Exposes the agent crew via a RESTful API
    *   **PDFPlumber**: Handles document parsing and text extraction
    *   **Python-docx**: Generates professional Word documents

2.  **Frontend (React/Vite)**:
    *   **Interactive UI**: "Glassmorphism" design with real-time animations
    *   **File Handling**: Drag-and-drop support for strategy documents
    *   **Markdown Rendering**: Rich display of the generated strategy
    *   **Export Functionality**: Download as professional Word documents

## 🛠 Prerequisites

*   **Python** 3.10+
*   **Node.js** 20+
*   **API Keys**:
    *   `OPENAI_API_KEY`: For the LLM (GPT-4o recommended)
    *   `SERPER_API_KEY`: For internet search capabilities (Serper.dev)
    *   Optional: `BROWSERLESS_API_KEY`, `EXA_API_KEY` for enhanced research

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ai_strategy_crew
```

### 2. Backend Setup
Navigate to the backend directory and set up the Python environment.

```bash
cd ai_strategy_crew

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .
pip install fastapi uvicorn python-multipart python-docx pdfplumber
```

**Configuration**:
Create a `.env` file in `ai_strategy_crew/ai_strategy_crew/.env` with your keys:

```ini
MODEL=gpt-4o
OPENAI_API_KEY=sk-...
SERPER_API_KEY=...
BROWSERLESS_API_KEY=...  # Optional
EXA_API_KEY=...  # Optional
```

### 3. Frontend Setup
Navigate to the frontend directory and install dependencies.

```bash
cd ../frontend
npm install
```

## 🏃‍♂️ Running the Application

You need to run both the backend and frontend terminals simultaneously.

### Terminal 1: Application Backend
```bash
cd ai_strategy_crew
source .venv/bin/activate
uvicorn ai_strategy_crew.api:app --reload --host 0.0.0.0 --port 8000
```

### Terminal 2: User Interface
```bash
cd frontend
npm run dev
```

Open your browser and navigate to: **[http://localhost:3000](http://localhost:3000)**

## 🎮 Usage

1.  **Upload**: Drag and drop your strategy document (PDF or Text) into the upload zone
2.  **Process**: Click "Generate AI Strategy" - the system will upload the file and kick off the AI crew
3.  **Wait**: The 6 agents will work through 10 comprehensive tasks (15-30 minutes depending on complexity)
4.  **Review**: The final 50-70 page strategic roadmap will be rendered on screen
5.  **Export**: Download as a professional Word document ready for board presentation

## 🤖 The AI Crew (6 Specialized Agents)

### Core Strategy Team

**1. Senior Digital Transformation Strategist**
- 15+ years advising Fortune 500 companies
- Conducts strategic analysis and gap identification
- Delivers executive-level insights aligned with business outcomes

**2. Chief AI Strategy Officer**
- Architected $100M+ AI transformation programs
- Designs comprehensive AI strategies and use cases
- Creates compelling narratives for C-suite buy-in

**3. Enterprise AI Infrastructure Architect & CDO**
- World-class expertise in cloud platforms and MLOps
- Designs scalable, secure AI infrastructure
- Provides detailed technical roadmaps with cost estimates

### Supporting Specialists

**4. AI Investment & ROI Analyst**
- Evaluated $2B+ in technology investments
- Develops 5-year financial models with NPV/IRR
- Translates technical investments into financial outcomes

**5. AI Ethics, Risk & Compliance Officer**
- Expert in GDPR, AI Act, SOC2 compliance
- Assesses risks and develops governance frameworks
- Ensures responsible AI deployment

**6. Organizational Change & Adoption Strategist**
- Achieved 85%+ adoption rates across 40+ enterprises
- Designs comprehensive change management plans
- Addresses cultural barriers and skill gaps

## 📊 Deliverable Structure (50-70 Pages)

1. **Executive Summary** (2 pages) - Board-ready overview
2. **Strategic Context** (3-4 pages) - Digital strategy analysis and competitive landscape
3. **AI Use Case Portfolio** (6-8 pages) - 10-15 detailed use cases with prioritization
4. **Technical Architecture & Infrastructure** (8-10 pages) - Complete technical blueprint
5. **Financial Analysis & Business Case** (6-8 pages) - 5-year projections and ROI
6. **Risk, Governance & Compliance** (6-8 pages) - Comprehensive risk assessment
7. **Change Management & Adoption** (7-9 pages) - Organizational readiness plan
8. **Implementation Roadmap** (8-10 pages) - Phased execution plan
9. **Appendices** - Glossary, models, diagrams, references

## 📚 Documentation

For detailed information about the enhanced system, see:
- **[ENTERPRISE_STRATEGY_GUIDE.md](./ENTERPRISE_STRATEGY_GUIDE.md)** - Comprehensive guide to agents, tasks, and workflows

## 🎯 Use Cases

- **C-Suite Executives**: Board-ready AI strategy presentations
- **Strategy Consultants**: Accelerate client deliverable creation
- **Digital Transformation Teams**: Comprehensive implementation roadmaps
- **Innovation Officers**: Identify and prioritize AI opportunities
- **IT Leadership**: Technical architecture and infrastructure planning
- **Finance Teams**: Business case development and ROI analysis

## 🔒 Enterprise Features

✅ **Consulting-Grade Quality**: Matches McKinsey/BCG/Bain standards  
✅ **Multi-Stakeholder Coverage**: CEO, CFO, CTO, CHRO, Legal, Business Units  
✅ **Data-Driven**: Specific metrics, benchmarks, and industry research  
✅ **Actionable**: Clear recommendations with implementation guidance  
✅ **Comprehensive**: Addresses strategy, technology, finance, risk, and change  
✅ **Professional**: Executive-level writing with consistent formatting  

## 📄 License

This project is licensed under the MIT License.

---

**Version**: 2.0  
**Status**: Production Ready  
**Last Updated**: January 2026


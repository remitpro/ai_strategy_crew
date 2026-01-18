# AI Strategy Architect

An enterprise-grade application that leverages a crew of autonomous AI agents to transform digital strategy documents into comprehensive AI adoption roadmaps. Built with **CrewAI**, **FastAPI**, and a premium **React** frontend.

![Project Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-blue)

## 🚀 Overview

AI Strategy Architect automates the sophisticated process of strategic planning. By uploading your existing digital strategy documents (PDF, TXT, MD), an orchestrated team of AI agents analyzes your goals, identifies high-impact AI opportunities, and designs a robust technical infrastructure plan.

### Key Capabilities
*   **Strategic Analysis**: Deconstructs corporate digital strategies to find alignment with AI.
*   **Opportunity Discovery**: Identifies specific AI use cases across business domains (HR, Ops, Marketing, etc.).
*   **Infrastructure Planning**: Recommends the necessary data architecture and MLOps tech stack.
*   **Executive Reporting**: Synthesizes all findings into a cohesive, presentation-ready strategy document.

## 🏗 Architecture

The project consists of two main components:

1.  **Backend (Python/FastAPI)**:
    *   **CrewAI**: Orchestrates the multi-agent system (AI Strategist, Data Architect, Transformation Analyst).
    *   **FastAPI**: Exposes the agent crew via a RESTful API.
    *   **PDFPlumber**: Handles document parsing and text extraction.

2.  **Frontend (React/Vite)**:
    *   **Interactive UI**: "Glassmorphism" design with real-time animations.
    *   **File Handling**: Drag-and-drop support for strategy documents.
    *   **Markdown Rendering**: Rich display of the generated strategy.

## 🛠 Prerequisites

*   **Python** 3.10+
*   **Node.js** 20+
*   **API Keys**:
    *   `OPENAI_API_KEY`: For the LLM (GPT-4o recommended).
    *   `SERPER_API_KEY`: For internet search capabilities (Serper.dev).

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
pip install fastapi uvicorn python-multipart
```

**Configuration**:
Create a `.env` file in `ai_strategy_crew/ai_strategy_crew/.env` with your keys:

```ini
MODEL=gpt-4o
OPENAI_API_KEY=sk-...
SERPER_API_KEY=...
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

1.  **Upload**: Drag and drop your strategy document (PDF or Text) into the upload zone.
2.  **Process**: Click "Generate AI Strategy". The system will upload the file and kick off the AI crew.
3.  **Wait**: The agents will research and deliberate (this may take 1-3 minutes depending on complexity).
4.  **Review**: The final strategic roadmap will be rendered on the screen.

## 🤖 The AI Crew

*   **Business Transformation Analyst**: Analyzes the "As-Is" state and strategic goals.
*   **AI Strategist**: Ideates "To-Be" AI use cases and business value.
*   **Data Infrastructure Expert**: Architects the technical foundation required for execution.

## 📄 License
This project is licensed under the MIT License.

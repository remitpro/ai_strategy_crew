# AI Strategy Crew 🤖

This CrewAI project generates a **comprehensive AI strategy** from a company's **digital strategy**.

## 🧭 How it works
The crew uses three agents:
1. Business Transformation Analyst – analyzes the digital strategy.
2. AI Strategist – identifies AI opportunities and composes the final AI strategy.
3. Data & Infrastructure Expert – defines the data and infrastructure plan.

All agents use the `SerperDevTool` to research AI trends and implementation best practices.

## 🚀 Usage
1. Install dependencies:
   ```bash
   pip install crewai crewai-tools

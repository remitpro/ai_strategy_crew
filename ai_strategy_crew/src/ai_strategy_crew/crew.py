from crewai import Crew, Process
from crewai_tools import SerperDevTool
from .config import agents, tasks

# Instantiate the SerperDevTool
serper_tool = SerperDevTool()

# Bind tools to all agents
agents.business_transformation_analyst.tools = [serper_tool]
agents.ai_strategist.tools = [serper_tool]
agents.data_infrastructure_expert.tools = [serper_tool]
agents.financial_analyst.tools = [serper_tool]
agents.change_management_specialist.tools = [serper_tool]
agents.risk_compliance_officer.tools = [serper_tool]

# Define the Crew with all agents and tasks in sequential order
crew = Crew(
    agents=[
        agents.business_transformation_analyst,
        agents.ai_strategist,
        agents.data_infrastructure_expert,
        agents.financial_analyst,
        agents.risk_compliance_officer,
        agents.change_management_specialist
    ],
    tasks=[
        # Phase 1: Analysis and Discovery
        tasks.analyze_digital_strategy_task,
        tasks.conduct_competitive_analysis_task,
        
        # Phase 2: Solution Design
        tasks.identify_ai_use_cases_task,
        tasks.design_technical_architecture_task,
        
        # Phase 3: Business Case and Risk Assessment
        tasks.develop_financial_model_task,
        tasks.assess_risks_and_compliance_task,
        
        # Phase 4: Implementation Planning
        tasks.design_change_management_plan_task,
        tasks.create_implementation_roadmap_task,
        
        # Phase 5: Final Deliverable
        tasks.create_executive_summary_task,
        tasks.compile_final_strategy_document_task
    ],
    process=Process.sequential,
    verbose=True
)


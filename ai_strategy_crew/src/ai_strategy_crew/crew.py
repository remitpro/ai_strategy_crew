from crewai import Crew, Process
from crewai_tools import SerperDevTool
from .config import agents, tasks

# Instantiate the SerperDevTool
serper_tool = SerperDevTool()

# Bind tools to agents
agents.ai_strategist.tools = [serper_tool]
agents.data_infrastructure_expert.tools = [serper_tool]
agents.business_transformation_analyst.tools = [serper_tool]

# Define the Crew
crew = Crew(
    agents=[
        agents.business_transformation_analyst,
        agents.ai_strategist,
        agents.data_infrastructure_expert
    ],
    tasks=[
        tasks.analyze_digital_strategy_task,
        tasks.design_ai_opportunities_task,
        tasks.define_infrastructure_plan_task,
        tasks.compose_final_ai_strategy_task
    ],
    process=Process.sequential
)

import os
import yaml
from crewai import Agent, Task

def load_yaml(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

current_dir = os.path.dirname(__file__)
agents_data = load_yaml(os.path.join(current_dir, 'agents.yaml'))
tasks_data = load_yaml(os.path.join(current_dir, 'tasks.yaml'))

class AgentsConfig:
    def __init__(self):
        self.ai_strategist = Agent(
            role=agents_data['ai_strategist']['role'],
            goal=agents_data['ai_strategist']['goal'],
            backstory=agents_data['ai_strategist']['backstory'],
            verbose=True,
            allow_delegation=False
        )
        self.data_infrastructure_expert = Agent(
            role=agents_data['data_infrastructure_expert']['role'],
            goal=agents_data['data_infrastructure_expert']['goal'],
            backstory=agents_data['data_infrastructure_expert']['backstory'],
            verbose=True,
            allow_delegation=False
        )
        self.business_transformation_analyst = Agent(
            role=agents_data['business_transformation_analyst']['role'],
            goal=agents_data['business_transformation_analyst']['goal'],
            backstory=agents_data['business_transformation_analyst']['backstory'],
            verbose=True,
            allow_delegation=False
        )

agents = AgentsConfig()

class TasksConfig:
    def __init__(self):
        self.analyze_digital_strategy_task = Task(
            description=tasks_data['analyze_digital_strategy_task']['description'],
            expected_output=tasks_data['analyze_digital_strategy_task']['expected_output'],
            agent=agents.business_transformation_analyst
        )
        self.design_ai_opportunities_task = Task(
            description=tasks_data['design_ai_opportunities_task']['description'],
            expected_output=tasks_data['design_ai_opportunities_task']['expected_output'],
            agent=agents.ai_strategist
        )
        self.define_infrastructure_plan_task = Task(
            description=tasks_data['define_infrastructure_plan_task']['description'],
            expected_output=tasks_data['define_infrastructure_plan_task']['expected_output'],
            agent=agents.data_infrastructure_expert
        )
        self.compose_final_ai_strategy_task = Task(
            description=tasks_data['compose_final_ai_strategy_task']['description'],
            expected_output=tasks_data['compose_final_ai_strategy_task']['expected_output'],
            agent=agents.ai_strategist
        )

tasks = TasksConfig()

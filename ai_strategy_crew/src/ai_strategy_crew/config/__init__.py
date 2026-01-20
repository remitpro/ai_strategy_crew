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
        # Core Strategy Agents
        self.business_transformation_analyst = Agent(
            role=agents_data['business_transformation_analyst']['role'],
            goal=agents_data['business_transformation_analyst']['goal'],
            backstory=agents_data['business_transformation_analyst']['backstory'],
            verbose=True,
            allow_delegation=False
        )
        
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
        
        # Supporting Specialist Agents
        self.financial_analyst = Agent(
            role=agents_data['financial_analyst']['role'],
            goal=agents_data['financial_analyst']['goal'],
            backstory=agents_data['financial_analyst']['backstory'],
            verbose=True,
            allow_delegation=False
        )
        
        self.change_management_specialist = Agent(
            role=agents_data['change_management_specialist']['role'],
            goal=agents_data['change_management_specialist']['goal'],
            backstory=agents_data['change_management_specialist']['backstory'],
            verbose=True,
            allow_delegation=False
        )
        
        self.risk_compliance_officer = Agent(
            role=agents_data['risk_compliance_officer']['role'],
            goal=agents_data['risk_compliance_officer']['goal'],
            backstory=agents_data['risk_compliance_officer']['backstory'],
            verbose=True,
            allow_delegation=False
        )

agents = AgentsConfig()

class TasksConfig:
    def __init__(self):
        # Phase 1: Analysis and Discovery
        self.analyze_digital_strategy_task = Task(
            description=tasks_data['analyze_digital_strategy_task']['description'],
            expected_output=tasks_data['analyze_digital_strategy_task']['expected_output'],
            agent=agents.business_transformation_analyst
        )
        
        self.conduct_competitive_analysis_task = Task(
            description=tasks_data['conduct_competitive_analysis_task']['description'],
            expected_output=tasks_data['conduct_competitive_analysis_task']['expected_output'],
            agent=agents.ai_strategist
        )
        
        # Phase 2: Solution Design
        self.identify_ai_use_cases_task = Task(
            description=tasks_data['identify_ai_use_cases_task']['description'],
            expected_output=tasks_data['identify_ai_use_cases_task']['expected_output'],
            agent=agents.ai_strategist
        )
        
        self.design_technical_architecture_task = Task(
            description=tasks_data['design_technical_architecture_task']['description'],
            expected_output=tasks_data['design_technical_architecture_task']['expected_output'],
            agent=agents.data_infrastructure_expert
        )
        
        # Phase 3: Business Case and Risk Assessment
        self.develop_financial_model_task = Task(
            description=tasks_data['develop_financial_model_task']['description'],
            expected_output=tasks_data['develop_financial_model_task']['expected_output'],
            agent=agents.financial_analyst
        )
        
        self.assess_risks_and_compliance_task = Task(
            description=tasks_data['assess_risks_and_compliance_task']['description'],
            expected_output=tasks_data['assess_risks_and_compliance_task']['expected_output'],
            agent=agents.risk_compliance_officer
        )
        
        # Phase 4: Implementation Planning
        self.design_change_management_plan_task = Task(
            description=tasks_data['design_change_management_plan_task']['description'],
            expected_output=tasks_data['design_change_management_plan_task']['expected_output'],
            agent=agents.change_management_specialist
        )
        
        self.create_implementation_roadmap_task = Task(
            description=tasks_data['create_implementation_roadmap_task']['description'],
            expected_output=tasks_data['create_implementation_roadmap_task']['expected_output'],
            agent=agents.ai_strategist
        )
        
        # Phase 5: Final Deliverable
        self.create_executive_summary_task = Task(
            description=tasks_data['create_executive_summary_task']['description'],
            expected_output=tasks_data['create_executive_summary_task']['expected_output'],
            agent=agents.ai_strategist
        )
        
        self.compile_final_strategy_document_task = Task(
            description=tasks_data['compile_final_strategy_document_task']['description'],
            expected_output=tasks_data['compile_final_strategy_document_task']['expected_output'],
            agent=agents.ai_strategist
        )

tasks = TasksConfig()

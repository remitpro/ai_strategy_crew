import os
from crewai import Crew
from .crew import crew

def main():
    print("=== AI Strategy Crew ===")
    print("Provide the company’s digital strategy text below:\n")
    digital_strategy = input("Paste digital strategy here:\n")

    # Run the crew
    print("\nRunning CrewAI agents...\n")
    result = crew.kickoff(inputs={'digital_strategy': digital_strategy})

    print("\n=== Final AI Strategy Output ===\n")
    print(result)

if __name__ == "__main__":
    os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY", "your-serper-key")
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "your-openai-key")
    main()

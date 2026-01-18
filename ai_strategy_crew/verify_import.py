from dotenv import load_dotenv
load_dotenv() 

try:
    from ai_strategy_crew.crew import crew
    print("SUCCESS: crew imported successfully")
except ImportError as e:
    print(f"FAILURE: {e}")
except Exception as e:
    print(f"FAILURE: {e}")

from sql_agent import run_agent

if __name__ == "__main__":
    while True:
        nlq = input("\nEnter your question (or type 'exit'): ")
        if nlq.lower() in ["exit", "quit"]:
            break
        try:
            result = run_agent(nlq)
            print("\nResult:\n", result)
        except Exception as e:
            print("Error:", e)
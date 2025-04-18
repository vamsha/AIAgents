# Natural Language to SQL Generator agent

## Components overview
    1. Frontend : Streamlit
    2. NLQ to SQL converter ( AI Agent ): 
            Experiement with some lite models ( gemini/gemini-2.0-flash-lite )
    3. SQL validator : Prevents SQl injection or malformed queries.
    4. MySQL Executor: Run teh SQL query and get the results ( used mysql.connector ).
    5. Logging / Monitoring: Log query and response with result for debugging.
    6. Evalution: Evaluate the result 
            Result Accuracy - check the sql executed result.
            Logical SQL comparision - **Not a good idea** because query can be written in multiple ways.
            LLM/ Human feedback - Try to implement the feedback loop like chatGPT has thumbsup/down symbols.

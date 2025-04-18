from smolagents import CodeAgent, tool, LiteLLMModel, memory
from model_schema import schema_description
from config import config
from query_executor import execute_query


# Tool 1: Return schema
@tool
def get_schema() -> str:
    """Returns the database schema."""
    return schema_description


# Tool 2: Generate SQL from natural language
@tool
def generate_sql(query: str) -> str:
    """
    Generates SQL for a given natural language query based on the schema.
    Args:
        query (str): Natural language query to get sql query based on schema
    """
    # Prompt definition
    prompt = f""" 
                You are an expert SQL agent that interprets user questions and generates MySQL queries using this schema:{schema_description}
                Important Rules:
                    - Only generate **read-only** SQL queries (e.g., SELECT statements).
                    - Do **not** use INSERT, UPDATE, DELETE, DROP, TRUNCATE, or any other write or schema-altering operations.
                    - If the question implies modifying the database, respond with a SELECT-only alternative or mention that only read operations are allowed.
                    - Always return only the SQL query. Do not explain anything else.
                
                Rephrases the answer in a complete sentence using the context of the original question.
                Question: {query}

            SQL:
            """

    # Flash Lite model
    model = LiteLLMModel(
        model_id="gemini/gemini-2.0-flash-lite", api_key=config["GOOGLE_API_KEY"]
    )
    llm = model
    op = llm(prompt)
    print("i am printing the prompt message ", op)
    return op


def is_safe_sql(sql_query: str) -> bool:
    """
    Validates that the SQL query does not contain dangerous keywords.
    """
    forbidden_keywords = ["insert", "drop", "delete", "truncate", "update"]
    sql_lower = sql_query.lower()
    return not any(keyword in sql_lower for keyword in forbidden_keywords)


@tool
def sql_execute(query: str) -> str:
    """
    Execute the sql qiery which got generated.
    Args:
        query (str): SQL query to execute
    """
    if is_safe_sql(query):
        print("Safe SQL:", query)
        return execute_query(query)
    else:
        raise ValueError(
            "Only read-only queries are allowed. No INSERT, DELETE, or DROP."
        )


# @tool
# def explain_answer(input: str, response: str) -> str:
#     """
#     Rephrases the answer in a complete sentence using the context of the original question.

#     Input should be a string formatted like:
#     Args:
#         input: natural language question which user asks
#         response: extracted data after processing
#     """

#     prompt = (
#         "You are a helpful assistant that turns short answers into natural language explanations.\n"
#         "Rephrase the following in a full sentence:\n"
#         f"Question: {input}\nAnswer: {response}"
#     )
#     # Flash Lite model
#     model = LiteLLMModel(
#         model_id="gemini/gemini-2.0-flash-lite", api_key=config["GOOGLE_API_KEY"]
#     )
#     llm = model
#     op = llm(prompt)
#     return op


# Define tools
tools = [get_schema, generate_sql, sql_execute]  # , explain_answer]
model = LiteLLMModel(
    model_id="gemini/gemini-2.0-flash-lite", api_key=config["GOOGLE_API_KEY"]
)
# Create the agent
agent = CodeAgent(
    tools=tools,
    model=model,
    name="NL2SQL Agent",
)


# Run Agent
def run_agent(nlq: str):
    # return agent_executor.invoke({"input": nlq})
    print("*******************", agent.memory.system_prompt)
    response = agent.run(nlq)
    # input_text = f"Question: {nlq}\nAnswer: {response}"
    # explained = agent.run_tool("explain_answer", input_text)
    # Now enhance the answer with explanation:
    explanation_prompt = f"""Rephrase this answer in a full sentence that includes the question context.\n\nQuestion: {nlq}\nAnswer: {response} 
                        and always try to present the output in table format too"""
    explained_answer = agent.run(explanation_prompt)
    print("inside run agent +++++++++++++++++ ", explained_answer)
    return explained_answer


# Example natural language input
if __name__ == "__main__":
    user_query = "How many customers are from USA?"
    run_agent(user_query)

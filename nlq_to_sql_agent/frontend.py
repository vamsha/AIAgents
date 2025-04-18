import streamlit as st
from sql_agent import run_agent


# Streamlit UI
st.set_page_config(page_title="AI SQL Generator", layout="centered")
st.title("🧠 Natural Language to SQL Generator")

user_query = st.text_input("Enter your natural language query:")

if st.button("submit"):
    if user_query.strip() == "":
        st.warning("Please enter a query before generating.")
    try:
        result = run_agent(user_query)
        print("\nResult:\n", result)
        st.success(f"{result}")
    except Exception as e:
        print("Error:", e)

import streamlit as st
from sql_agent import run_agent

# Set page config
st.set_page_config(page_title="AI SQL Generator", layout="centered")
st.title("🧠 Natural Language to SQL Generator")

# Initialize session state
if 'thumbs_up' not in st.session_state:
    st.session_state.thumbs_up = 0
if 'thumbs_down' not in st.session_state:
    st.session_state.thumbs_down = 0
if 'result' not in st.session_state:
    st.session_state.result = None
if 'submitted_query' not in st.session_state:
    st.session_state.submitted_query = ""

# Input
user_query = st.text_area("Enter your natural language query:", value=st.session_state.submitted_query, height=150)

# Submit button
if st.button("Submit"):
    if user_query.strip() == "":
        st.warning("Please enter a query before generating.")
    else:
        try:
            st.session_state.submitted_query = user_query  # Save for persistence
            st.session_state.result = run_agent(user_query)
        except Exception as e:
            st.error("Something went wrong while generating SQL.")
            st.exception(e)

# Show result (even after interaction)
if st.session_state.result:
    st.success(st.session_state.result)

    # Feedback section
    st.subheader("Was this result helpful?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👍 Yes"):
            st.session_state.thumbs_up += 1
    with col2:
        if st.button("👎 No"):
            st.session_state.thumbs_down += 1

    st.caption(f"👍 Helpful: {st.session_state.thumbs_up}")
    st.caption(f"👎 Not Helpful: {st.session_state.thumbs_down}")

st.markdown("""
<hr style="border:1px solid #ccc" />

<p style='text-align: center; color: gray; font-size: 0.9em;'>
© 2025 vamshavardhan reddy kotha. All rights reserved.
</p>
""", unsafe_allow_html=True)
import streamlit as st
import requests

# App Configuration
st.set_page_config(page_title="LangGraph Agent UI", layout="centered")

# API endpoint
API_URL = "http://127.0.0.1:8000/chat"

# Models
MODEL_NAMES = [
    "Deepseek-r1-distill-llama-70b",
    "Llama3-70b-8192"
]

# UI Elements
st.title("LangGraph Chatbot Agent")
st.write("Interact with the LangGraph-based agent using this interface.")

# System prompt
given_system_prompt = st.text_area("Define you AI Agent:", height=100, placeholder="Type your system prompt here...")

# Selecting the model
selected_model = st.selectbox("Select Model:", MODEL_NAMES)

# User messages
user_input = st.text_area("Enter your message(s):", height=150, placeholder="Type your message here...")

# Query
if st.button("Submit"):
    if user_input.strip():
        try:
            # input to the FastAPI
            payload = {"messages": [user_input], "model_name": selected_model, 'system_prompt': given_system_prompt}
            response = requests.post(API_URL, json=payload)

            # Response
            if response.status_code == 200:
                response_data = response.json()
                if "error" in response_data:
                    st.error(response_data["error"])
                else:
                    ai_responses = [
                        message.get("content", "")
                        for message in response_data.get("messages", [])
                        if message.get("type") == "ai"
                    ]

                    if ai_responses:
                        st.subheader("Agent Response:")
                        st.markdown(f"{ai_responses[-1]}")
                    else:
                        st.warning("No AI response found in the agent output.")
            else:
                st.error(f"Request failed with status code {response.status_code}.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a message before clicking 'Send Query'.")
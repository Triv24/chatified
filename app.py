import streamlit as st
from os import getenv
from openai import OpenAI
from google import genai
from xai_sdk import Client

st.header("Welcome to Chatified!")
st.title("What can I do for you Today ?")

gemini_client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

model = st.selectbox("Choose your model", ["gemini-2.5-flash", "gpt-4o", "gpt-3", "grok-4"])
st.session_state["model"] = model

if "messages" not in st.session_state :
    st.session_state["messages"] = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Ask me Here"):
    st.session_state.messages.append({"role" : "user", "content" : prompt})
    
    with st.chat_message('user') :
        st.write(prompt)

    content = st.session_state.messages
    response = gemini_client.models.generate_content(
        model= "gemini-2.5-flash",
        contents= content
    )

    with st.chat_message("assistant"):
        st.markdown(response.text)

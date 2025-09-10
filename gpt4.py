import streamlit as st
from openai import OpenAI
from google import genai

st.sidebar.markdown("""
# Welcome to GPT-4 Model !
    You will need to submit an api-key for OpenAI API in order to proceed.
    
    Don't worry the apikey is just stored in the session state and is not used after the session ends.
""")

st.sidebar.markdown("""
Enter the API-Key here :
""")
api_key = st.sidebar.text_input("")
st.session_state.api = api_key

api_key = st.session_state.api

client = OpenAI(st.session_state.api)

if "history" not in st.session_state:
    st.session_state.history = []

if "img" not in st.session_state:
    st.session_state.img = None

st.title("✨ Hey!")
st.markdown("## Welcome to GPT-4 Model")
st.markdown("#### Want to Ask about an Image?")

file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if file is not None:
    st.session_state.img = file
    st.success("✅ Image uploaded successfully!")

if st.session_state.img is not None:
    st.image(st.session_state.img, caption="Your uploaded image")
    st.write("You can now ask Gemini about this image 🚀")
else:
    st.info("No image uploaded — you can still chat with Gemini using text or voice.")

if prompt := st.chat_input("Ask me Here...") :

    st.session_state.history.append({"role" : "user", "content" : prompt})

    st.write ("Generating...")

    cntnt = "".join(f"{x} : {y}" for chat in st.session_state.history for x,y in chat.items())
        
    if st.session_state.img is None:

        response = client.chat.completions()
    else :
        binary_image = st.session_state.img.read()

        response = client.chat.completions.create(
model="gpt-5",
messages=[
    {"role": "developer", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
]
)

    st.session_state.history.append({"role" : 'assistant', "content" : response.text})

    for chats in st.session_state.history :
        with st.chat_message(chats["role"]):
            st.write(chats["content"])


    

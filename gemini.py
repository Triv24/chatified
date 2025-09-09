import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

if "history" not in st.session_state:
    st.session_state.history = []

if "img" not in st.session_state:
    st.session_state.img = None

st.title("✨ Hey!")
st.markdown("## Welcome to Gemini's World")
st.markdown("#### Want to Ask ablout an Image?")

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

    cntnt = "".join(f"{x} : {y}" for chat in st.session_state.history for x,y in chat.items())
    
    if st.session_state.img is None:

        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents=cntnt
        )
    else :
        binary_image = st.session_state.img.read()

        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents=[
                genai.types.Part.from_bytes(
                    data=binary_image,
                    mime_type='image/jpeg',
                ), cntnt
            ]
        )

    st.session_state.history.append({"role" : 'assistant', "content" : response.text})

    for chats in st.session_state.history :
        with st.chat_message(chats["role"]):
            st.write(chats["content"])


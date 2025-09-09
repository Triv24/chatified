import streamlit as st

st.markdown("""
# ✨ Welcome to Chatified
---

### Your all-in-one multimodal AI chat assistant. Ask, explore, and create with the world’s top AI models — all in one place.
---
## 🚀 What You Can Do with Chatified

    💬 Chat with leading LLMs: Switch seamlessly between GPT, Gemini, Groq, and more.

    🖼️ Generate images: Turn descriptive prompts into AI-generated visuals.

    🎙️ Speak naturally: Use voice prompts to interact hands-free.

    📷 Upload images: Ask questions about your images and get instant insights.

    📚 Session history: Keep track of your conversations across sessions.\n\n          
                     
               
## 🎁 Bonus Features

    🔄 Switch models mid-conversation without losing context.

    🌍 Multilingual support to chat in your preferred language.

    🌓 Theme toggle: Switch between light & dark mode anytime.

---
## 🌟 Why Chatified?

> **Chatified brings the power of multimodal AI into a single intuitive interface, making it easier than ever to chat, create, and explore.**
---""")

st.sidebar.markdown("""
## ✨ Start Instant Chat :
---""")

st.sidebar.page_link("gemini.py", width="stretch", label="Instant Gemini Chat")

st.sidebar.page_link("gpt4.py", width="stretch", label="Instant GPT-4o Chat")

st.sidebar.page_link("groq.py", width="stretch", label="Instant Groq Chat")

st.sidebar.markdown("""
---""")

st.sidebar.markdown("""
## ✨ Generate Image :
---""")

st.sidebar.page_link("img_gen.py", width="stretch", label="Instant Gemini Chat")

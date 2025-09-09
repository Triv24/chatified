import streamlit as st

main_page = st.Page("main.py", title="Home Page", icon=":material/apps:")
gpt4 = st.Page("gpt4.py", title="GPT-4 Chat", icon=":material/api:")
gemini= st.Page("gemini.py", title="Gemini Chat", icon=":material/apps:")
groq = st.Page("groq.py", title="Groq Chat", icon=":material/apps:")

img_gen = st.Page("img_gen.py", title="Generate Image", icon=":material/apps:")

page = st.navigation([main_page, gpt4, gemini, groq, img_gen], position='top', expanded=True)

page.run()

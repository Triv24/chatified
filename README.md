# Chatified

`Chatified` is a multi-model chatbot website.

## **`Chatified` is a multi-modal chatbot app in Streamlit** that allows users to :

1. **Choose between at least 3 different AI models** (OpenAI, Gemini, Groq, etc.) for both text and image generation.
2. **Generate text answers** to typed prompts, with responses from the currently selected model.
3. **Generate images from descriptive prompts**, using the selected image-generation model.
4. **Upload an image and ask questions about it** (visual Q&A, e.g., “What’s in this picture?”).
5. **Speak to the chatbot**: Accept **voice prompts** as input (in addition to typing) and transcribe them for model response.
6. **Handle all exceptions gracefully**: Show friendly, clear error messages if anything goes wrong.
7. **Show visual loading indicators** whenever the app is working on a response (for text, image, upload, or speech).
8. **Use Streamlit as the frontend** for all interactions.
9. **Create an intuitive, visually pleasing UI** that mimics modern AI chat interfaces.
    
---

> **Bonus Features (Optional, for extra points)**:
> 
> - Maintain session chat history and allow switching models mid-conversation.
> - Support multi-language text and voice prompts.
> - Allow users to download the chat log and generated images.
> - Theme toggle (light/dark mode).

---

## Tech-stack used :
- **Frontend:** Streamlit *(for rapid prototyping and AI UIs)*
- **AI APIs:** Gemini, OpenAI, Groq
- **Extra:** Python speech-to-text library for voice input, error handling, and image Q&A

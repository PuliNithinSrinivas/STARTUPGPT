import google.generativeai as genai
import streamlit as st

# Set your Gemini API Key
genai.configure(api_key="AIzaSyAC2I3drvTKLeXIu0SILdNNG7D4EVm9Br8")  # replace with your real key

# Use Gemini 1.5 Flash (lightweight & free-tier friendly)
model_name = "models/gemini-1.5-flash-latest"
model = genai.GenerativeModel(model_name=model_name)

# Chat session with history support
def get_gemini_response(prompt):
    # Load previous history if exists
    chat = model.start_chat(history=st.session_state.get("chat_history", []))

    # Send user input to Gemini
    response = chat.send_message(prompt)

    # Save updated history back to session
    st.session_state.chat_history = chat.history

    # Return the bot's reply
    return response.text

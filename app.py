import streamlit as st
from gemini_api import get_gemini_response
from nlp_utils import clean_text

st.set_page_config(page_title="StartupGPT", page_icon="🚀")
st.markdown("<h1 style='text-align: center;'>🚀 StartupGPT - Your AI Startup Assistant</h1>", unsafe_allow_html=True)

# --- Custom CSS Styling ---
st.markdown("""
    <style>
    .stChatMessage { padding: 10px; border-radius: 16px; margin-bottom: 10px; }
    .stChatMessage.user { background-color: #DCF8C6; text-align: right; }
    .stChatMessage.assistant { background-color: #F1F0F0; }
    .chatbox input { border-radius: 10px; }
    .suggestion-btn {
        display: inline-block;
        margin: 5px 10px 15px 0;
        background-color: #e0e0e0;
        padding: 5px 12px;
        border-radius: 12px;
        font-size: 14px;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# --- Initialize chat history ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Clear Chat Button ---
if st.button("🧹 Clear Chat"):
    st.session_state.messages = []
    # st.experimental_rerun()
    st.rerun()

# --- Suggested Prompts ---
st.markdown("#### 💡 Suggested Questions:")
cols = st.columns(2)
with cols[0]:
    if st.button("How to get startup funding?"):
        st.session_state.suggested = "How to get startup funding?"
with cols[1]:
    if st.button("What is MVP in a startup?"):
        st.session_state.suggested = "What is MVP in a startup?"

suggested_query = st.session_state.get("suggested", None)

# --- Display chat history ---
for msg in st.session_state.messages:
    role = msg["role"]
    with st.chat_message(role):
        st.markdown(msg["content"])

# --- Input box ---
user_input = st.chat_input("Ask your startup question...")

# --- Use suggested prompt if clicked ---
if suggested_query and not user_input:
    user_input = suggested_query
    st.session_state.suggested = None  # reset after using it

if user_input:
    cleaned = clean_text(user_input)

    # Show user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Typing animation with spinner
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_gemini_response(cleaned)
            st.markdown(response)

    # Save assistant reply
    st.session_state.messages.append({"role": "assistant", "content": response})

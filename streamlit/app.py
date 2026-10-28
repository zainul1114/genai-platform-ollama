import streamlit as st
import requests

st.title("Enterprise AI Chatbot 🚀")
st.caption("Powered by Qwen2.5-Coder, routed via LiteLLM")

LITELLM_URL = "http://litellm:4000/chat/completions"
LITELLM_KEY = "sk-litellm-master-key" 

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a coding question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        payload = {
            "model": "qwen2.5-coder",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 512
        }
        headers = {
            "Authorization": f"Bearer {LITELLM_KEY}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(LITELLM_URL, json=payload, headers=headers)
            response.raise_for_status()
            answer = response.json()["choices"][0]["message"]["content"]
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
        except Exception as e:
            st.error(f"Gateway Error: {e}")

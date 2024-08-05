from openai import OpenAI
import streamlit as st
import ollama

option = None
model = None

with st.sidebar:
    option = st.selectbox(
            "which framework to use?",
        ("Ollama", "Langchain", "OpenAI"),
    )
    if option == 'Ollama':
        model = st.selectbox(
            "which model to use?",
            ("llama3.1", "llama3", "mistral", "phi3")
        )
    elif option == 'Langchain':
        pass
    elif option == 'OpenAI':
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
        "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title(":cloud: Chatbot")
st.caption(":rocket: A Streamlit chatbot powered by OpenAI")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    # if not openai_api_key:
    #     st.info("Please add your OpenAI API key to continue.")
    #     st.stop()
    client = None
    msg = None
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    if option == 'Ollama':
        if model is not None:
            response = ollama.chat(model=model, messages=[
                {
                    'role': 'user',
                    'content': prompt,
                },
            ])
            msg = response['message']['content']
    elif option == 'OpenAI':
        client = OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message.content
    
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
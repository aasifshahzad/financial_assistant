import streamlit as st
from model import initialize_openai_client, submit_message, wait_on_run, assistant_id, process_completed_run
from functions import available_functions

st.set_page_config(page_title="FA with FC&CI", page_icon=":speech_balloon:")

st.sidebar.title("Configuration")
entered_api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

# Check if an API key is entered, then initialize the OpenAI client
client = None
if entered_api_key:
    with st.spinner('Initializing OpenAI Client...'):
        client = initialize_openai_client(entered_api_key)
        st.success('OpenAI Client Initialized!')

    if st.sidebar.button(" Exit  Chat "):
        st.session_state.messages = []  # Clear the chat history
        st.session_state.start_chat = False  # Reset the chat state
        st.session_state.thread_id = None
        st.title("Financial Assistants :bar_chart:")

    # Description
    st.markdown("""
        This assistant is your go-to resource for financial insights and advice. Here's what you can do:
        - :page_facing_up: **Analyze financial statements** to understand your company's health.
        - :chart_with_upwards_trend: **Track market trends** and make informed investment decisions.
        - :moneybag: Receive tailored **investment advice** to maximize your portfolio's performance.
        - :bulb: **Explore various financial scenarios** and plan strategically for future ventures.

        Simply enter your financial query below and let the assistant guide you with actionable insights.
    """)

    st.session_state.start_chat = True
    thread = client.beta.threads.create()
    st.session_state.thread_id = thread.id

    if st.session_state.start_chat:
        if "openai_model" not in st.session_state:
            st.session_state.openai_model = client
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            if message["role"] == "user":
                with st.chat_message("user"):
                    st.markdown(message["content"])
            elif message["role"] == "assistant":
                with st.chat_message("assistant"):
                    st.markdown(message["content"])

        prompt = st.chat_input("Enter your financial query to begin the chat.")
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner('Thinking...'):
            run = submit_message(thread, prompt, assistant_id)
            run = wait_on_run(run, thread, available_functions)

        # Get the assistant messages
        assistant_messages = process_completed_run(run, client, st.session_state)

        # Display assistant messages using Streamlit components
        for message in assistant_messages:
            with st.chat_message("assistant"):
                st.markdown(message.content[0].text.value)

    else:
        st.write("Enter your financial query to begin the chat.")

if not client:
    st.warning("Please enter your OpenAI API key in the sidebar to use the app.")

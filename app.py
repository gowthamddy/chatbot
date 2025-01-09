import streamlit as st
from model import CricketRAGChatbot
import os


def main():
    st.title("Cricket Knowledge Chatbot 🏏")

    # Initialize the chatbot
    if 'chatbot' not in st.session_state:
        try:
            st.session_state.chatbot = CricketRAGChatbot()
            st.success("Chatbot initialized successfully!")
        except Exception as e:
            st.error(f"Error initializing chatbot: {str(e)}")
            return

    # Chat interface
    st.write("Ask me anything about cricket matches!")

    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Your question"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.chatbot.ask_question(prompt)
                    st.markdown(response)
                    # Add assistant response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    error_message = f"Error generating response: {str(e)}"
                    st.error(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})


if __name__ == "__main__":
    main()
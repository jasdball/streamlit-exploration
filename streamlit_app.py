import streamlit as st

def config():
    st.set_page_config(
        page_title="Welcome",
        page_icon=":shark:",
        layout="wide"
    )

def init():
    if 'messages' not in st.session_state:
        st.session_state.messages = []

def main():
    st.title("Welcome to my app!")

if __name__ == '__main__':
    config()
    init()
    main()
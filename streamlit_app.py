import streamlit as st
import time

HEIGHTS = [f"{i}' {j}\"" for i in range(4,7) for j in range (12)]

def config():
    st.set_page_config(
        page_title="Welcome",
        page_icon=":robot_face:",
        layout="wide"
    )

def validate_form():
    name:str = st.session_state.name
    if (name.lower().strip()) == "jason":
        st.error("Nice try!")
        st.session_state.form_output = False
    else:
        st.session_state.form_output = True


def main():
    st.title("Welcome!")
    with st.form(key="user_form",clear_on_submit=True,enter_to_submit=False):
        st.text_input("What's your name?",key="name")
        st.number_input("How old are you?",key="age",step=1)
        st.select_slider("How tall are you?",HEIGHTS,key="height")
        if st.form_submit_button("Submit",on_click=validate_form) and st.session_state.form_output:
            with st.status("Processing your data...",expanded=True):
                time.sleep(3)
                st.write(f"Pondering the name {st.session_state.name}...")
                time.sleep(3)
                st.write(f"Thinking about how anyone can be {st.session_state.age} years old...")
                time.sleep(3)
                st.write(f"Contemplating the height {st.session_state.height}...")
                time.sleep(3)
            st.balloons()
            st.subheader(f"Wow, {st.session_state.name}, you smell like a {st.session_state.height} turd that's been sitting out in the sun for {st.session_state.age} years!")


if __name__ == '__main__':
    config()
    main()
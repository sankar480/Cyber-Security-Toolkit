import streamlit as st
import Home
import Email
import link
import password
import crypto
import file
import pdf


# Define a SessionState class for managing app state
class SessionState:
    def __init__(self):
        self.current_page = "Home"

# Instantiate SessionState
session_state = SessionState()

def main():
    st.sidebar.title("Tools")
    page_options = ["Home", "Temp Email", "Password generator", "Fishing link Finder", "cryptography", "File cryptography", "File Encryptor & Decryptor"]
    selected_page = st.sidebar.selectbox("Go to", page_options)

    # Update current_page based on selected navigation option
    if selected_page != session_state.current_page:
        session_state.current_page = selected_page

    # Display the selected page
    if session_state.current_page == "Home":
        Home.home_page()
    elif session_state.current_page == "Temp Email":
        Email.email_page()
    elif session_state.current_page == "Password generator":
        password.passwordgen_page()
    elif session_state.current_page == "Fishing link Finder":
        link.link_page()
    elif session_state.current_page == "cryptography":
        crypto.crypto_page()
    elif session_state.current_page == "File cryptography":
        pdf.main_page()
    elif session_state.current_page == "File Encryptor & Decryptor":
        file.page()

if __name__ == "__main__":
    main()

import streamlit as st
from mailtm import Email  # Assuming mailtm is a mock library for temporary email services

def email_page():
    def listener(new_message):
        email_page.latest_message = new_message
        st.experimental_rerun()  # Rerun the app to update the latest message display

    # Initialize the Email service
    email_service = Email()
    email_service.register()
    
    # Display the domain and the generated email address
    st.write("Domain: " + email_service.domain)
    st.write("Email Address: " + str(email_service.address))
    
    # Start listening for new emails
    email_page.latest_message = None
    email_service.start(listener)
    
    st.write("Waiting for new emails...")

    # Create an input box with a copy button for the email address
    st.text_input("Your temporary email address", email_service.address, key='email_display')

    # Display the latest email message in a text area
    if email_page.latest_message:
        subject = email_page.latest_mesSsage['subject']
        content = email_page.latest_message.get('text') or email_page.latest_message.get('html', '')
        if isinstance(content, list):  # If content is a list, join it into a string
            content = '\n'.join(content)
        st.text_area("Latest Email Message", f"Subject: {subject}\nContent: {content}", height=300)
    else:
        st.text_area("Latest Email Message", "No new email messages yet.", height=100)       
# st.write("---")
# st.subheader("Hi, This is Cyber Security Tool Kit :wave:")
# st.write("Welcome to the Cyber Security Tools Hub, your comprehensive resource for defending against cyber threats and safeguarding your digital assets. Explore our curated collection of powerful tools designed to enhance your security posture and stay ahead of evolving cyber risks.")
# st.subheader("Our Mission")
# st.write("At Cyber Security Tools Hub, we are dedicated to empowering individuals and organizations with the knowledge and tools needed to protect their data and privacy in an increasingly digital world. Our mission is to make cyber security accessible and understandable for everyone.")
# st.markdown("[Learn More >](https://www.zscaler.com)")

if __name__ == "__main__":
    email_page()


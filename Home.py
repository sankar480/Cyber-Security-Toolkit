import streamlit as st
import requests
from streamlit_lottie import st_lottie

def home_page():
# Function to load Lottie animation from URL
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Function to inject local CSS styles
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    def main():
        st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

        # Load local CSS styles
    local_css("style.css")

    st.subheader("Hi, This is Cyber Security Tool Kit :wave:")
    st.write("Welcome to the Cyber Security Tools Hub, your comprehensive resource for defending against cyber threats and safeguarding your digital assets. Explore our curated collection of powerful tools designed to enhance your security posture and stay ahead of evolving cyber risks.")
    st.subheader("Our Mission")
    st.write("At Cyber Security Tools Hub, we are dedicated to empowering individuals and organizations with the knowledge and tools needed to protect their data and privacy in an increasingly digital world. Our mission is to make cyber security accessible and understandable for everyone.")
    st.markdown("[Learn More >](https://www.zscaler.com)")

    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
                    st.header("What we do!")
                    st.write("## Decide on the types of cyber security tools you want to feature on your website. This could include:")
                    st.write("- Vulnerability scanners")
                    st.write("- Antivirus and malware detection software")
                    st.write("- Network monitoring tools")
                    st.write("- Encryption tools")
                    st.write("- Password managers")
                    st.write("- Incident response and forensic tools")
                    st.write("- Educational resources (blogs, tutorials, webinars)")
                    st.markdown("[Learn video >]()")
    with right_column:
                    lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
                    st_lottie(lottie_coding, height=300, key="coding")

    st.write("---")
    st.header("Our Project")
    image_column, text_column = st.columns((1, 2))
    with text_column:
                    st.subheader("")
                    st.write("At Cyber Security Tools Hub, we are dedicated to empowering individuals and organizations with the knowledge and tools needed to protect their data and privacy in an increasingly digital world. Our mission is to make cyber security accessible and understandable for everyone.")

    st.write("---")
    st.header("Get In Touch With Me!")
    contact_form = """
                    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
                        <input type="hidden" name="_captcha" value="false">
                        <input type="text" name="name" placeholder="Your name" required>
                        <input type="email" name="email" placeholder="Your email" required>
                        <textarea name="message" placeholder="Your message here" required></textarea>
                        <button type="submit">Send</button>
                    </form>
                """
    left_column, right_column = st.columns(2)
    with left_column:
                    st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
                    st.empty()

        
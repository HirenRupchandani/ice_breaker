import streamlit as st
# from langchain.llms import OpenAI
from dotenv import load_dotenv
from ice_breaker import ice_break
import requests

load_dotenv()

st.set_page_config(page_title="Hiren Rupchandani - Profile Summary", page_icon=":bird:")

st.title("🦜🔗 About Hiren Rupchandani")

st.subheader("Learn About Hiren and the roles he would be fit for")

linkedin_url = "https://www.linkedin.com/in/hiren-rupchandani/"
github_url = "https://github.com/hirenrupchandani"
email_url = "mailto:hrupchan@iu.edu"

with st.form("my_form"):
    position = st.text_input("Enter the position", placeholder="e.g., Data Analyst")
    # text = st.text_area("Enter text:", "Tell me something about Hiren Rupchandani")
    submitted = st.form_submit_button("Get some summary, facts, and position rating")
    if submitted:
        data, profile_pic_url = ice_break(name="Hiren Rupchandani", position=position)

        print(profile_pic_url)

        summary = data.summary
        facts = data.facts
        rating = data.rating

        col1, col2 = st.columns([1, 2])

        with col1:
            image_html = f"""
            <div style="text-align: center;">
                <img src="{profile_pic_url}" alt="Hiren Rupchandani" style="width:100%;">
                <br>
                <a href="https://www.linkedin.com/in/hiren-rupchandani-45a646157/" target="_blank" style="margin: 0 10px;">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/a/a3/Linkedin_%28CoreUI_Icons_v1.0.0%29.svg" alt="LinkedIn" style="width:32px;height:32px;">
                </a>
                <a href="https://github.com/hirenrupchandani" target="_blank" style="margin: 0 10px;">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" style="width:32px;height:32px;">
                </a>
            </div>
            """
            st.markdown(image_html, unsafe_allow_html=True)

        with col2:
            st.subheader("About Hiren")
            st.write(summary)
        st.subheader("Some Facts")
        for fact in facts:
            st.write(f"- {fact}")

        st.subheader("Rating")
        st.write(rating)
        print(data)

footer_html = f"""
<div style="padding: 10px; text-align: center; position: sticky; width: 100%; border: solid grey; border-width: 1px; border-radius: 5px">
    <div style="margin-top: 10px;">
        <span style="font-size: 1.2em; font-weight: bold;">Connect with me</span>
        <div style="margin-top: 10px;">
            <a href="{linkedin_url}" target="_blank" style="margin: 0 10px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/b/b0/Linkedin_footer.svg" alt="LinkedIn" style="width:32px;height:32px;">
            </a>
            <a href="{github_url}" target="_blank" style="margin: 0 10px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg" alt="GitHub" style="width:32px;height:32px;">
            </a>
            <a href="{email_url}" target="_blank" style="margin: 0 10px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/5c/Email_Logo_PNG.png" alt="Email" style="width:32px;height:32px;">
            </a>
        </div>
    </div>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)


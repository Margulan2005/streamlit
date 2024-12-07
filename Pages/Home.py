from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":cold_face:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

lottie_coding = load_lottieurl("https://lottie.host/66535123-7d5b-47d2-bd29-f35b831bccfd/nKC3J3nDm4.json")
img_contact_form = Image.open("img/palmer.jpg")
img_lottie_animation = Image.open("img/cold.jpg")

with st.container():
    st.subheader("Hi, my name is Margulan :wave:")
    st.title("Cole Palmer")
    st.write("Cole Jermaine Palmer is an English professional footballer who plays for Chelsea and the England national team.")
    st.write("[Learn more >](https://www.chelseafc.com/en)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About him")
        st.write("##")
        st.write(
            """
            - Name in home country: Cole Jermaine Palmer
            - Date of birth/Age: May 6, 2002 (22)
            - Place of birth: Manchester
            - Height: 1,85 m
            - Citizenship: England
            - Position: Midfield - Attacking Midfield
            - Foot: left
            - Player agent: CAA Base Ltd
            - Current club: Chelsea FC
            - Joined: Sep 1, 2023
            - Contract expires: Jun 30, 2033
            - Last contract extension: Aug 13, 2024
            - Outfitter: Nike
            """
        )
        st.write("[Instagram >](https://www.instagram.com/colepalmer10/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="Chelsea")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Unstoppable! Cole Palmer's Goals & Assists for Chelsea")
        st.write(
            """
            A young attacking player of outstanding all-round quality who can create and score goals, 
            his first year at Stamford Bridge could hardly have gone better as he was awarded Player 
            of the Season and became a full England international. In July 2024, he scored for his 
            nation in the European Championship final versus Spain.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/3CFm0dj96sI)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Cole Palmer 2024 - Skills, Goals & Assists | HD")
        st.write(
            """
            Ahead of the start of the 2024/25 campaign, there was good news for Chelsea fans when 
            Palmer signed a two-year contract extension, committing him to the club until 2033. Very 
            soon after he was one of the nominees for the prestigious Ballon d'Or and he was ranked 25th 
            for that award when the vote result was announced.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/DHiAtzlw8Nk)")

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/margulantursynkhan2005@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Margulan" required>
        <input type="email" name="email" placeholder="margulantursynkhan2005@gmail.com" required>
        <textarea name="message" placeholder="Your Message Here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

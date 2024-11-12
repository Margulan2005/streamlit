import streamlit as st
from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar
import os
from PIL import Image
import pandas as pd
import numpy as np

image = Image.open('img/liverpool.png')
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)

logo_path = os.path.join(os.path.dirname(__file__), "img", "realmadrid.svg")
pages = [" ",'Home','Project1', 'Project2', 'Project3']

styles = {
    "nav": {
        "background": "linear-gradient(to right, #4CAF50, #00BCD4)",  # Gradient color
        "display": "flex",
        "justify-content": "center",
        "padding": "10px 0",  # Extra padding for a thicker navbar
        "border-radius": "8px",  # Rounded corners for a modern look
    },
    "img": {
        "position": "absolute",
        "left": "20px",  # Adjust logo position for better alignment
        "top": "4px",
        "width": "80px",
        "height": "40px",
    },
    "span": {
        "display": "block",
        "color": "#FFFFFF",  # White text for readability
        "padding": "0.5rem 1rem",  # Extra padding for larger clickable areas
        "font-size": "16px",  # Slightly larger font size
        "transition": "background 0.3s ease, color 0.3s ease",  # Smooth transition effect
    },
    "active": {
        "background-color": "#FFFFFF",  # White background for active tab
        "color": "#4CAF50",  # Green text for the active tab to match gradient
        "font-weight": "bold",
        "padding": "14px",
        "border-radius": "4px",  # Slightly rounded active tab
    }
}

options = {
    "show_menu": False,
    "show_sidebar": True,
}

page = st_navbar(pages,
    styles=styles,
    logo_path=logo_path,
    options=options)

if page == 'Home':
    Home.Home().app()
elif page == "Project1":
    Project1.Project1().app()
elif page == "Project2":
    Project2.Project2().app()
elif page == "Project3":
    Project3.Project3().app()
else:
    Home.Home().app()
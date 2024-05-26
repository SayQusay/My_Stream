import streamlit as st
import pandas as pd
import plost
import numpy as np
from st_click_detector import click_detector

content = """
    <a href='#' id='Image 1'><img width='20%' src='https://images.unsplash.com/photo-1565130838609-c3a86655db61?w=200'></a>
    """
clicked = click_detector(content)

st.markdown(f"**{clicked} clicked**" if clicked != "" else "**No click**")

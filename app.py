import streamlit as st
import pandas as pd
import numpy as np

def main_page():
    st.markdown("# Main page")
    st.sidebar.markdown("Main Page")

def page2():
    st.markdown(" Data")
    st.sidebar.markdown("Data")

def page3():
    st.markdown("RR Detection")
    st.sidebar.markdown("RR Detection")

def page4():
    st.markdown("HRV Analysis")
    st.sidebar.markdown("HRV Analysis")

page_names_to_func = {
    "Main Page": main_page,
    "Data":page2,
    "RR Detection":page3,
    "HRV Analysis":page4,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


import streamlit as st

st.title("PyTorch Availability Check")

try:
    import torch
    st.success("PyTorch is installed.")
except ImportError:
    st.error("PyTorch is not installed.")

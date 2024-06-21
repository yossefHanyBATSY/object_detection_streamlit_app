import streamlit as st 
from PIL import Image
from model import *

st.title("Image Uploader")

uploaded_file=st.file_uploader("choose an image file",type=["jpg","jpeg","png"])

if uploaded_file is not None:
    image=Image.open(uploaded_file).convert("RGB")
    st.image(uploaded_file,caption="Uploaded Image")
    
    
    if(st.button('Analyse Image')):
        component_names=process_image(image)
        st.write("components identified in the image")
        for name in component_names:
            st.write(name)
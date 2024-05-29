import streamlit as st
import torch
from torchvision import transforms
from PIL import Image


# Konfigurasi halaman
st.set_page_config(page_title="CNN for Breast Cancer", layout="wide")

# Buat option menu
option = st.sidebar.selectbox("Menu", ["Home", "CNN Analysis"])

# Halaman Home
if option == "Home":
    st.markdown("<h1 style='text-align: center; '>Confronting Breast Cancer: Urgent Call for Awareness</h1>", unsafe_allow_html=True)


    #Show the Urgency
    st.subheader("It's a :red[scary] thing for women")
    st.markdown("<h4 style='text-align: center; color: #EB455F;'>Breast cancer is the most common cancer among women in 158 of 183 countries (86%) and the leading cause of female cancer deaths in 107 of 183 countries (Omer, A.M., et al, 2023)</h4>", unsafe_allow_html=True)
    st.write("""
    In 2020, 2.3 million women were diagnosed with breast cancer, with 685,000 deaths globally. At the end of 2020, 7.8 million women who had been diagnosed with breast cancer in the previous five years were still alive, making breast cancer the most prevalent malignancy (Allahqoli et al., 2022)
    """)
    st.divider()

    #What can we Do
    st.subheader("Developing technology to make :grey[automatic] detection")
    st.write("""
    Technological developments encourage the creation of more effective and efficient work systems. In the health sector, an early detection system is very much needed. Apart from making radiology work easier, experts can also more easily carry out interventions more quickly.
    - **Automatic Detection with CNN**
         CNNs can learn to recognize patterns and features in images that may not be visible to the human eye.
         
    - **Tumor Segmentation**
         CNNs can be used for tumor segmentation in medical images, helping more accurately determine tumor size and location.
         
    - **Risk Prediction**
         CNN-based algorithms can predict breast cancer risk by analyzing medical images and other patient data, helping doctors make clinical decisions.
    """)
    st.divider()
    
    st.subheader("Why do we use :green[CNN] instead of :red[ANN]")
    st.write("""
    **Too many parameters for a small image dimension.** 
    For example, a 28x28 MNIST image requires around 105.124 parameters that consist of input, hidden layers 1 & 2, and output layer.
    
    **CNN works best to extract image features automatically.** 
    CNN can learn the most discriminative feature from raw image pixels, which is needed in the model’s training process.
    
    **CNN is insensitive to translation and different positions of input images.** 
    Hence, unlike ANN, CNN could recognize patterns regardless of the position in the image. This quality is crucial to have for an accurate breast cancer classification.
    """)

    st.divider()
    st.subheader("Project Description: CNN with ResNet")
    st.write("""
    The size of the breast images used is 256x256 px.
    
    The total images used to train the model is 1.016 images with 507 cancerous images and 509 normal images.
    
    Residual Network (ResNet) is used for the architecture, where it utilizes the concept of skip connections, where the network will learn about the residual mapping of input to output rather than the entire mapping. Hence, the gradients calculated during backpropagation are not prone to vanishing. 
    
    :green-background[In summary], CNN with ResNet offers an effective yet intense training process without degrading the model’s accuracy performance.
    """)

    st.divider()
    st.subheader("Introducing our Community")

# Halaman CNN Analysis
elif option == "CNN Analysis":
    uploaded_file = st.file_uploader("Choose an image...", type="png")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
    
    col1,col2 = st.columns([0.3,0.7],gap='medium')
    
    with col1:
        st.markdown('''
        **View**
        ''')
        view = st.radio(
            "Choose your medical view",
            ["MLO", "CC"],
            index=None,
        )
        st.divider()
        
        arc = st.radio(
            "Select your architecture network",
            ["CNN", "ResNet18"],
            index=None,
        )
        apply = st.button("Apply",type="secondary")
        if apply:
            if arc == 'CNN':
                if view == 'Mlo':
                    st.write('a')
                else:
                    st.write('b')
            else:
                if view == 'Mlo':
                    st.write('C')
                else:
                    st.write('d')
        st.divider()
       

    with col2:
        st.markdown('''
        **Output Images**
        ''')

        st.image(image)
        
       

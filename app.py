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
    st.title("Why do we use CNN instead of ANN")
    st.write("""
    **Too many parameters for a small image dimension.** 
    Ex: a 28x28 MNIST image requires around 105.124 parameters that consist of input, hidden layers 1 & 2, and output layer.
    
    **CNN works best to extract image features automatically.** 
    As in, it’s able to learn the most discriminative feature from raw image pixels, which is needed in the model’s training process.
    
    **CNN is insensitive to translation and different positions of input image.** 
    Hence, unlike ANN, CNN could recognize patterns regardless of the position in the image. This quality is crucial to have for an accurate breast cancer classification.
    """)
    st.title("Project Description: CNN with ResNet")
    st.write("""
    The size of the breast images used is 256x256 px.
    
    The total images used to train the model is 1.016 images with 507 cancerous images and 509 normal images.
    
    Residual Network (ResNet) is used for the architecture, where it utilizes the concept of skip connections, where the network will learn about the residual mapping of input to output rather than the entire mapping. Hence, the gradients calculated during backpropagation are not prone to vanishing. 
    
    :green-background[In summary], CNN with ResNet offers an effective yet very deep training process without degrading the model’s accuracy performance.
    """)

# Halaman CNN Analysis
elif option == "CNN Analysis":
    tab1, tab2 = st.tabs(["CNN", "CNN + ResNet"])

    # Untuk menampilkan "sesuatu" di tab1
    with tab1:
        st.header("CNN Analysis")
        st.write("Here you can add the CNN program details.")
        # Tambahkan kode atau deskripsi untuk CNN Anda di sini

    # Untuk menampilkan "sesuatu" di tab2
    with tab2:
        st.header("CNN + ResNet Analysis")
        st.write("Here you can add the CNN + ResNet program details.")

        # Load your model
        PATH = "/content/model_v1.pth"

        # Dummy model for example purposes, replace with your actual model
        # Example:
        # model = YourModelClass()
        # model.load_state_dict(torch.load(PATH))
        # model.eval()

        transform = transforms.Compose([transforms.ToTensor()])

        def predict(image_path):
            image = Image.open(image_path).convert('RGB')
            image = transform(image)
            image = image.unsqueeze(0)

            with torch.no_grad():
                output = model(image)
                prediction = torch.max(output.data, 1)[1]
                return prediction.item()

        # File uploader
        uploaded_file = st.file_uploader("Choose an image...", type="png")

        if uploaded_file is not None:
            image_path = uploaded_file.name
            with open(image_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            result = predict(image_path)
            
            if result == 0:
                st.write('Prediction: benign')
            else:
                st.write('Prediction: malignant')

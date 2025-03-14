import os
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image
import requests
import streamlit as st

#pip install virtualenv
#virtualenv tensorflow_env
#source tensorflow_env/bin/activate
#pip install tensorflow tensorflow-hub numpy Pillow requests streamlit

def load_image_from_path(image_file):
    image = Image.open(image_file)
    image = image.resize((224, 224))
    return np.array(image) / 255.0

def load_model():
    model_url = "https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/classification/4"
    return hub.KerasLayer(model_url)

def predict_image_class(image, model):
    image = np.expand_dims(image, axis=0)
    logits = model(image)
    return np.argmax(logits)

def get_imagenet_labels():
    labels_filename = 'ImageNetLabels.txt'
    if not os.path.isfile(labels_filename):
        st.info("Downloading ImageNet labels...")
        url = 'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt'
        response = requests.get(url)
        with open(labels_filename, 'w') as f:
            f.write(response.text)
    with open(labels_filename, 'r') as file:
        labels = file.read().split('\n')
    return labels

def main():
    st.title("Cat Image Classifier")
    image_file = st.file_uploader("Upload an image", type=['png', 'jpeg', 'jpg'])
    if image_file is not None:
        image = load_image_from_path(image_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        if st.button('Predict'):
            model = load_model()
            predicted_class = predict_image_class(image, model)
            labels = get_imagenet_labels()
            if 'cat' in labels[predicted_class].lower():
                st.success("Cat detected!")
                st.write("Generic Cat DNA:", "ATCGTTACGTGACGGATCACGTACGTAGCTAGCT")
            else:
                st.error("No cat detected.")

if __name__ == "__main__":
    main()

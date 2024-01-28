import streamlit as st
import matplotlib.image as img
from PIL import Image
from sklearn.cluster import KMeans
from PIL import Image, ImageDraw
import numpy as np

title = st.title("Colors Extractor Website")


def create_color_palette(dominant_colors, palette_size=(300, 50)):
    # Create an image to display the colors
    palette = Image.new("RGB", palette_size)
    draw = ImageDraw.Draw(palette)

    # Calculate the width of each color swatch
    swatch_width = palette_size[0] // len(dominant_colors)

    # Draw each color as a rectangle on the palette
    for i, color in enumerate(dominant_colors):
        draw.rectangle([i * swatch_width, 0, (i + 1) * swatch_width, palette_size[1]], fill=tuple(color))

    return palette


uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
dominant_colors = st.slider("Select a number", min_value=0, max_value=10, value=10, step=1, format="%d")

if int(dominant_colors) <= 0:
    st.write("Please enter number greater than 0")
else:
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        image = img.imread(uploaded_file)
        X = image.reshape(-1, 3)
        kmeans = KMeans(n_clusters=int(dominant_colors))
        kmeans.fit(X)
        st.title('Your Dominant Colors are:')
        st.image(create_color_palette(kmeans.cluster_centers_.astype('int')))

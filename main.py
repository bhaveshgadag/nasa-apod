from nasa_api import get_apod
import requests
import streamlit as st

content = get_apod()

image = requests.get(content['url'])

with open('image.jpg', 'wb') as file:
    file.write(image.content)

st.title(content['title'])
st.image("image.jpg")
st.write(content['explanation'])

from nasa_api import get_apod
import requests
import streamlit as st

st.title("hello")

content = get_apod()

image = requests.get(content['url'])

with open('image.jpg', 'wb') as file:
    file.write(image.content)

print(content)
st.image()
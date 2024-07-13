import streamlit as st
import pandas as pd
import numpy as np
import requests
import dotenv



def get_tile(zoom, x, y):
  url = f"https://retina-tiles.p.rapidapi.com/local/osm@2x/v1/{zoom}/{x}/{y}.png"
  headers = {
    "x-rapidapi-key": "cff35cfbd4msh1bcd30de22d14aep17e308jsndcd80f735349",
    "x-rapidapi-host": "retina-tiles.p.rapidapi.com"
  }
  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    with open("hello.png", "wb") as f:
      f.write(response.content)
  else:
    print(f"Failed to retrieve image. Status code: {response.status_code}")

get_tile(12, 0, 0)

st.set_page_config(page_title="Metrocraft")
st.title('Metrocraft: ')
st.subheader("The AI urban planning and civil policy platform for frustrated citizens and sci-fi enthusiasts!")
df = pd.DataFrame(
  [[37.7699, -122.226]],
  columns = ["lat", "lon"]
)
st.map(df)

# Function to save return_val to a text file
def save_to_file(data, filename="return_val.txt"):
    with open(filename, "w") as file:
        file.write(str(data))

# Example prompt variable
prompt = "Your prompt here"

# Streamlit button
if st.button('Submit'):
    return_val = True  # Replace with actual return value logic

    if return_val == True:
        st.success(f"{prompt} registered successfully")
        save_to_file(return_val)
    else:
        st.error('Please enter the prompt again')
        save_to_file(return_val)
    
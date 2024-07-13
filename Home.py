import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
import coordinates
from openai import OpenAI
import re

st.set_page_config(page_title="Metrocraft", layout='wide')


load_dotenv()



st.title('Metrocraft: ')
st.subheader("The AI urban planning and civil policy platform for frustrated citizens and sci-fi enthusiasts!")

# Function to save a prompt to a text file by appending
def save_to_file(data, filename="prompt.txt"):
    with open(filename, "a") as file:
        file.write(f"{data}\n")

# Function to load prompts from a file
def load_prompts_from_file(filename="prompt.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

# Initialize session state for prompts list if not already done
if 'prompts' not in st.session_state:
    st.session_state.prompts = load_prompts_from_file()

# Example prompt variable
prompt = st.text_input("Your prompt here")

# Streamlit button
if st.button('Submit'):
    return_val = True  # Replace with actual return value logic

    if return_val == True:
        st.success(f"Prompt accepted")
        st.session_state.prompts.append(prompt)
        save_to_file(prompt)
    else:
        st.error('Please enter the prompt again')

# Display the list of prompts
st.write("Prompts List:")
for i, p in enumerate(st.session_state.prompts, 1):
    st.write(f"{i}. {p}")

df = pd.DataFrame(
    [[37.7699, -122.226]],
    columns=["lat", "lon"]
)
st.map(df)

import streamlit as st
import pandas as pd
import numpy as np
import requests
from dotenv import load_dotenv
import os
import math
import coordinates
from openai import OpenAI
import re
from graphs import construct_graph
import mistral_query
import json

# Initialize the last_line variable
last_line = ""

# Set the configuration for the Streamlit page
st.set_page_config(page_title="Metrocraft", layout='wide')
st.title("MetroCraft: the AI urban planner and policymaker!")
# Load environment variables from a .env file
load_dotenv()

# Function to save a given data to a text file by appending
def save_to_file(data, filename="prompt.txt"):
    with open(filename, "a") as file:
        file.write(f"{data}\n")

# Function to load prompts from a text file
def load_prompts_from_file(filename="prompt.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

# Initialize session state for the list of prompts if not already done
if 'prompts' not in st.session_state:
    st.session_state.prompts = load_prompts_from_file()

# Text input for the user to enter a prompt
prompt = st.text_input("Prompt (example: write a 5 step plan to turn Bangalore into a vertical metropolis")
# Text input for the user to enter a city name
city = st.text_input("City name")

# Initialize session state for policies list
st.session_state.policies = []

# Streamlit button to submit the entered prompt and city
if st.button('Submit'):
    return_val = True  # Replace with actual return value logic

    if return_val:
        st.success(f"Prompt accepted")
        st.session_state.prompts.append(prompt)
        
        # Save the city and prompt to text files
        save_to_file(city, "cities.txt")
        save_to_file(prompt)
        
        # Get coordinates of the city and generate an image
        coordinates.get_coords(city)
        with open('./cities.txt') as f:
            for line in f:
                pass
            last_line = line.strip()
            st.image(f"{last_line}.png")
        
        # Create a policy based on the prompt and generate a graph
        policy = mistral_query.create_policy(f"{prompt}")
        mistral_query.create_graph(policy)
        
        # Add the policy to session state and display it
        st.session_state.policies.append(policy)
        print(st.session_state.policies)
        st.image(f"{city}.png")
        st.title("Policies")
        st.write(json.dumps(json.loads(policy)))
        
    else:
        st.error('Please enter the prompt again')

# Display the list of prompts
st.write("Prompts List:")
for i, p in enumerate(st.session_state.prompts, 1):
    st.write(f"{i}. {p}")

# Experimental function for dialog interaction
@st.experimental_dialog("e")
def heil(heil):
    st.write("hello")
 
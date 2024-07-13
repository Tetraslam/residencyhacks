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
import json


client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
systemprompt = "You are a strategic public policy planner who helps create roadmaps for urban development. You speak concisely and focus on the end goal, generating ONE easy to parse json object containing each step."
userprompt = "Create a 5 step plan to expand defense around kowloon walled city"
completion = client.chat.completions.create(
  model="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
  messages=[
    {"role": "system", "content": f"{systemprompt}"},
    {"role": "user", "content": f"{userprompt}"}
  ],
  temperature=0.7)

graph_edges =  [[1,2], [2,3], [3,4], [1, 3]]

print(completion.choices[0].message.content)
systemprompt = "You are a helpful network graph assistant. You identify edges between nodes based on natural language connections and your own knowledge. Reply to the user's list of nodes with a list in the form [[node1number, node2number], [node2number, node3number]], where each element represents a connection between nodes. Node indices start at 0 (the first node given by the user)."
userprompt = completion.choices[0].message.content
graph_edges = client.chat.completions.create(
  model="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
  messages=[
    {"role": "system", "content": f"{systemprompt}"},
    {"role": "user", "content": f"{userprompt}"}
  ],
  temperature=0.7)
construct_graph(f"System prompt: {systemprompt} \n User prompt: {userprompt}",
                num_of_vertices=5,
                policy_names=list(json.loads(completion.choices[0].message.content).keys()),
                policy_descriptions=list(json.loads(completion.choices[0].message.content).values()),
                edges=graph_edges.choices[0].message.content)

# Load environment variables
load_dotenv()

coordinates.get_coords("paris")
st.title("hello")

@st.experimental_dialog("e")
def heil(heil):
  st.write("hello")
  
heil("e")
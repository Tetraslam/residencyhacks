import streamlit as st
import os

st.set_page_config(page_title="Voting", layout='wide')
st.title('Vote for change')
st.subheader("Vote for your favorite policy here!")

# Function to save votes to a file
def save_votes_to_file(votes, filename="votes.txt"):
    with open(filename, "a") as file:
        for prompt, count in votes.items():
            file.write(f"{prompt}:{count}\n")

# Function to load votes from a file
def load_votes_from_file(filename="votes.txt"):
    votes = {}
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                prompt, count = line.strip().split(":")
                votes[prompt] = int(count)
    return votes

# Function to read prompts from a file
def read_prompts_from_file(filename="prompt.txt"):
    prompts = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            prompts = [line.strip() for line in file.readlines()]
    return prompts

# Function to save prompts to a file
def save_prompt_to_file(prompt, filename="prompt.txt"):
    with open(filename, "a") as file:
        file.write(f"{prompt}\n")

# Load existing votes
votes = load_votes_from_file()

# Load prompts from the prompt.txt file into session state
if 'prompts' not in st.session_state:
    st.session_state.prompts = read_prompts_from_file()

if st.session_state.prompts:
    # Create a dropdown menu for selecting a prompt
    selected_prompt = st.selectbox("Select a prompt", st.session_state.prompts)

    # Display the selected prompt and a button to vote for it
    if st.button('Vote'):
        if selected_prompt in votes:
            votes[selected_prompt] += 1
        else:
            votes[selected_prompt] = 1
        save_votes_to_file(votes)
        st.success(f"Voted for: {selected_prompt}")

    # Display the current votes for each prompt
    st.header("Current Votes")
    for prompt, count in votes.items():
        st.write(f"{prompt}: {count} votes")
else:
    st.error('No prompts found in prompt.txt.')

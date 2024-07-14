from openai import OpenAI
from dotenv import load_dotenv
from graphs import construct_graph
import json
import ast
from functools import cache
import re

# Load environment variables
load_dotenv()

def last_line(filename):
    """
    Get the last line from a text file.
    
    Args:
        filename (str): The name of the file (without extension).
    
    Returns:
        str: The last line of the file.
    """
    with open(f'./{filename}.txt') as f:
        for line in f:
            pass
        return line.strip()

def find_largest_json_object(text):
    """
    Find the largest JSON object in a given text.
    
    Args:
        text (str): The text containing JSON objects.
    
    Returns:
        str: The largest JSON object found in the text.
    """
    json_regex = re.compile(r'''
          (
              \{                          # Opening curly brace for an object
              (?:                         # Non-capturing group for key-value pairs
                  [^{}]*                  # Anything except curly braces
                  |                       # OR
                  \{(?:[^{}])*?\}         # Nested object (recursively match)
              )*
              \}                          # Closing curly brace for an object
          )
    ''', re.VERBOSE)
    matches = json_regex.findall(text)
    largest_json = None
    largest_size = 0
    
    for match in matches:
        try:
            parsed_json = json.loads(match)
            json_size = len(json.dumps(parsed_json))
            if json_size > largest_size:
                largest_size = json_size
                largest_json = match
        except json.JSONDecodeError:
            continue
    
    return largest_json

def string_to_list(string):
    """
    Convert a string representation of a list to an actual list.
    
    Args:
        string (str): The string representation of the list.
    
    Returns:
        list: The converted list.
    
    Raises:
        ValueError: If the string does not represent a valid list.
    """
    try:
        result = ast.literal_eval(string)
        if isinstance(result, list):
            return result
        else:
            raise ValueError("The provided string does not represent a list")
    except (ValueError, SyntaxError) as e:
        raise ValueError(f"Invalid string format: {e}")

# Initialize OpenAI client with local server settings
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

def create_policy(user_prompt):
    """
    Generate a policy in JSON format based on a user prompt using the OpenAI API.
    
    Args:
        user_prompt (str): The user's prompt for generating the policy.
    
    Returns:
        str: The generated policy as a JSON string.
    """
    systemprompt = "You are a strategic public policy planner who helps create roadmaps for urban development. You respond concisely and focus on the end goal, generating ONE easy to parse json object containing each step. Do not generate any additional text outside the JSON object."
    completion = client.chat.completions.create(
        model="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
        messages=[
            {"role": "system", "content": systemprompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7)
    return completion.choices[0].message.content

def create_graph(policy_content):
    """
    Create and visualize a graph based on the generated policy content using the OpenAI API.
    
    Args:
        policy_content (str): The content of the policy in JSON format.
    
    Returns:
        None
    """
    systemprompt = "You are a helpful network graph assistant. You identify edges between nodes based on natural language connections and your own knowledge. Reply to the user's list of nodes with a list in the form [[node1number, node2number], [node2number, node3number]], where each element represents a connection between nodes. Make sure that there are more edges than vertices. Node indices start at 0 (the first node given by the user)."
    
    graph_edges_response = client.chat.completions.create(
        model="TheBloke/Mistral-7B-Instruct-v0.1-GGUF",
        messages=[
            {"role": "system", "content": systemprompt},
            {"role": "user", "content": policy_content}
        ],
        temperature=0.7)
    
    list_graph_edges = string_to_list(graph_edges_response.choices[0].message.content)
    print(list_graph_edges)

    # Debug statements
    largest_json = find_largest_json_object(policy_content)
    print("Largest JSON Object:", largest_json)
    print("Type of Largest JSON Object:", type(largest_json))
    
    policy_dict = json.loads(largest_json)
    print("Policy Dict:", policy_dict)
    print("Type of Policy Dict:", type(policy_dict))

    # Construct and save the graph
    construct_graph(f"System prompt: {systemprompt} \n User prompt: {policy_content}",
                    num_of_vertices=5,
                    policy_names=list(policy_dict.keys()),
                    policy_descriptions=list(policy_dict.values()),
                    edges=list_graph_edges,
                    city_name=last_line("cities"))

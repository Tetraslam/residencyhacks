# MetroCraft: AI-Powered Urban Planning and Policy Making

Welcome to **MetroCraft**, the platform for AI-driven urban planning and policy making! This project aims to leverage LLMs and satellite data to design and visualize strategic urban policies, ensuring a smarter, more efficient future for cities worldwide. Our goal is to allow urban planners, policymakers, and communities to make informed, data-driven decisions.

Voter manipulation should be a decentralized decision (the irony is strong with this one).

## Table of Contents
- [MetroCraft: AI-Powered Urban Planning and Policy Making](#metrocraft-ai-powered-urban-planning-and-policy-making)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

MetroCraft uses Mistral-7B-Instruct locally and interactive visualizations to create comprehensive urban policies based on user-provided prompts. Users can input their ideas for urban development, and MetroCraft generates detailed plans, visualizations, and strategic roadmaps. We're also adding civil infrastructure maps to the menu in the future.

## Features

- **AI-Driven Policy Generation**: Generates urban policies using LLMs for the nitty-gritty.
- **Interactive Voting System**: Allows users to vote on their favorite policies.
- **Graph Construction**: Visualizes urban policies as interactive graphs.
- **Geospatial Integration**: Retrieves and displays city coordinates on map tiles.
- **User-Friendly Interface**: Simple, intuitive UI built with Streamlit.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/metrocraft.git
   cd metrocraft
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your API keys:
   ```
   OPENWEATHER=your_openweather_api_key
   RAPID_API_KEY=your_rapidapi_key

5. **LMStudio Query Server**:
   Download [LMStudio](https://lmstudio.ai/) if you haven't already, and download TheBloke/Mistral-7B-Instruct-v0.1. You can then open the "Local Server" section in the sidebar and start the server. MetroCraft is already set up to use the default port (`1234`).
   ```

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run main.py
   ```

2. **Input prompts and city names**: 
   - Enter a policy prompt and city name to generate urban planning strategies.
   - View the generated policies and their visualizations.
   
3. **Vote for policies**:
   - Navigate to the voting page to vote for your favorite policies.
   - View the current voting results. [in progress]

## Project Structure

- **main.py**: The main entry point for the Streamlit application. Handles user inputs and displays policy generation results.
- **voting.py**: Manages the voting system for policies, allowing users to vote and view results.
- **graphs.py**: Contains functions for constructing and visualizing graphs based on urban policies.
- **coordinates.py**: Handles geospatial data retrieval, converting city names to coordinates and fetching map tiles.
- **mistral_query.py**: Interacts with the AI models to generate policies and graph edges.

## Contributing

We welcome contributions from the community! If you'd like to contribute to MetroCraft, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Join us in shaping the cities of tomorrow with intelligent, data-driven urban planning and policymaking. Together, we can create sustainable, efficient, and vibrant urban environments. Let's build the future with MetroCraft! And don't let those dirty politicians take away the bicycle lanes you deserve.
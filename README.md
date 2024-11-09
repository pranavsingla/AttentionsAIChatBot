# One-Day Tour Planning Application

## Overview
This is a one-day tour planning assistant that helps users create a comprehensive plan for exploring a city based on their preferences. The system uses a combination of FastAPI, Neo4j, and Streamlit to provide a seamless and personalized experience.

## Installation
1. Clone the repository
2. Navigate to the project directory
3. Install the required dependencies:



## Running the Application Locally

You'll have to go to transformers, huggingface llama3 homepage to get access to model_id = "meta-llama/Meta-Llama-3-8B" which is a gated repo to run the following code. You can also directly ask for access to following gated model: https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct . It will only take a few minutes :)

1. Start the FastAPI backend:
uvicorn backend.main:app --reload

2. Start the Streamlit frontend:
streamlit run frontend/main.py


## Usage
- Open the Streamlit app in your browser
- Enter your preferences and generate an itinerary
- View and adjust your itinerary dynamically

## Note
- Ensure Neo4j database is running and accessible.
import streamlit as st
import requests

# Define the Streamlit app
st.title("One-Day Tour Planning Assistant")

# Collect user input
city = st.text_input("Enter the city you want to visit:")
start_time = st.text_input("Enter the start time of your trip:")
end_time = st.text_input("Enter the end time of your trip:")
budget = st.number_input("Enter your budget for the day:", min_value=0.0)
interests = st.multiselect("Select your interests:", ["Culture", "Adventure", "Food", "Shopping"])

if st.button("Generate Itinerary"):
    # Send user preferences to backend API
    preferences = {
        "city": city,
        "start_time": start_time,
        "end_time": end_time,
        "budget": budget,
        "interests": interests
    }
    response = requests.post("http://localhost:8000/generate_itinerary", json=preferences)
    if response.status_code == 200:
        itinerary = response.json()
        st.write(itinerary)

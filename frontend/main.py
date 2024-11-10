import streamlit as st
import requests

# Function to handle signup
def signup():
    st.subheader("Signup")
    username = st.text_input("Username", key="signup_username")
    password = st.text_input("Password", type="password", key="signup_password")
    
    if st.button("Signup"):
        signup_data = {"username": username, "password": password}
        response = requests.post("http://localhost:8000/signup", json=signup_data)
        if response.status_code == 200:
            st.success("Signup successful! Please log in.")
        else:
            st.error(response.json().get("detail"))

# Function to handle login
def login():
    st.subheader("Login")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    
    if st.button("Login"):
        login_data = {"username": username, "password": password}
        response = requests.post("http://localhost:8000/login", json=login_data)
        if response.status_code == 200:
            st.session_state.logged_in = True  # Set the session state flag to True
            st.session_state.username = username  # Optionally store the username
            st.success("Login successful!")
        else:
            st.error(response.json().get("detail"))

# Option to navigate to login or signup page
def show_navigation():
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        choice = st.radio("Select an option", ("Login", "Signup"))
        
        if choice == "Signup":
            signup()
        elif choice == "Login":
            login()
    else:
        # If logged in, show the main app
        st.title("One-Day Tour Planning Assistant")

        # Collect user input
        city = st.text_input("Enter the city you want to visit:")
        start_time = st.text_input("Enter the start time of your trip:")
        end_time = st.text_input("Enter the end time of your trip:")
        budget = st.number_input("Enter your budget for the day in USD $:", min_value=0.0)
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

# Run the navigation logic
show_navigation()


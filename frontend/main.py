import streamlit as st
import requests

# Define the Streamlit app
st.title("One-Day Tour Planning Assistant")

# Check if the user is logged in
if "username" not in st.session_state:
    login_option = st.selectbox("Login or Signup", ["Login", "Signup"])

    if login_option == "Signup":
        # Signup form
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")
        if st.button("Signup"):
            response = requests.post("http://localhost:8000/signup", json={
                "username": username,
                "password": password,
                "email": email
            })
            st.write(response.json().get("message"))

    elif login_option == "Login":
        # Login form
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            response = requests.post("http://localhost:8000/login", json={
                "username": username,
                "password": password
            })
            if response.status_code == 200:
                # Store session state
                st.session_state["username"] = username
                st.write("Login successful!")
            else:
                st.write("Invalid credentials")
else:
    # If the user is logged in
    st.write(f"Welcome, {st.session_state['username']}!")
    
    # Collect user preferences for itinerary generation
    city = st.text_input("Enter the city you want to visit:")
    start_time = st.text_input("Enter the start time of your trip:")
    end_time = st.text_input("Enter the end time of your trip:")
    budget = st.number_input("Enter your budget for the day in USD $:", min_value=0.0)
    interests = st.multiselect("Select your interests:", ["Culture", "Adventure", "Food", "Shopping"])

    if st.button("Generate Itinerary"):
        # Send preferences to the backend API
        preferences = {
            "city": city,
            "start_time": start_time,
            "end_time": end_time,
            "budget": budget,
            "interests": interests
        }
        # Send both username and preferences as the payload
        response = requests.post("http://localhost:8000/generate_itinerary", json={
            "username": st.session_state["username"],  # Include the username
            "preferences": preferences  # Include the preferences
        })
        
        if response.status_code == 200:
            itinerary = response.json()
            st.write(itinerary)
        else:
            st.write(f"Error: {response.status_code} - {response.text}")
        # response = requests.post("http://localhost:8000/generate_itinerary", json=preferences)
        
        # if response.status_code == 200:
        #     itinerary = response.json()
        #     st.write(itinerary)




# import streamlit as st
# import requests

# # Define the Streamlit app
# st.title("One-Day Tour Planning Assistant")

# if "username" not in st.session_state:
#     login_option = st.selectbox("Login or Signup", ["Login", "Signup"])

#     if login_option == "Signup":
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         email = st.text_input("Email")
#         if st.button("Signup"):
#             response = requests.post("http://localhost:8000/signup", json={
#                 "username": username,
#                 "password": password,
#                 "email": email
#             })
#             st.write(response.json().get("message"))

#     elif login_option == "Login":
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         if st.button("Login"):
#             response = requests.post("http://localhost:8000/login", json={
#                 "username": username,
#                 "password": password
#             })
#             if response.status_code == 200:
#                 st.session_state["username"] = username
#                 st.write("Login successful!")
#             else:
#                 st.write("Invalid credentials")
# else:
#     st.write(f"Welcome, {st.session_state['username']}!")
    
#     # Collect user input
#     city = st.text_input("Enter the city you want to visit:")
#     start_time = st.text_input("Enter the start time of your trip:")
#     end_time = st.text_input("Enter the end time of your trip:")
#     budget = st.number_input("Enter your budget for the day:", min_value=0.0)
#     interests = st.multiselect("Select your interests:", ["Culture", "Adventure", "Food", "Shopping"])

#     if st.button("Generate Itinerary"):
#         # Send user preferences to backend API
#         preferences = {
#             "city": city,
#             "start_time": start_time,
#             "end_time": end_time,
#             "budget": budget,
#             "interests": interests
#         }
#         response = requests.post("http://localhost:8000/generate_itinerary", json=preferences)
#         if response.status_code == 200:
#             itinerary = response.json()
#             st.write(itinerary)

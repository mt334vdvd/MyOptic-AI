import streamlit as st
from PIL import Image
import requests

# Set page configuration
st.set_page_config(page_title="Myoptic AI", page_icon="🤖", layout="centered")

# Custom styling
st.markdown("""
    <style>
        body {
            background-color: #ffffff;
            color: #0033cc;
        }
        .stButton>button {
            background-color: #0033cc !important;
            color: white !important;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stTextInput>div>div>input {
            border: 2px solid #0033cc !important;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Enter Data Manually", "Upload Retinal Scans", "Chatbot"])

# Home Page
if page == "Home":
    st.title("Welcome to Myoptic AI")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Enter Data Manually"):
            st.session_state.page = "Enter Data Manually"
            st.rerun()
    with col2:
        if st.button("Upload Retinal Scans"):
            st.session_state.page = "Upload Retinal Scans"
            st.rerun()
    with col3:
        if st.button("Chatbot"):
            st.session_state.page = "Chatbot"
            st.rerun()
    st.markdown("---")
    st.subheader("About Us")
    st.write("Let's connect and improve eye health with AI!")

# Enter Data Manually Page
elif page == "Enter Data Manually":
    st.title("Enter Data Manually")
    param1 = st.text_input("Parameter 1")
    param2 = st.text_input("Parameter 2")
    param3 = st.text_input("Parameter 3")
    param4 = st.text_input("Parameter 4")
    if st.button("Get Results"):
        st.success("Results processed successfully!")

# Upload Retinal Scans Page
elif page == "Upload Retinal Scans":
    st.title("Upload Retinal Scans and Images")
    uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Retinal Scan", use_column_width=True)
        st.success("Image uploaded successfully!")

# Chatbot Page
elif page == "Chatbot":
    st.title("Myoptic AI Chatbot")
    st.write("Hi, This is Myoptic AI chatbot. What issue are you facing?")

    # Initialize session state for chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    for chat in st.session_state.chat_history:
        with st.chat_message("user"):
            st.markdown(chat["user"])
        with st.chat_message("assistant"):
            st.markdown(chat["bot"])

    # User input
    user_input = st.text_input("Type your message here:")
    
    if st.button("Send") and user_input.strip():
        try:
            # Send request to Flask chatbot
            api_url = "http://127.0.0.1:5000/chat"  # Ensure Flask server is running
            response = requests.post(api_url, json={"message": user_input})

            if response.status_code == 200:
                bot_reply = response.json().get("reply", "No response received.")
            else:
                bot_reply = "Error: Unable to connect to chatbot."

            # Save conversation history
            st.session_state.chat_history.append({"user": user_input, "bot": bot_reply})

            # Refresh chat display
            st.rerun()

        except Exception as e:
            st.error(f"An error occurred: {e}")


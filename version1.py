import streamlit as st
import streamlit.components.v1 as components

# Set page config
st.set_page_config(page_title='MyOptic AI', layout='wide')

# Apply custom CSS for styling
st.markdown(
    """
    <style>
        .stButton>button {
            background-color: #9370DB;
            color: white;
            border-radius: 10px;
            width: 100%;
            height: 50px;
            font-size: 16px;
        }
        .stFileUploader div div { 
            background-color: #2D2D2D;
            color: white;
            text-align: center;
            border-radius: 10px;
            padding: 10px;
        }
        .stTextInput>div>div>input {
            background-color: white;
            color: black;
            border-radius: 5px;
        }
        .help-desk {
            background-color: #D3D3D3;
            padding: 20px;
            border-radius: 10px;
        }
        .home-page {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
        }
        .logo-container {
            text-align: center;
            padding: 10px;
            background-color: white;
            width: 100%;
        }
        .about-us {
            position: absolute;
            bottom: 0;
            width: 100%;
            padding: 10px;
            background-color: white;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation
st.sidebar.title("Go to -")
page = st.sidebar.selectbox("", ["Home", "Enter Report Data", "Upload Retinal Scans", "AI Chatbot", "Help Desk"], key='page_selector')

if page == "Home":
    st.markdown("""<div class='logo-container'>""", unsafe_allow_html=True)
    st.image("My O ptic AI.png", use_container_width=True)
    st.markdown("""</div>""", unsafe_allow_html=True)
    
    st.markdown("""<div class='home-page'>""", unsafe_allow_html=True)
    st.title("Welcome to MyOptic AI!")
    st.write("We care about your vision.")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Enter your report data manually"):
            st.session_state['page_selector'] = "Enter Report Data"
    with col2:
        if st.button("Upload retinal scans"):
            st.session_state['page_selector'] = "Upload Retinal Scans"
    with col3:
        if st.button("Use AI Chatbot"):
            st.session_state['page_selector'] = "AI Chatbot"
    st.markdown("""</div>""", unsafe_allow_html=True)
    
    st.markdown("""<div class='about-us'>""", unsafe_allow_html=True)
    st.write("About Us | Connect with us at business.mahiytg@gmail.com")
    st.markdown("""</div>""", unsafe_allow_html=True)

elif page == "Enter Report Data":
    st.title("Please enter your report data here")
    param1 = st.text_input("Parameter 1")
    param2 = st.text_input("Parameter 2")
    param3 = st.text_input("Parameter 3")
    if st.button("Results"):
        st.success("Processing your data...")

elif page == "Upload Retinal Scans":
    st.title("Upload your retinal scans here!")
    uploaded_files = st.file_uploader("Choose files", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
    if uploaded_files:
        for uploaded_file in uploaded_files:
            st.image(uploaded_file, caption=f"Uploaded Scan: {uploaded_file.name}", use_container_width=True)
        st.success("Files uploaded successfully!")

elif page == "AI Chatbot":
    st.title("Myoptic AI ChatBot")
    user_input = st.text_input("Ask something about your eye health:")
    if user_input:
        st.write(f"AI Response: Your query about '{user_input}' is being processed...")

elif page == "Help Desk":
    st.markdown("""<div class='help-desk'>""", unsafe_allow_html=True)
    st.title("HELP DESK")
    st.write("Hi there! To get your queries solved, please contact us at - business.mahiytg@gmail.com")
    st.markdown("""</div>""", unsafe_allow_html=True)

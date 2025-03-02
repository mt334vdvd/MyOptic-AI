import streamlit as st


st.sidebar.title("Myoptic AI")
page = st.sidebar.radio("Navigation", [
    "Home", "Enter Data Manually", "Upload Retinal Scans", "Chatbot"
] )

if page == "Home":
    st.title("Welcome to Myoptic AI")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Enter Data Manually"):
            st.experimental_set_query_params(page="Enter Data Manually")
    with col2:
        if st.button("Upload Retinal Scans"):
            st.experimental_set_query_params(page="Upload Retinal Scans")
    with col3:
        if st.button("Chatbot"):
            st.experimental_set_query_params(page="Chatbot")
    
    st.subheader("About Us")
    st.write("Let's connect!")

elif page == "Enter Data Manually":
    st.title("Enter Data Manually")
    param1 = st.text_input("Parameter 1:")
    param2 = st.text_input("Parameter 2:")
    param3 = st.text_input("Parameter 3:")
    param4 = st.text_input("Parameter 4:")
    if st.button("Results"):
        st.write("Processing Data...")

elif page == "Upload Retinal Scans":
    st.title("Upload Retinal Scans and Images")
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

elif page == "Chatbot":
    st.title("Myoptic AI Chatbot")
    st.write("Hi, this is Myoptic AI chatbot. What issue are you facing?")
    user_input = st.text_area("Type your message here:")
    if st.button("Send"):
        st.write("Processing your query...")



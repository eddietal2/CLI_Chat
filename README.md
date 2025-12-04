Llama Chat

💬 A Simple and Efficient Chat Interface Powered by Llama Models

Welcome to Llama Chat! This repository hosts a minimal and easy-to-use chat application that leverages the power of the Llama family of large language models. The goal is to provide a straightforward setup for experimentation, deployment, and interaction with Llama models in a conversational format.

✨ Features

Llama Model Integration: Easily connect to local or hosted Llama model endpoints (e.g., via Hugging Face, Ollama, or a custom API).

Conversational Memory: Maintains chat history within the session to enable context-aware responses.

Markdown Rendering: Displays model responses with proper formatting (e.g., code blocks, lists, bold text).

Simple Interface: A clean, minimalist user interface designed for focused interaction.

Easy Configuration: Quick setup to swap out different Llama variants or adjust generation parameters.

⚙️ Prerequisites

Before you begin, ensure you have the following installed:

Python (3.9+): The core language used for the backend logic and model interaction.

Pip: Python package installer (usually included with Python).

A Llama Endpoint/API: Access to a running Llama model (e.g., using Ollama, VLLM, or a cloud provider's API key).

🚀 Installation

Follow these steps to get your local instance of Llama Chat running.

1. Clone the Repository

git clone [https://github.com/eddietal2/llama_chat.git](https://github.com/eddietal2/llama_chat.git)
cd llama_chat


2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies:

# Create the environment (Linux/macOS)
python3 -m venv venv

# Activate the environment (Linux/macOS)
source venv/bin/activate

# Activate the environment (Windows)
.\venv\Scripts\activate


3. Install Dependencies

Install the necessary Python packages. This project typically uses libraries like streamlit or flask for the front end and llama-cpp-python or requests for the model interaction.

pip install -r requirements.txt


4. Configuration

You must set your Llama model API endpoint or configuration variables.

Create a file named .env in the root directory.

Add your model configuration details. If using an external API, it might look like this:

# Example for an external API
LLAMA_API_URL="http://localhost:8000/v1/chat/completions"
# Or, if using an API Key
# API_KEY="your-secret-key-here"


If running a local model, check the documentation for how to specify the model path or name.

🛠️ Usage

Running the Chat Application

Assuming the application uses Streamlit for its interface (a common choice for quick Python ML demos):

streamlit run app.py


If it uses a Flask/FastAPI backend:

# Example: using uvicorn for FastAPI
uvicorn main:app --reload


The application will typically open in your web browser at http://localhost:8501 (for Streamlit) or http://127.0.0.1:8000 (for FastAPI).

Interacting with the Model

Type your message into the input box.

Press Enter or click the Send button.

The Llama model will process your query and stream its response back into the chat window.

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

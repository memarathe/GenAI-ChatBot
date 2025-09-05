
import gradio as gr
"""
This script provides a simple Gradio-based web interface for interacting with a locally hosted Tinyllama language model via the Ollama API.
Modules:
    - gradio: Used to build the web UI for user interaction.
    - dotenv: Loads environment variables from a .env file.
    - ollama: Handles model management and chat interactions with Tinyllama.
Workflow:
    1. Loads environment variables for configuration.
    2. Pulls the Tinyllama model locally using Ollama.
    3. Defines a function `handle_user_input` to send user prompts to the Tinyllama model and retrieve responses.
    4. Builds a Gradio interface with a textbox for user input and a non-editable textbox for model responses.
    5. Launches the Gradio interface when the script is run directly.
Functions:
    - handle_user_input(user_prompt): Sends the user's prompt to the Tinyllama model and returns the generated response.
    - build_ui(): Constructs and returns the Gradio interface for user interaction.
Usage:
    Run the script to start a local web server where users can enter prompts and receive AI-generated responses from Tinyllama.
"""
import dotenv
dotenv.load_dotenv()
import ollama

# Pull the model locally before using it
ollama.pull('Tinyllama')
def handle_user_input(user_prompt):
    llm = 'Tinyllama'
    response = ollama.chat(model = llm, messages=[
        {"role": "system", "content":""},
        {"role": "user", "content": user_prompt}
    ])
    return response["message"]["content"]

def build_ui():
    interface = gr.Interface(
        fn = handle_user_input,
        inputs = gr.Textbox(lines=4, placeholder="Enter your prompt here..."),
        outputs = gr.Textbox(lines=5, label="Response", interactive=False),
        title = "AI innovation test"
    )
    return interface

if __name__ == "__main__":
    interface = build_ui()
    interface.launch()
    

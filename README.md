# ChatGPT Python Chatbot

This is a simple Python chat application that uses the OpenAI GPT-3 model (ChatGPT) to have text-based conversations with users. You can use this application to create a chatbot that can answer questions, engage in conversations, or provide information.

## Prerequisites

Before using this chatbot application, make sure you have the following prerequisites:

- Python 3.6 or higher installed on your system.
- An OpenAI API key. You can sign up for an API key at [OpenAI](https://beta.openai.com/signup/).

## Installation

Follow these steps to install and set up the ChatGPT Python chatbot:

1. Clone this repository to your local machine:
    
    `git clone https://github.com/itzreqle/chatgpt_python_bot.git`
    
2. Navigate to the project directory:
    
    `cd chatgpt_python_bot`
    
3. Install the required Python packages using pip:
    
    `pip install openai`
    
4. Open the `main.py` file in a text editor of your choice.
    
5. Replace `'YOUR_API_KEY'` with your actual OpenAI API key in the `api_key` variable.
    

## Usage

To use the ChatGPT Python chatbot, follow these steps:

1. Open a terminal window and navigate to the project directory:
    
    `cd chatgpt_python_bot`
    
2. Run the chatbot script:
    
    `python main.py`
    
You will see a message indicating that the chatbot is ready: "ChatGPT: Hello! How can I assist you today?"
    
Type your questions or statements as input and press Enter.
    
The chatbot will generate responses based on your input and display them in the terminal.
    
3. To exit the chatbot, simply type "exit" and press Enter. The chatbot will respond with "ChatGPT: Goodbye!" and close.
    

## Customization

You can customize the behavior of the chatbot by modifying the `chat_with_gpt` function in the `main.py` file. You can change the `max_tokens` parameter, adjust the prompts, or add more sophisticated conversation management logic.

## License

This chatbot application is provided under the MIT License. You can find the license details in the [LICENSE](https://chat.openai.com/c/LICENSE) file.

## Acknowledgments

This application is built using the OpenAI GPT-3 model. Special thanks to OpenAI for providing access to their API.

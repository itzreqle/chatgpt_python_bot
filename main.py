import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = 'YOUR_API_KEY'

# Initialize the OpenAI API client
openai.api_key = api_key


# Function to interact with the ChatGPT model
def chat_with_gpt(prompt):
    try:
        # Generate a response from ChatGPT
        response = openai.Completion.create(
            engine="text-davinci-002",  # Choose the GPT-3 engine
            prompt=prompt,
            max_tokens=50,  # Adjust the maximum length of the response as needed
        )

        return response.choices[0].text.strip()
    except Exception as e:
        # Handle any errors that may occur
        return str(e)


# Main program loop
if __name__ == "__main__":
    print("ChatGPT: Hello! How can I assist you today?")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ("exit", "bye"):
            print("ChatGPT: Goodbye!")
            break

        # Get a response from ChatGPT
        response = chat_with_gpt(user_input)

        # Display the response from ChatGPT
        print("ChatGPT:", response)
def chatbot_response(user_message):
    """Returns a response based on user input."""
    responses = {
        "hello": "Hi there! How can I help you?",
        "bye": "Goodbye! Have a great day!",
        "how are you": "I'm just a bot, but I'm doing great! Thank you!"
    }
    return responses.get(user_message.lower(), "Sorry, I didn't understand that.")

# Real-world example:
user_input = "bye"
print("Bot:", chatbot_response(user_input))

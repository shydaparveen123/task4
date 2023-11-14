import random

def get_response(user_input):
    responses = {
        'hello': ['Hi there!', 'Hello!', 'Hey!', 'Greetings!'],
        'how are you': ['I\'m good, thanks!', 'Doing well, how about you?', 'Not bad, and you?'],
        'bye': ['Goodbye!', 'See you later!', 'Bye!', 'Have a great day!'],
        'default': ['I am not sure how to respond to that.', 'Could you please rephrase?', 'I didn\'t understand.']
    }

    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return random.choice(responses['default'])

def chat_bot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input('You: ')
        
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day.")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat_bot()

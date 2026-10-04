import re
print("🤖 Hello! I am RuleBot.")
print("I am a simple rule-based chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    # Convert the message into words
    words = re.findall(r'\b\w+\b', user_input)

    # Greetings
    if any(word in words for word in ["hello", "hi", "hey"]):
        print("Bot: Hello! Nice to meet you.")

    # How are you
    elif "how are you" in user_input or "how do you feel" in user_input:
        print("Bot: I am doing great! Thank you.")

    # Name
    elif "your name" in user_input or "who are you" in user_input:
        print("Bot: My name is RuleBot.")

    # Creator
    elif "who created you" in user_input or "who made you" in user_input:
        print("Bot: I was created using Python.")

    # Purpose
    elif "what can you do" in user_input or "your purpose" in user_input:
        print("Bot: I answer simple questions using predefined rules.")

    # Python
    elif "what is python" in user_input:
        print("Bot: Python is a popular programming language.")

    # AI
    elif "what is ai" in user_input or "what is artificial intelligence" in user_input:
        print("Bot: AI stands for Artificial Intelligence. It allows computers to perform tasks that normally require human intelligence.")

    # Chatbot
    elif "what is a chatbot" in user_input or "what is chatbot" in user_input:
        print("Bot: A chatbot is a computer program that communicates with users.")

    # Rule-based chatbot
    elif "what is rule based" in user_input or "what is rule based chatbot" in user_input:
        print("Bot: A rule-based chatbot uses predefined rules to identify user inputs and provide suitable responses.")

    # Programming
    elif "what is programming" in user_input:
        print("Bot: Programming means writing instructions that tell a computer what to do.")

    # Project
    elif "what is this project" in user_input or "tell me about this project" in user_input:
        print("Bot: This is a rule-based chatbot project built using Python. It uses predefined rules and pattern matching to respond to user inputs.")

    # Help
    elif "help" in words:
        print("Bot: You can ask me about Python, AI, chatbots, programming, or this project.")

    # Thanks
    elif "thank you" in user_input or "thanks" in words:
        print("Bot: You're welcome!")

    # Good morning
    elif "good morning" in user_input:
        print("Bot: Good morning! Have a great day.")

    # Good night
    elif "good night" in user_input:
        print("Bot: Good night! Sleep well.")

    # Exit
    elif any(word in words for word in ["bye", "goodbye"]):
        print("Bot: Goodbye! Have a nice day!")
        break

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that yet.")
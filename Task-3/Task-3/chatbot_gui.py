import tkinter as tk
from tkinter import scrolledtext
import re
def get_response(user_input):
    user_input = user_input.lower().strip()

    # Convert input into individual words
    words = re.findall(r'\b\w+\b', user_input)

    # Greetings
    if any(word in words for word in ["hello", "hi", "hey"]):
        return "Hello! Nice to meet you."

    # How are you
    elif "how are you" in user_input or "how do you feel" in user_input:
        return "I am doing great! Thank you."

    # Name
    elif "your name" in user_input or "who are you" in user_input:
        return "My name is RuleBot."

    # Creator
    elif "who created you" in user_input or "who made you" in user_input:
        return "I was created using Python."

    # Purpose
    elif "what can you do" in user_input or "your purpose" in user_input:
        return "I answer simple questions using predefined rules."

    # Python
    elif "what is python" in user_input:
        return "Python is a popular programming language."

    # AI
    elif "what is ai" in user_input or "what is artificial intelligence" in user_input:
        return "AI stands for Artificial Intelligence. It allows computers to perform tasks that normally require human intelligence."

    # Chatbot
    elif "what is a chatbot" in user_input or "what is chatbot" in user_input:
        return "A chatbot is a computer program that communicates with users."

    # Rule-based chatbot
    elif "what is rule based" in user_input or "what is rule based chatbot" in user_input:
        return "A rule-based chatbot uses predefined rules to identify user inputs and provide suitable responses."

    # Programming
    elif "what is programming" in user_input:
        return "Programming means writing instructions that tell a computer what to do."

    # Project
    elif "what is this project" in user_input or "tell me about this project" in user_input:
        return "This is a rule-based chatbot project built using Python. It uses predefined rules and pattern matching to respond to user inputs."

    # Help
    elif "help" in words:
        return "You can ask me about Python, AI, chatbots, programming, or this project."

    # Thanks
    elif "thank you" in user_input or "thanks" in words:
        return "You're welcome!"

    # Good morning
    elif "good morning" in user_input:
        return "Good morning! Have a great day."

    # Good afternoon
    elif "good afternoon" in user_input:
        return "Good afternoon! How can I help you?"

    # Good evening
    elif "good evening" in user_input:
        return "Good evening! How can I help you?"

    # Good night
    elif "good night" in user_input:
        return "Good night! Sleep well."

    # Exit
    elif any(word in words for word in ["bye", "goodbye"]):
        return "Goodbye! Have a nice day!"

    # Unknown input
    else:
        return "Sorry, I don't understand that yet."
def send_message(event=None):
    user_input = entry.get().strip()

    if user_input == "":
        return

    chat_area.insert(tk.END, "You: " + user_input + "\n")

    response = get_response(user_input)

    chat_area.insert(tk.END, "Bot: " + response + "\n\n")

    entry.delete(0, tk.END)
    chat_area.see(tk.END)
def clear_chat():
    chat_area.delete("1.0", tk.END)
    chat_area.insert(
        tk.END,
        "Bot: Hello! I am RuleBot. How can I help you?\n\n"
    )
def exit_chat():
    window.destroy()
window = tk.Tk()

window.title("Rule-Based Chatbot")
window.geometry("650x550")
title = tk.Label(
    window,
    text="🤖 RuleBot - Rule-Based Chatbot",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)

chat_area = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    width=75,
    height=22,
    font=("Arial", 11)
)

chat_area.pack(padx=10, pady=10)


# Welcome message

chat_area.insert(
    tk.END,
    "Bot: Hello! I am RuleBot. How can I help you?\n\n"
)
input_frame = tk.Frame(window)
input_frame.pack(pady=5)
entry = tk.Entry(
    input_frame,
    width=50,
    font=("Arial", 11)
)

entry.pack(side=tk.LEFT, padx=5)
send_button = tk.Button(
    input_frame,
    text="Send",
    command=send_message,
    width=10
)

send_button.pack(side=tk.LEFT)
button_frame = tk.Frame(window)
button_frame.pack(pady=10)
clear_button = tk.Button(
    button_frame,
    text="Clear Chat",
    command=clear_chat,
    width=12
)
clear_button.pack(side=tk.LEFT, padx=5)
exit_button = tk.Button(
    button_frame,
    text="Exit",
    command=exit_chat,
    width=12
)
exit_button.pack(side=tk.LEFT, padx=5)
entry.bind("<Return>", send_message)
window.mainloop()
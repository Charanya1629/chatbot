# chatbot.py
"""
Simple rule-based chatbot (Task 8).
- Uses keyword matching (if-elif style logic)
- Easy to extend: add keywords/responses to INTENTS
"""

import random
import sys

# INTENTS: each intent has keywords (phrases to look for) and possible responses
INTENTS = {
    "greeting": {
        "keywords": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": [
            "Hi there! How can I help you today?",
            "Hello! What would you like to do?",
            "Hey! Need any help?"
        ],
    },
    "how_are_you": {
        "keywords": ["how are you", "how r u", "how are you doing"],
        "responses": [
            "I'm a simple bot — always ready to help :)",
            "Doing fine! How about you?"
        ],
    },
    "thanks": {
        "keywords": ["thank you", "thanks", "thx"],
        "responses": ["You're welcome!", "No problem!", "Happy to help!"]
    },
    "bye": {
        "keywords": ["bye", "goodbye", "see you", "exit"],
        "responses": ["Goodbye! Have a great day!", "See you later!"]
    },
    "help": {
        "keywords": ["help", "what can you do", "commands"],
        "responses": [
            "I can greet you, answer simple questions, and exit on 'bye'. Try: hi, how are you, thanks, bye"
        ]
    }
}

def clean_text(text: str) -> str:
    """Lowercase and trim the input to make matching easier."""
    return text.lower().strip()

def find_intent(user_text: str):
    """
    Find an intent by checking whether any intent keyword appears in user_text.
    Returns the intent key or None if no intent matched.
    """
    text = clean_text(user_text)
    for intent, data in INTENTS.items():
        for kw in data["keywords"]:
            # simple containment check: 'how are you' in 'hi how are you?'
            if kw in text:
                return intent
    return None

def respond_to(user_text: str):
    """Get a response string (or fallback) based on matched intent."""
    intent = find_intent(user_text)
    if intent:
        return random.choice(INTENTS[intent]["responses"])
    # fallback: no matching intent
    return "Sorry, I don't understand that. Try 'help' to see commands."

def main():
    print("Welcome to Task-8 Chatbot (type 'bye' to exit).")
    while True:
        try:
            user = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            break

        if not user.strip():
            print("Bot: Please type something.")
            continue

        answer = respond_to(user)
        print("Bot:", answer)

        # If user said 'bye' or intent == 'bye', exit
        if find_intent(user) == "bye":
            break

if __name__ == "__main__":
    main()

import datetime
import random
import re

class Chatbot:
    def __init__(self):
        self.context = {"greeted": False}
        self.jokes = [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "Why did the math book look sad? Because it had too many problems.",
            "Why was the computer cold? Because it left its Windows open!"
        ]

    def get_response(self, user_input):
        user_input = user_input.lower()

        # Greeting detection
        if re.search(r"\b(hello|hi|hey|greetings)\b", user_input):
            self.context["greeted"] = True
            return "Hello! How can I help you today?"

        # Asking bot's name
        if re.search(r"\b(your name|who are you)\b", user_input):
            return "I am Chatty, your friendly Python chatbot."

        # Asking about wellbeing
        if re.search(r"\b(how are you|how's it going)\b", user_input):
            return "I'm good, thanks! How about you?"

        # Asking what bot can do
        if re.search(r"\b(what can you do|help|abilities)\b", user_input):
            return "I can chat, tell jokes, answer simple questions, and do basic math."

        # Asking time
        if re.search(r"\b(time|current time|clock)\b", user_input):
            now = datetime.datetime.now().strftime("%H:%M:%S")
            return f"The current time is {now}"

        # Tell joke
        if re.search(r"\b(joke|funny)\b", user_input):
            return random.choice(self.jokes)

        # Simple math detection
        if re.search(r"[\d\s\+\-\*\/\.\(\)]", user_input):
            try:
                result = eval(user_input, {"__builtins__": None}, {})
                return f"The answer is {result}"
            except:
                return "Sorry, I couldn't solve that math problem."

        # Goodbye
        if re.search(r"\b(bye|exit|quit|goodbye)\b", user_input):
            return "Goodbye! It was nice chatting with you."

        if self.context["greeted"]:
            return "You said: " + user_input + ". Can you tell me more?"

        return "Sorry, I didn't understand that. Can you rephrase?"

if __name__ == "__main__":
    bot = Chatbot()
    print("Welcome to Chatty! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if re.search(r"\b(exit|quit|bye|goodbye)\b", user_input.lower()):
            print("Bot: Goodbye! Have a great day!")
            break
        response = bot.get_response(user_input)
        print("Bot:", response)

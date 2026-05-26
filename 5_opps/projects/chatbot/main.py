class Chatbot:
    def __init__(self, name):
        self.name = name
        self.intents = {
            "hi": "Hello there!",
            "hello": "Hi! How can I help you today?",
            "how are you": "I'm just a bunch of code, but thanks for asking!",
            "bye": "Goodbye! Have a great day.",
            "your name": f"My name is {self.name}."
        }

    def respond(self, message):
        message = message.lower().strip()
        for question in self.intents:
            if question == message:
                return self.intents[question]
        return "Sorry, I didn't understand that."

    def run(self):
        print(f"Hello! I am {self.name}. Type 'exit' to close.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print(f"{self.name}: See you later!")
                break
            response = self.respond(user_input)
            print(f"{self.name}: {response}")


# Create chatbot object
bot = Chatbot("Jarvis")

# Start chatbot
bot.run()

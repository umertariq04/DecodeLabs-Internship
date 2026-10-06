# app.py
# This is the PYTHON SERVER. It does all the thinking.
# The webpage (index.html) just sends it messages and shows the replies.

from flask import Flask, render_template, request, jsonify
import random
import datetime
import re  # Lets us find patterns of text, like "12 + 5".

app = Flask(__name__)

# This is our knowledge base, same as in chatbot.py.
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What's on your mind?",
    "hey": "Hey! Good to see you.",
    "how are you": "I'm just a program, but I'm running smoothly! How about you?",
    "i am fine": "Glad to hear that!",
    "i am good": "That's great to hear!",
    "i am sad": "I'm sorry to hear that. I hope things get better soon.",
    "i am bored": "Try asking me for a joke!",
    "what is your name": "I'm MyChatbot, a rule-based chatbot.",
    "who made you": "I was built as a DecodeLabs internship project.",
    "are you a robot": "Yes, I'm a chatbot that follows rules written by a developer.",
    "what can you do": "I can chat, tell jokes, tell the time, and do simple math.",
    "help": "Try: hello, what is your name, tell me a joke, what time is it, or a math problem like 12 + 5.",
    "thank you": "You're welcome!",
    "thanks": "Anytime!",
    "sorry": "No worries at all!",
    "what is ai": "AI is when computers do tasks that normally need human thinking.",
    "what is python": "Python is a beginner-friendly programming language.",
    "what is a chatbot": "A chatbot is a program that talks with people through text.",
    "bye": "Goodbye! Have a great day.",
}

# A list of jokes. We will pick one at random.
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the computer go to therapy? It had too many unresolved issues.",
    "Why was the computer cold? It left its Windows open.",
]

# This is the "shape" of a simple math problem: a number, a symbol, a number.
# \d+ means "one or more digits". \s* means "zero or more spaces".
math_pattern = r"(\d+)\s*([\+\-\*/])\s*(\d+)"

default_reply = "I do not understand that. Could you rephrase?"


def get_bot_reply(user_text):
    # Make it lowercase and remove spaces from the start and end.
    clean_text = user_text.lower().strip()

    # Check if the user wants a joke.
    if "joke" in clean_text:
        return random.choice(jokes)

    # Check if the user is asking for the time.
    if "time" in clean_text:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return "Right now it's " + now + "."

    # Check if the message contains a simple math problem, like "12 + 5".
    math_match = re.search(math_pattern, clean_text)
    if math_match:
        # Pull out the three pieces we found: first number, symbol, second number.
        first_number = int(math_match.group(1))
        symbol = math_match.group(2)
        second_number = int(math_match.group(3))

        # Dividing by zero is impossible, so we handle that separately.
        if symbol == "/" and second_number == 0:
            return "I can't divide by zero."

        # Do the correct operation, based on which symbol was used.
        if symbol == "+":
            result = first_number + second_number
        elif symbol == "-":
            result = first_number - second_number
        elif symbol == "*":
            result = first_number * second_number
        else:
            result = first_number / second_number

        # If the answer is a whole number like 2.0, show it as 2.
        if result == int(result):
            result = int(result)

        return "That equals " + str(result) + "."

    # Go through every keyword in our responses dictionary.
    for keyword in responses:
        if keyword in clean_text:
            return responses[keyword]

    # If nothing matched, use the default reply.
    return default_reply


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    user_text = data["message"]
    reply = get_bot_reply(user_text)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
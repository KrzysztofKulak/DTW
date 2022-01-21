import random

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    welcome_messages = [
        "🐕🐕🐕  zarejestruj się i spaceruj jusz teraz!!1 🐕🐕🐕",
        "gorące 🐩🐩🐩 w twojej okolicy",
        "🐩🐩 nie bierz smaczków od nieznajomych!!! 🐕🐕",
    ]
    return random.choice(welcome_messages)

import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    welcome_messages = [
        "πππ  zarejestruj siΔ i spaceruj jusz teraz!!1 πππ",
        "gorΔce π©π©π© w twojej okolicy",
        "π©π© nie bierz smaczkΓ³w od nieznajomych!!! ππ",
    ]
    return random.choice(welcome_messages)

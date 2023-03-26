from flask import Flask
import random

app = Flask(__name__)

QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "The best way to predict the future is to invent it. - Alan Kay",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "If you can't explain it simply, you don't understand it well enough. - Albert Einstein"
]

@app.route('/')
def random_quote():
    return random.choice(QUOTES)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

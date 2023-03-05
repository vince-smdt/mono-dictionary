import dictionary
from flask import Flask

# Flask application
app = Flask(__name__)

# Routes
@app.route("/<word>")
def word_definition(word : str):
    word_data = dictionary.fetch_word(word)

    if word_data == dictionary.INVALID_MESSAGE:
        return "<h2>Invalid word!</h2>"

    return "<p>" + str(word_data) + "</p>"

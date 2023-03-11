import dictionaryapi
from flask import Flask, request, jsonify
from flask_cors import CORS

# Flask application
app = Flask(__name__)
CORS(app)

# Routes
@app.route("/", methods=["POST"])
def word_definition():
    if request.method != "POST":
        pass # TODO - Handle wrong method
    
    # Fetch word
    word = request.form.get("word")
    word_data = dictionaryapi.fetch_word(word)
    
    # Check if word is valid
    if word_data == dictionaryapi.INVALID_MESSAGE:
        return jsonify({ "error": "Invalid word!" })

    # Return word data
    return word_data

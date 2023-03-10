import dictionary
from flask import Flask, redirect, render_template, request, url_for

# Flask application
app = Flask(__name__)

# Routes
@app.route("/", methods=["GET", "POST"])
def word_definition():
    if request.method != "POST":
        return render_template("home.html")
    
    # Fetch word
    word = request.form.get("word")
    word_data = dictionary.fetch_word(word)
    
    # Check if word is valid
    if word_data == dictionary.INVALID_MESSAGE:
        return { "error": "Invalid word!" }

    # Return word data
    return word_data

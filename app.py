import dictionary
from flask import Flask, redirect, render_template, request, url_for

# Flask application
app = Flask(__name__)

# Routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/word-submit", methods=['GET', 'POST'])
def word_submit():
    if request.method == 'POST':
        result = request.form['word']
        return redirect(url_for('word_definition', word=result))
    
    return redirect(url_for('home'))

@app.route("/<word>")
def word_definition(word : str):
    word_data = dictionary.fetch_word(word)
    
    if word_data == dictionary.INVALID_MESSAGE:
        return "<p>Invalid word!</p>"
    
    return render_template("definition.html", data=word_data)

from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import re
import os

app = Flask(__name__)
# Use SQLite for local development, PostgreSQL for production
if 'DATABASE_URL' in os.environ:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///language_learning.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

def clean_text(text):
    """Convert text to lowercase and remove punctuation & extra spaces."""
    text = text.lower().strip()  # Convert to lowercase & remove extra spaces
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    return text

@app.route("/check_answer", methods=["POST"])
def check_answer():
    data = request.json
    user_answer = clean_text(data.get("user_answer", ""))
    correct_answer = clean_text(data.get("correct_answer", ""))

    if user_answer == correct_answer:
        sentence = Sentence.query.order_by(db.func.random()).first()
        return jsonify({"status": "correct", "new_hindi": sentence.hindi, "new_answer": sentence.english})
    else:
        return jsonify({"status": "incorrect"})

# Database Model
class Sentence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hindi = db.Column(db.Text, nullable=False)
    english = db.Column(db.Text, nullable=False)

# Create DB
with app.app_context():
    db.create_all()

# # Homepage: Show All Sentences
# @app.route("/")
# def index():
#     sentences = Sentence.query.all()
#     return render_template("index.html", sentences=sentences)

# Homepage
@app.route("/")
def index():
    return render_template("index.html")

# View All Sentences
@app.route("/view-all")
def view_all():
    sentences = Sentence.query.all()
    return render_template("view_all.html", sentences=sentences)

# Add Sentence Form
@app.route("/add", methods=["GET", "POST"])
def add_sentence():
    if request.method == "POST":
        hindi = request.form["hindi"]
        english = request.form["english"]
        if hindi and english:
            new_sentence = Sentence(hindi=hindi, english=english)
            db.session.add(new_sentence)
            db.session.commit()
            return redirect(url_for("index"))
    return render_template("add_sentence.html")

# Get Random Sentence (For AJAX)
@app.route("/random")
def get_random_sentence():
    sentence = Sentence.query.order_by(db.func.random()).first()
    return jsonify({"hindi": sentence.hindi, "english": sentence.english})

@app.route("/next_sentence")
def next_sentence():
    sentence = Sentence.query.order_by(db.func.random()).first()
    return jsonify({"hindi": sentence.hindi, "english": sentence.english})

@app.route("/practice")
def practice():
    sentence = Sentence.query.order_by(db.func.random()).first()
    return render_template("practice.html", hindi=sentence.hindi, correct_english=sentence.english)


if __name__ == "__main__":
    app.run(debug=True)

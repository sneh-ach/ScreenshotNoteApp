import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import pytesseract
from PIL import ImageGrab
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
CORS(app)

def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, screenshot_name TEXT, note TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS flashcards (id INTEGER PRIMARY KEY, question TEXT, answer TEXT)")
    conn.close()

@app.route('/screenshot', methods=['GET'])
def take_screenshot():
    try:
        screenshot = ImageGrab.grab()
        screenshot.save("screenshot.png")
        return jsonify({"message": "Screenshot saved as screenshot.png"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add_note', methods=['POST'])
def add_note():
    data = request.json
    screenshot_name = data.get("screenshot_name")
    note = data.get("note")
    try:
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO notes (screenshot_name, note) VALUES (?, ?)", (screenshot_name, note))
            conn.commit()
        return jsonify({"message": "Note added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add_flashcard', methods=['POST'])
def add_flashcard():
    data = request.json
    question = data.get("question")
    answer = data.get("answer")
    try:
        with sqlite3.connect('data.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO flashcards (question, answer) VALUES (?, ?)", (question, answer))
            conn.commit()
        return jsonify({"message": "Flashcard added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/debug_code', methods=['POST'])
def debug_code():
    data = request.json
    code_snippet = data.get("code_snippet")
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Debug this code:\n{code_snippet}",
            max_tokens=150
        )
        suggestion = response.choices[0].text.strip()
        return jsonify({"suggestion": suggestion}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(port=5000, debug=True)

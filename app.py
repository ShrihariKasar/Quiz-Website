from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__, static_folder='static')

# Load questions from a JSON file
def load_questions():
    with open('questions.json', 'r') as f:
        return json.load(f)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    questions = load_questions()
    if request.method == 'POST':
        answers = request.form
        score = 0
        for q_id, answer in answers.items():
            # Extract question index from the 'question_' prefix and convert it to an integer
            question_index = int(q_id.split('_')[1])
            if answer and questions[question_index]['answer'] == answer:
                score += 1
        return redirect(url_for('result', score=score, total=len(questions)))
    return render_template('quiz.html', questions=questions)

@app.route('/result')
def result():
    score = request.args.get('score', 0, type=int)
    total = request.args.get('total', 0, type=int)
    return render_template('result.html', score=score, total=total)

if __name__ == '__main__':
    app.run(debug=True)

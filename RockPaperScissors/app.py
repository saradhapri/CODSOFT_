from flask import Flask, render_template, request, jsonify  # type: ignore
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json.get('choice')
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    return jsonify({
        'user_choice': user_choice,
        'computer_choice': computer_choice,
        'result': result
    })

def determine_winner(user, computer):
    if user == computer:
        return 'It\'s a tie!'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return 'You win!'
    else:
        return 'You lose!'

if __name__ == '__main__':
    app.run(debug=True)

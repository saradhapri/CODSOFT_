from flask import Flask, render_template, request, session 
import random
import string
from flask_session import Session 

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

def generate_password(length, complexity):
    characters = ''
    if complexity == 'low':
        characters = string.ascii_lowercase
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    strength = length >= 15 and has_lower and has_upper and has_digit and has_special
    return 'Strong' if strength else 'Weak'

@app.route('/')
def home():
    password_history = session.get('password_history', [])
    return render_template('index.html', password_history=password_history)

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    complexity = request.form['complexity']
    password = generate_password(length, complexity)
    strength = password_strength(password)
    password_history = session.get('password_history', [])
    password_history.append(password)
    session['password_history'] = password_history[-5:]  # Store only last 5 passwords
    return render_template('index.html', password=password, strength=strength, password_history=password_history)

if __name__ == '__main__':
    app.run(debug=True)

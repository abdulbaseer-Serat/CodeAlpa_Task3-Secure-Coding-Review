from flask import Flask, request, render_template, redirect, session
import sqlite3
import bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Rate limiting (5 requests per minute)
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM users WHERE username=?", (username,))
        result = cursor.fetchone()

        conn.close()

        if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
            session['user'] = username
            return redirect('/home')
        else:
            return "Login Failed ❌"

    return render_template('login.html')


@app.route('/home')
def home():
    if 'user' in session:
        return render_template('home.html')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=False)
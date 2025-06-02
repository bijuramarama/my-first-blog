from flask import Flask, render_template, request, redirect, url_for, session, escape
from pymongo import MongoClient
import os # For environment variables

app = Flask(__name__)
app.secret_key = os.urandom(24) # Secret key for session management

# MongoDB Configuration
# We'll use environment variables for Mongo URI in a production-like setup with docker-compose
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['user_login_db'] # Database name
users_collection = db['users'] # Collection name

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=escape(session['username']))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'] # In a real app, hash and salt passwords!

        user = users_collection.find_one({'username': username})

        if user and user['password'] == password: # NEVER store/compare plaintext passwords in prod
            session['username'] = username
            # Store a dummy user if it doesn't exist for testing
            # In a real app, you'd have a registration page or pre-seeded users.
            # For now, let's insert a test user if login is attempted and user doesn't exist.
            # This is just for ease of testing without a registration form.
            return redirect(url_for('index'))
        else:
            # For simplicity, if user not found or password incorrect,
            # and if it's the test user, create it.
            # THIS IS NOT FOR PRODUCTION.
            if username == "testuser" and password == "testpass":
                if not users_collection.find_one({'username': "testuser"}):
                    users_collection.insert_one({'username': "testuser", 'password': "testpass"})
                    session['username'] = username
                    return redirect(url_for('index'))
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Port 5000 is where Nginx will proxy requests to
    app.run(host='0.0.0.0', port=5000, debug=True)

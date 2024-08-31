from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This will act as a temporary storage for user data
users = {}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    email = request.form['email']
    password = request.form['password']
    
    # Here you would typically validate the login credentials
    # For demonstration purposes, we'll just store the user in a dictionary
    users[email] = password
    
    # Redirect to the home page after successful login
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/logout')
def logout():
    # Add your logout logic here
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

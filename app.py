from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/classes')
def classes():
    return render_template('classes.html')

@app.route('/assignments')
def assignments():
    return render_template('assignments.html')

@app.route('/class-tests')
def class_tests():
    return render_template('class_tests.html')

@app.route('/groups')
def groups():
    return render_template('groups.html')

if __name__ == '__main__':
    app.run(debug=True)
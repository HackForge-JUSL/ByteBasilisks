from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user credentials (replace with your actual user database)
users = {
    'user1@example.com': 'password1',
    'user2@example.com': 'password2'
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    if email in users and users[email] == password:
        return redirect(url_for('index'))
    else:
        error = 'Invalid email or password. Please try again.'
        return render_template('login.html', error=error)

@app.route('/index')
def index():
    return render_template('index.html')
  
@app.route('/physics')
def physics():
    return render_template('physics.html')

@app.route('/chemistry')
def chemistry():
    return render_template('chemistry.html')
  
@app.route('/mathematics2')
def mathematics2():
    return render_template('mathematics2.html')

@app.route('/spanish')
def spanish():
    return render_template('spanish.html')
  
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
  app.run()
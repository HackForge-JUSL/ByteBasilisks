from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)
'''
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.db'
db=SQLAlchemy(app)
class user(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=False)
    password_hash=db.Column(db.String(128), nullable = False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_passwords(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'
'''

users = {
    'user1@example.com': 'password1',
    'user2@example.com': 'password2'
}
'''
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form['username']
        password = request.form['password']
        
        existing_user = user.query.filter_by(username=username).first()
        if existing_user:
            error = 'User already exists'
            return render_template('login.html', error=error)
        
        new_user = user(username=username)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))
'''

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
def tests():
    return render_template('tests.html')

@app.route('/groups')
def groups():
    return render_template('groups.html')

if __name__ == '__main__':
  app.run()
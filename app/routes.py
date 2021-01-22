from app import app
from flask import render_template
from app.forms import LoginForm, SignupForm

@app.route('/')
@app.route('/home')
def index():
    user = {'username': 'Sameer'}
    return  render_template('index.html', title='Home', user=user)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route('/register')
def register():
    form = SignupForm()
    return render_template('register.html', title='Register', form=form)

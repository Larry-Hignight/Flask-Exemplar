from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/index')
def index():
    user = {'nickname': 'Larry'} # mocked user
    return render_template('index.html', title='Home', user=user)

@app.route('/blog')
def blog():
    user = {'nickname': 'Miguel'}  # mock user
    posts = [                      # mock posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("blog.html", title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
                           title='Sign In',
                           form=form)

@app.route('/login2', methods=['GET', 'POST'])
def login2():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)

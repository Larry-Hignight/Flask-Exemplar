from flask import render_template
from app import app

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

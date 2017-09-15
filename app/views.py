from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/blog')
def blog():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("blog.html",
                           title='Home',
                           user=user,
                           posts=posts)

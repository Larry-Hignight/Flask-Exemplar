from flask import render_template, request, jsonify, Response
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/template1')
def template1():
    user = {'nickname': 'Larry'} # mocked user
    return render_template('index.html', title='Home', user=user)

@app.route('/template2')
def template2():
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


## ---- Query Parameters ---- ##

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User ' + username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

#@app.route('/login', methods=['GET', 'POST'])
#def login():
#    if request.method == 'POST':
#        do_the_login()
#    else:
#        show_the_login_form()

@app.route('/test_json')
def test_json():
    app.logger.debug("This is a debug level log for the json resource")
    app.logger.info("Bring the info!")
    s = [1, 2, {"key": "value"}]
    return jsonify(s)


## -- Static Files -- ##

@app.route('/test_xml')
def test_xml():
    app.send_static_file('static/book.xml')

import os    
@app.route('/test_image')
def test_image():
    app.logger.error("CWD > " + os.getcwd())
    app.logger.error("/   > " + str(os.listdir()))
    app.logger.error("src > " + str(os.listdir('/src')))
    app.logger.error("app > " + str(os.listdir('/src/app')))
    app.logger.error("static > " + str(os.listdir('/src/app/static')))
    return app.send_static_file('/src/app/static/surf.jpg')

@app.route('/static')
def test_static():
    return app.send_static_file('app/static/')


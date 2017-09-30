from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config.from_object('config')
#db = SQLAlchemy(app)

db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@mysql/information_schema'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

from app import views #, models

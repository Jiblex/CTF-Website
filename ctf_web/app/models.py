from app import database, login_manager
from datetime import datetime
import os
from sqlalchemy import create_engine
from flask_login import UserMixin

# builds path to current file
basedir = os.path.abspath(os.path.dirname(__file__))

# loads user by uid 
@login_manager.user_loader
def user_load(uid):
    return User.query.get(int(uid))



# class represents a user in the database
class User(database.Model, UserMixin):
    __tablename__ = "user"
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(100), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    image = database.Column(database.String(20), nullable=False, default="default.jpg")
    password = database.Column(database.String(60), nullable=False)
    posts = database.relationship("Post", backref="author", lazy=True)

    # User object should be printed as (username, email, image)
    def __repr__(self):
        return f"User('{self.username}, {self.email}, {self.image}')"


# class represents a user post in the database
class Post(database.Model):
    __tablename__ = "post"
    id = database.Column(database.Integer, primary_key=True)
    uid = database.Column(database.Integer, database.ForeignKey("user.id"), nullable=False) 
    title = database.Column(database.String(200), nullable=False)
    date_posted = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    content = database.Column(database.String(1000), nullable=True)

    # Post object should be printed as (username, email, image)
    def __repr__(self):
        return f"Post('{self.title}, {self.date_posted}')"


# Connecting to the database and creating tables
engine = create_engine('sqlite:///' + os.path.join(basedir, 'ctf.db'))
database.metadata.create_all(engine)

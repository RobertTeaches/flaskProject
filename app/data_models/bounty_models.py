from datetime import datetime
import json
from dataclasses import dataclass
import random
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

from app import db


bounty_static_id = 0


# Classes
class Bounty(db.Model):
    id: int
    title: str
    description: str
    reward: int
    xp: int
    image_src: str
    theme: str

    id = db.Column(db.String(256), primary_key=True)
    title = db.Column(db.String(128), index=True, unique=True)
    description = db.Column(db.String(1024), index=True, unique=True)
    reward = db.Column(db.Integer)
    xp = db.Column(db.Integer)
    image_src = db.Column(db.String(256))
    theme = db.Column(db.String(30), index=True)

    def __init__(self, title="N/A", description="Empty", reward=1, xp=25, image_src="", theme=""):
        global bounty_static_id
        self.id = bounty_static_id
        bounty_static_id += 1

        self.title = title
        self.description = description
        self.reward = reward
        self.xp = xp
        self.theme = theme
        self.image_src = image_src

    def __repr__(self):
        return f"Bounty: {self.title} - {self.id}"


class BountySubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(2048))
    submission_time = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

@dataclass
class BountyTheme(db.Model):
    name: str = db.Column(db.String(30), primary_key=True, index=True)
    icon_url: str = db.Column(db.String(256))
    header_color: str = db.Column(db.String(10))
    card_color: str = db.Column(db.String(10))



class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(128), unique=True, index=True)
    first_name: str = db.Column(db.String(128), index=True)
    last_name: str = db.Column(db.String(128), index=True)
    email: str = db.Column(db.String(128), unique=True)
    password_hash: str = db.Column(db.String(256))
    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) -> bool:
        return check_password_hash(self.password_hash, password)


class Student(User):
    __tablename__ = 'student'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    nickname: str = db.Column(db.String(128), index=True)
    avatar_image: str = db.Column(db.String)
    # Yes, we are ignoring all common-sense principles for Student-Logins. Sucks to Suck to be a student with
    # no privacy
    plain_password = db.Column(db.String(64))
    bounty_submissions = db.relationship(BountySubmission, backref='author', lazy='dynamic')

    __mapper_args__ = {
        'polymorphic_identity': 'student'
    }

    def check_password(self, password) -> bool:
        return password == self.plain_password

# End Classes


# Util Methods
@login.user_loader
def load_user(_id):
    return User.query.get(int(_id))



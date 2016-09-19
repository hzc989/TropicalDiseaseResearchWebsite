from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from markdown import markdown
import bleach
from flask import current_app, request, url_for
from flask_login import UserMixin, AnonymousUserMixin
#from app.exceptions import ValidationError
from . import db, login_manager

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    truename = db.Column(db.String(64))
    role = db.Column(db.Enum('user','admin','superadmin'), default='user')
    password_hash = db.Column(db.String(128))
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    permit_login = db.Column(db.Boolean, default=True)
    paper_posts = db.relationship('Paper', backref='poster', lazy='dynamic')
    content_posts = db.relationship('Content', backref='poster', lazy='dynamic')
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Paper(db.Model):
    __tablename__ = 'papers'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    pdf_uri = db.Column(db.String(150))
    tag = db.Column(db.Enum, nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    type = db.Column(db.Enum('project_paper', 'related_paper', 'closed_paper'))
    poster_uid = db.Column(db.Integer, db.ForeignKey('users.id'))
    authors = db.Column(db.Enum, nullable=False)
    journal = db.Column(db.String(64), nullable=False)
    
    def __repr__(self):
        return '<Paper %r>' % self.name

class Content(db.Model):
    __tablename__ = 'contents'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    tag = db.Column(db.Enum, nullable=True)
    addons_uri = db.Column(db.String(150))
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    type = db.Column(db.Enum('news', 'notice', 'datatools'))
    poster_uid = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __repr__(self):
        return '<Content %r>' % self.title

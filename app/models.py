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
    
    @staticmethod
    def generate_fake(count=10,r='user'):
        from sqlalchemy.exc import IntegrityError
        from random import seed
        import forgery_py

        seed()
        for i in range(count):
            u = User(username=forgery_py.internet.user_name(True),
                     truename=forgery_py.name.full_name(),
                     role=r,
                     password=forgery_py.lorem_ipsum.word(),
                     member_since=forgery_py.date.date(True),
                     permit_login=True)
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()

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
    
    @staticmethod 
    def generate_fake(count=50,t='news'):
        from sqlalchemy.exc import IntegrityError
        from random import seed, randint
        import forgery_py

        seed()
        user_count = User.query.filter_by(role='admin').count()
        for i in range(count):
            u = User.query.filter_by(role='admin').offset(randint(0, user_count - 1)).first()
            p = Content(title=forgery_py.lorem_ipsum.title(),
                        content=forgery_py.lorem_ipsum.sentences(randint(1, 5)),
                        type=t,
                        poster=u)
            db.session.add(p)
            db.session.commit()
    
    def __repr__(self):
        return '<Content %r>' % self.title

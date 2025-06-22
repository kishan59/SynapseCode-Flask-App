from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime, timezone

# creating tables using Models (ORM)
# User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    snippets = db.relationship('Snippet', backref='user', lazy=True)

    # a friendly respresentation of User object
    def __repr__(self):
        return f"User('{self.username}')"
    

# Snippet Model
class Snippet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    code_content = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    source_url = db.Column(db.String(255), nullable=True)
    tags = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # A friendly representation of Snippet object
    def __repr__(self):
        return f"Snippet('{self.title}', '{self.language}', '{self.created_at}')"

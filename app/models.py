from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class InCom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer())
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    order_number = db.Column(db.String(140))
    product_type = db.Column(db.String(140))
    model = db.Column(db.String(140))
    cause = db.Column(db.String(140))
    detection_area = db.Column(db.String(140))
    description = db.Column(db.String(140))

    def __repr__(self):
        return f'<RW: {self.username},{self.product_type}'

# TODO na co to było?
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

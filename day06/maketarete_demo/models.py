from ext import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Interger, primary_key=True, autoincrement=True)
    username = db.Column(db.string(50), nullable=False)
    age = db.Column(db.Integer)
    height = db.Column(db.string(30), default='178cm')

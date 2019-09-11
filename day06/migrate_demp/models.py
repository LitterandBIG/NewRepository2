from ext import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Interger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Interger)
    height = db.Column(db.String(30), default='187cm')

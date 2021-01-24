from lib.db import db

class Owner(db.Model):
    __tablename__ ="owners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    pet = db.relationship('Pet', backref='owner', uselist=False)
    

    def __init__(self, name):
        self.name = name

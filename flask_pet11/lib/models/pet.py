from lib.db import db

class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))
    name = db.Column(db.String(100), nullable=False)


    def __init__(self, owner_id, name):
        self. owner_id = owner_id
        self.name = name

from lib.db import db

class Continent(db.Model):
    __tablename__ ="continents"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    code = db.Column(db.String(64), nullable=False)
    ethnicity = db.relationship('Ethnicity', backref='continent', uselist=False)


    def __init__(self, name, code):
        self.name = name
        self.code = code

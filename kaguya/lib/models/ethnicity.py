from lib.db import db

class Ethnicity(db.Model):
    __tablename__ = 'ethnicitys'
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    continent_id = db.Column(db.Integer, db.ForeignKey('continents.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(100), nullable=False)

    def __init__(self, continent_id, name, code):
        self.continent_id = continent_id
        self.name = name
        self.code = code

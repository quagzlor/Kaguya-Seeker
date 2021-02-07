from lib.db import db

class FeatureType(db.Model):
    __tablename__ ="feature_type"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    code = db.Column(db.String(64), nullable=False)

    def __init__(self, name, code):
        self.name = name
        self.code = code

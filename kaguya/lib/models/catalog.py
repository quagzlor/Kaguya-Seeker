from lib.db import db

class Catalog(db.Model):
    __tablename__ ="catalog_detail"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    pcode = db.relationship('pcode', backref='product_code', uselist=False)

    def __init__(self, pcode, name):
        self.pcode = pcode
        self.name = name

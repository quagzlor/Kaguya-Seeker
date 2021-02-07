from lib.db import db

class ProductCode(db.Model):
    __tablename__ ="product_code"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    pcode = db.Column(db.String(64), nullable=False)


    def __init__(self, name, pcode):
        self.name = name
        self.pcode = pcode
from lib.db import db

class Approval(db.Model):
    __tablename__ ="approval_status"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    def __init__(self, name):
        self.name = name
from lib.db import db

class Feature(db.Model):
    __tablename__ ="feature"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    ethnicity_id = db.relationship('ethnicity_id', backref='ethnicity', uselist=False)
    approval_status_id = db.relationship('approval_status_id', backref='approval_status', uselist=False)
    feature_type_id = db.relationship('feature_type_id', backref='feature_type', uselist=False)
    direction_id = db.relationship('direction_id', backref='direction', uselist=False)
    map_id = db.relationship('map_id', backref='map', uselist=False)

    def __init__(self, approval_status_id, feature_type_id, direction_id, map_id,  name, code):
        self.ethnicity_id = ethnicity_id
        self.approval_status_id = approval_status_id
        self.feature_type_id = feature_type_id
        self.direction_id = direction_id
        self.map_id = map_id
        self.name = name
        self.code = code
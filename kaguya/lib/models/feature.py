# from lib.db import db

# class Feature(db.Model):
#     __tablename__ ="feature"

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), nullable=False)
#     ethnicity_id = db.relationship('ethnicity_id', backref='ethnicity', uselist=False)
#     approval_status_id = db.relationship('approval_status_id', backref='approval_status', uselist=False)
#     feature_type_id = db.relationship('feature_type_id', backref='feature_type', uselist=False)
#     direction_id = db.relationship('direction_id', backref='direction', uselist=False)
#     map_id = db.relationship('map_id', backref='map', uselist=False)

#     def __init__(self, approval_status_id, feature_type_id, direction_id, map_id,  name, code):
#         self.ethnicity_id = ethnicity_id
#         self.approval_status_id = approval_status_id
#         self.feature_type_id = feature_type_id
#         self.direction_id = direction_id
#         self.map_id = map_id
#         self.name = name
#         self.code = code
from lib.db import db

class Feature(db.Model):
    __tablename__ ="features"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    latitude = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Integer, nullable=False)
    starting_latitude = db.Column(db.Integer, nullable=False)
    ending_latitude = db.Column(db.Integer, nullable=False)
    starting_longitude = db.Column(db.Integer, nullable=False)
    ending_longitude = db.Column(db.Integer, nullable=False)
    direction_id = db.Column(db.Integer, db.ForeignKey('direction.id'))
    diameter = db.Column(db.Integer, nullable=False)
    ethnicity_id = db.Column(db.Integer, db.ForeignKey('ethnicity.id'))
    quad_id = db.Column(db.Integer, db.ForeignKey('quad.id'))
    map_id = db.Column(db.Integer, db.ForeignKey('map.id'))
    approval_status_id = db.Column(db.Integer, db.ForeignKey('approval_status.id'))
    approval_date = db.Column(db.DateTime, nullable=False)
    ref = db.Column(db.Integer, nullable=False)
    reference_text = db.Column(db.String(64), nullable=False)
    feature_type_id = db.Column(db.Integer, db.ForeignKey('feature_type.id'))
    origin = db.Column(db.String(64), nullable=False)
    location = db.Column(db.String(64), nullable=False)
    circle_area = db.Column(db.Integer, nullable=False)
    square_area = db.Column(db.Integer, nullable=False)
    circle_area_mod = db.Column(db.Integer, nullable=False)

    def __init__(self, name, latitude, longitude, starting_latitude, ending_latitude, starting_longitude, ending_longitude, direction_id, diameter, ethnicity_id, quad_id, map_id, approval_status_id, approval_date, ref, reference_text, feature_type_id, origin, location, circle_area, square_area, circle_area_mod):
        name = name
        latitude = latitude
        longitude = longitude
        starting_latitude = starting_latitude
        ending_latitude = ending_latitude
        starting_longitude = starting_longitude
        ending_longitude = ending_longitude
        direction_id = direction_id
        diameter = diameter
        ethnicity_id = ethnicity_id
        quad_id = quad_id
        map_id = map_id
        approval_status_id = approval_status_id
        approval_date = approval_date
        ref = ref
        reference_text = reference_text
        feature_type_id = feature_type_id
        origin = origin
        location = location
        circle_area = circle_area
        square_area = square_area
        circle_area_mod = circle_area_mod


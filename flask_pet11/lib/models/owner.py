from lib.db import db

class Owner(db.Model):
    __tablename__ ="owners"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    pet = db.relationship('Pet', backref='owner', uselist=False)
    

    def __init__(self, name):
        self.name = name

class Approval(db.Model):
    __tablename__ ="approval_status"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

class Catalog(db.Model):
    __tablename__ ="catalog_detail"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    pcode = db.relationship('pcode', backref='product_code', uselist=False)

class Continent(db.Model):
    __tablename__ ="continent"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    code = db.Column(db.String(64), nullable=False)

class Direction(db.Model):
    __tablename__ ="direction"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

class FeatureType(db.Model):
    __tablename__ ="feature_type"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    code = db.Column(db.String(64), nullable=False)

class ProductCode(db.Model):
    __tablename__ ="product_code"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    pcode = db.Column(db.String(64), nullable=False)

class Map(db.Model):
    __tablename__ ="map"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)


class Quad(db.Model):
    __tablename__ ="quad"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

class Ethnicity(db.Model):
    __tablename__ ="ethnicity"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    code = db.Column(db.String(64), nullable=False)
    continent_id = db.relationship('continent_id', backref='continent', uselist=False)


class Feature(db.Model):
    __tablename__ ="feature"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    ethnicity_id = db.relationship('ethnicity_id', backref='ethnicity', uselist=False)
    approval_status_id = db.relationship('approval_status_id', backref='approval_status', uselist=False)
    feature_type_id = db.relationship('feature_type_id', backref='feature_type', uselist=False)
    direction_id = db.relationship('direction_id', backref='direction', uselist=False)
    map_id = db.relationship('map_id', backref='map', uselist=False)

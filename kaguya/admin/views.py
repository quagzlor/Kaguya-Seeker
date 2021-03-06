# from flask import render_template, request, redirect, url_for, flash

# from admin import app

# from lib.models import Ethnicity, Continent

# from lib.db import db

# from functools import wraps


# @app.route('/template', methods=['POST', 'GET'])
# def index():
    
#     continents = Continent.query.all()# SELECT * FROM continents;
#     ethnicitys = Ethnicity.query.all()# SELECT * FROM ethncitys;
#     return render_template("template/index.html", continents=continents, ethnicitys=ethnicitys)


# @app.route('/template/search', methods=['POST', 'GET'])
# def search():

#     continent_id = request.args.get('continent_id')
#     continent = Continent.query.get(continent_id')
#     print(Continent)
#     ethnicitys = Ethnicity.query.filter(Ethnicity.id == continent_id).order_by(Ethnicity.id).all()
   
#     return render_template('template/search.html', ethnicitys=ethnicitys, continent_id = continent_id, continent = continent)

from flask import render_template, request, redirect, url_for, flash, jsonify, json

from admin import app

from lib.models import Ethnicity, Continent

from lib.db import db

from functools import wraps

from wtforms import SelectField

from flask_wtf import FlaskForm


class Form(FlaskForm):
    continent = SelectField('continent', choices=[])
    ethnicity = SelectField('ethnicity', choices=[])
    feature = SelectField('feature', choices=[])

@app.route('/template', methods=['GET', 'POST'])
def index():
    form = Form()
    form.continent.choices = [(continent.id, continent.name) for continent in Continent.query.all()]

    if request.method == 'POST':
       #feature =  Feature.query.filter_by(id=form.feature.data).first()
       continent = Continent.query.filter_by(id=form.continent.data).first()
       ethnicity = Ethnicity.query.filter_by(id=form.ethnicity.data).first()
       

       return '<table border ="3"><thead><tr><th>Continent</th><th>Ethnicity</th><th>Code</th></tr><tr><td>{}</td><td>{}</td><td>{}</td></tr></thead>'.format(continent.name, ethnicity.name, continent.code)
#       return '<h1>Continent : {}, Ethnicity: {}, Code: {}, Feature: </h1>'.format(continent.name, ethnicity.name, continent.code, feature.name)
    return render_template('/template/index1.html', form=form)

@app.route('/ethnicity/<get_ethnicity>')
def ethnicitybycontinent(get_ethnicity):
    if get_ethnicity:
      ethnicity = Ethnicity.query.filter_by(continent_id=get_ethnicity).all()
    else:
      ethnicity = Ethnicity.query.all()
       
    ethnicityArray = []
    for continent in ethnicity:
        ethnicityObj = {}
        ethnicityObj['id'] = continent.id
        ethnicityObj['name'] = continent.name
        ethnicityArray.append(ethnicityObj)
    return jsonify({'ethnicitycontinent' : ethnicityArray}) 

@app.route('/ethnicity/<get_feature>')
def featurebyethnicity(get_feature):
    if get_feature:
      feature = Feature.query.filter_by(ethnicity_id=get_feature).all()
    else:
      feature = Feature.query.all()
       
    featureArray = []
    for ethnicity in feature:
        featureObj = {}
        featureObj['id'] = ethnicity.id
        featureObj['name'] = ethnicity.name
        featureArray.append(featureObj)
    return jsonify({'featureethnicity' : featureArray}) 

#@app.route('/ethnicity/<get_ethnicity>')
#def ethnicitybycontinent(get_ethnicity):
    #ethnicity = Ethnicity.query.filter_by(continent_id=get_ethnicity).all()
    #ethnicityArray = []
    #for feature in ethnicity:
        #ethnicityObj = {}
        #ethnicityObj['id'] = feature.id
        #ethnicityObj['name'] = feature.name
        #ethnicityArray.append(stateObj)
    #return jsonify({'ethnicitycontinent' : ethnicityArray})
  
#@app.route('/feature/<get_feature>')
#def feature(get_feature):
    #ethnicity_data = Feature.query.filter_by(ethnicity_id=get_feature).all()
    #featureArray = []
    #for feature in ethnicity_data:
        #featureObj = {}
        #featureObj['id'] = feature.id
        #featureObj['name'] = feature.name
        #featureArray.append(cityObj)
    #return jsonify({'featurelist' : featureArray}) 








#@app.route('/template', methods=['POST', 'GET'])
#    continents = Continent.form.get('continent_id')
#    ethnicitys = Ethnicity.filter(Ethnicity.continent_id==continent_id)
#    return render_template("template/index.html", ethnicitys=ethnicitys, continents=continents)
#
#@app.route('/template/search', methods=['POST', 'GET'])
#def search():
#    continent_id = request.args.get('continent_id') or ""
#    continents = Continent.query.order_by(Continent.id.desc()).all()
#    #ethnicitys = Ethnicity.form.get('id')
#    ethnicitys = Ethnicity.query.order_by(Ethnicity.id.desc())
#    if str.isdigit(continent_id):
#        ethnicitys = Ethnicity.filter(Ethnicity.continent_id==continent_id)
#    return render_template('/template/search.html', ethnicitys=ethnicitys, continents=continents)
#def search():
#    continent_id = request.args.post('continent_id') or ""
#    print(continent_id)
#    ethnicitys = Ethnicity.query.filter(Ethnicity.continent_id==continent_id)
#
#    return render_template("template/search.html", ethnicitys=ethnicitys)

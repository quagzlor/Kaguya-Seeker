from flask import render_template, request, redirect, url_for, flash

from admin import app

from lib.models import Ethnicity, Continent

from lib.db import db

from functools import wraps

@app.route('/template', methods=['POST', 'GET'])
def index():
    
    continents = Continent.query.all()# SELECT * FROM continents;
    ethnicitys = Ethnicity.query.all()# SELECT * FROM ethncitys;
    return render_template("template/index.html", continents=continents, ethnicitys=ethnicitys)

#<!--This script is used to update ethnicitys when data from continents is selected-->
@app.route('/template/ethnicitys_update', methods=['POST'])
def ethnicitys_update():
    
    req = request.json
    cont_id = req.get('cont_id')
    filtered_eth = Ethnicity.query().filter(continent_id == int(cont_id)).all()
    return filtered_eth

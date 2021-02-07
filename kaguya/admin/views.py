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

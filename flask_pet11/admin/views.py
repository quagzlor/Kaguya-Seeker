from flask import render_template, request, redirect, url_for, flash

from admin import app

from lib.models import Pet, Owner

from lib.db import db

from functools import wraps



@app.route('/pets')
def index():
    pets = Pet.query.order_by(Pet.id.desc()).all()
    return render_template("pets/index.html", pets=pets)

@app.route('/pets/<int:id>')
def info(id):
    pet = Pet.query.get(id)
    return render_template('pets/info.html', pet=pet)

@app.route('/pets/new')
def new():
    owners = Owner.query.all()
    return render_template('pets/new.html', owners=owners)



@app.route('/pets/create', methods =['POST'])
def create():
    pet = Pet(
    name=request.form.get('name'),
    owner_id=request.form.get('owner_id'),
    )
    try:
        db.session.add(pet)
        db.session.commit()
    except:
        flash('added', 'error')
        return redirect(url_for('new'))
    flash('added Sucessfully', 'success')
    return redirect(url_for('index'))

@app.route('/<int:id>/edit')
def edit(id):
    pet = Pet.query.get(id)
    owners = Owner.query.all()
    return render_template('pets/edit.html', pet=pet, owners=owners)

@app.route('/<int:id>/update', methods =['POST'])
def update(id):
    pet = Pet.query.get(id)
    pet.name = request.form.get('name')
    pet.owner_id = request.form.get('owner_id')
    try:
        db.session.merge(pet)
        db.session.commit()
    except:
        flash('Please check the input value', 'error')
        return redirect(url_for('new'))
    flash ('Edit Successfully ', 'success')
    return redirect(url_for('index'))

@app.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    pet = Pet.query.get(id)
    db.session.delete(pet)
    db.session.commit()
    flash('Delete Successfully', 'success')
    return redirect(url_for('index'))

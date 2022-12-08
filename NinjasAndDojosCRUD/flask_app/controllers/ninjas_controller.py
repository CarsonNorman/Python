from flask_app import app
from flask import Flask, render_template as render, redirect, request

from flask_app.models.ninja_models import Ninja
from flask_app.models.dojos_models import Dojo

@app.route('/create/ninja')
def ninja_form():
    dojos = Dojo.get_dojos()
    return render('ninjaForm.html', dojos=dojos)

@app.route('/create/ninja/confirm', methods=['post'])
def create_ninja():
    dojo = request.form['dojo']
    Ninja.create_ninja(request.form)
    return redirect(f'/dojo/{dojo}')
  
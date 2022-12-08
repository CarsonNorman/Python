from flask_app import app
from flask import Flask, render_template, redirect, request

from flask_app.models.dojos_models import Dojo

@app.route('/')
def render():
   dojos = Dojo.get_dojos()
   return render_template('index.html', dojos=dojos)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    if request.form['name'] != '':
        Dojo.create_dojo(request.form)
        return redirect('/')
    return redirect('/')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = Dojo.get_all_info({'id':id})
    print(data)
    return render_template('dojo.html', dojo=data)
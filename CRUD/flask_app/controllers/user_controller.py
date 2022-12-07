from flask_app import app
from flask import Flask, render_template as render, redirect, request

from flask_app.models.users_model import User

@app.route('/new_user')
def render_create():
    return render('create.html')

@app.route('/create', methods=['POST'])       
def create():
    User.create(request.form)
    return redirect('/')

@app.route('/')
def render_all():
    users = User.get_all()
    return render('read.html', user_list=users)

@app.route('/read/<int:id>')
def render_one(id):
    user = User.get_one({"id": id})
    print(user)
    return render('read_one.html', user= user)

@app.route('/delete/<int:id>')
def delete(id):
    user = User.delete({"id": id})
    return redirect('/')

@app.route('/update/<int:id>')
def update(id):
    user = User.get_one({"id": id})
    return render('update.html', id=user.id)

@app.route('/update/<int:id>/confirm', methods=['POST'])
def update_info(id):
    User.update(request.form)
    return redirect('/')
from flask_app import app, bcrypt
from flask import Flask, render_template as render, redirect, request, session, flash, url_for
from flask_app.models.login_model import Login
from flask_app.models.thoughts_model import Thought


@app.route('/')
@app.route('/<int:err>')
def landing(err=0):
    return render('landing.html', err=err)

@app.route('/validateCreate', methods=['POST'])
def validateCreate():
    formData = request.form
    if formData['name'] == '':
        flash('Name Field Cannot be empty')
        return redirect(url_for('landing', err=1))
    if formData['pass'] == '':
        flash('Password Field Cannot be empty')
        return redirect(url_for('landing', err=1))
    if formData['pass-confirm'] == '' or formData['pass-confirm'] != formData['pass']:
        flash('Passwords do not match')
        return redirect(url_for('landing', err=1))
    hash = bcrypt.generate_password_hash(formData['pass'])
    data = {
        **request.form,
        'pass': hash
    }
    return Login.create(data)

@app.route('/validateLog', methods=['POST'])
def validateLog():
    formData = request.form
    if formData['name'] == '':
        flash('Name field Cannot be empty')
        return redirect(url_for('landing', err=2))
    if formData['pass'] =='':
        flash('Password field cannot be empty')
        return redirect(url_for('landing', err=2))
    return Login.login(formData)

@app.route('/logout')
def logout():
    Login.logout()
    return redirect('/')


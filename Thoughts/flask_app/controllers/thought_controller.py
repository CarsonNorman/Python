from flask_app import app
from flask import Flask, render_template as render, redirect, request, session, flash, url_for
from flask_app.models.thoughts_model import Thought
from flask_app.models.login_model import Login


@app.route('/dashboard/<int:id>')
def renderHome(id):
    if 'id' in session and int(id) == int(session['id']):
        userData = Login.get_one({'id':id})
        print('filter', filter)
        if 'filter' in session:
            if session['filter'] == 'following':
                print('Running following filter' )
                postData = Thought.get_all_following()
            if session['filter'] == 'own':
                print('Running own thoughts filter' )
            postData = Thought.get_user_thoughts({'id':id})
            if session['filter'] == 'all':
                print('Running all filter' )
                postData = Thought.get_all_thoughts()
        else:
            print('Running all filter' )
            postData = Thought.get_all_thoughts()
        print('postData', postData)
        return render('dashboard.html', userData = userData, postData=postData)
    else: 
        flash('Please Login')
        return redirect(url_for('landing', err=3))

@app.route('/applyFilter/<int:id>/<filter>')
def applyFilter(id, filter):
    session['filter'] = filter
    return redirect(url_for('renderHome', id=id))

@app.route('/delete/post/<int:id>')
def deletePost(id):
    if 'id' in session:
        Thought.delete({'id':id})
        return redirect(url_for('renderHome', id=session['id']))
    return redirect(url_for('landing', err=3))

@app.route('/create/post/<int:id>')
def renderPost(id):
    return render('newPost.html', id=id)

@app.route('/create/post/<int:id>/confirm', methods=['POST'])
def createPost(id):
    if 'id' in session:
        post=request.form['post']
        if post != '':
            Thought.create({'user_id': id, 'thought': post})
            return redirect(url_for('renderHome', id=session['id']))
        flash('Post must not be empty')
        return redirect(url_for('renderPost', id=id))
    return redirect(url_for('landing', err=3))
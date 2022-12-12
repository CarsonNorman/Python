from flask_app import app
from flask import Flask, render_template as render, redirect, request, session, flash, url_for
from flask_app.models.recipe_model import Recipe
from flask_app.models.login_model import Login


@app.route('/recipe/create/<int:id>')
def renderCreate(id):
    if 'id' in session and int(id) == int(session['id']):
        return render('recipe.html', id=id)
    else: 
        flash('Please Login')
        return redirect(url_for('landing', err=3))

@app.route('/recipe/validate/<int:id>', methods=['post'])
def validateRecipe(id):
    if 'id' in session and int(id) == int(session['id']):
        if Recipe.validate(request.form):
            Recipe.create({**request.form, 'user':id})
            return redirect(f'/dashboard/{id}')
        else:
         return redirect(url_for('renderCreate', id=id))
    else: 
        flash('Please Login')
        return redirect(url_for('landing', err=3))

@app.route('/recipe/view/<int:id>')
def viewRecipe(id):
    if 'id' in session:
        userData = Login.get_one({'id':session['id']})
        recipe = Recipe.get_one({'id': id})
        return render('viewRecipe.html', recipe=recipe, userData=userData)

@app.route('/recipe/delete/<int:id>')
def deleteRecipe(id):
    if 'id' in session:
        Recipe.delete({'id':id})
        activeId = session['id']
        return redirect(f'/dashboard/{activeId}')
    else: 
        flash('Please Login')
        return redirect(url_for('landing', err=3))
    
@app.route('/recipe/edit/<int:id>')
def renderEdit(id):
    if 'id' in session:
        recipeData = Recipe.get_one({'id':id})
        return render('editRecipe.html', recipeData = recipeData)
    else: 
        flash('Please Login')
        return redirect(url_for('landing', err=3))

@app.route('/recipe/edit/confirm/<int:id>', methods=['POST'])
def editRecipe(id):
    if 'id' in session:
        data={
            **request.form,
            'id':id
        }
        Recipe.edit(data)
        activeId = session['id']
        return redirect(f'/dashboard/{activeId}')
    else: 
        flash('Please Login')
        return redirect(url_for('landing', err=3))

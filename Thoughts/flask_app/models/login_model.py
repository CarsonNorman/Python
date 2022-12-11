from flask_app import bcrypt
from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, render_template as render, redirect, request, session, flash, url_for

class Login:
    def __init__(self, data):
        self.id = data.id
        self.name = data.name
        self.password = data.password
        self.created_at = data.created_at
        self.updated_at = data.updated_at

    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO users (name,password)
        VALUES(%(name)s, %(pass)s)
        """
        results = connectToMySQL('thoughts').query_db(query, data)
        if results != False:
            user = cls.get_one({'id': results})
            session['id'] = user['id']
            return redirect(url_for('renderHome', id=user['id']))
        flash('Please Login with existing account')
        return redirect(url_for('landing', err=1))

    @classmethod
    def get_one(cls, data):
        print('data', data)
        query="""
        SELECT * FROM users 
        WHERE id=%(id)s
        """
        results = connectToMySQL('thoughts').query_db(query, data)
        print(results)
        return results[0]
  
    @classmethod
    def login(cls, data):
        print('data',data)
        query="""
        SELECT *
        FROM users 
        WHERE name=%(name)s
        """
        results = connectToMySQL('thoughts').query_db(query, data)
        print(results)
        if not results:
            flash('Login invalid')
            return redirect(url_for('landing', err=2))
        userPass = data['pass']
        checkPass = results[0]['password']
        if not bcrypt.check_password_hash(checkPass, userPass):
            flash('Login invalid')
            return redirect(url_for('landing', err=2))
        session['id'] = results[0]['id']
        return redirect(url_for('renderHome', id=results[0]["id"], filter='all'))

    @staticmethod
    def logout():
        session.clear()
        return redirect('/')
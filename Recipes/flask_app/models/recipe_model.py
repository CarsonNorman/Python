from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, render_template as render, redirect, request, session, flash, url_for

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.under = data['under']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['created_at']
        self.user_id = data['users_id']

    @classmethod
    def create(cls,data):
        query= """
            INSERT INTO recipes(name, description, under, instructions, users_id, made_at)
            VALUES(%(name)s, %(description)s, %(under)s, %(instructions)s, %(user)s, %(made_at)s)
        """
        return connectToMySQL('recipes').query_db(query, data)
    @classmethod
    def get_all(cls):
        query = """
            SELECT *, users.name as user , users.id as owner
            FROM recipes JOIN users ON users.id = recipes.users_id
        """
        results = connectToMySQL('recipes').query_db(query)
        return results
    @classmethod
    def get_one(cls, data):
        query="""
            SELECT recipes.id, recipes.name, recipes.description, recipes.under, recipes.instructions, recipes.made_at, users.name as user , users.id as owner
            FROM recipes JOIN users ON users.id = recipes.users_id
            WHERE recipes.id = %(id)s
        """
        results = connectToMySQL('recipes').query_db(query, data)
        print(results)
        return results[0]
    @classmethod
    def delete(cls, data):
        query="""
            DELETE FROM recipes
            WHERE recipes.id = %(id)s
        """
        return connectToMySQL('recipes').query_db(query, data)
    @classmethod
    def edit(cls, data):
        query="""
            UPDATE recipes
            SET name=%(name)s, description=%(description)s, under=%(under)s, instructions=%(instructions)s, made_at=%(made_at)s, updated_at=now()
            WHERE id=%(id)s;
        """
        return connectToMySQL('recipes').query_db(query, data)
    @classmethod
    def validate(cls, data):
        print(data)
        print(data['name'])
        if not data['name']:
            flash('Name cannot be empty')
            print('empty name')
            return False
        if data['description'] == '':
            flash('Description cannot be empty')
            return False
        if data['instructions'] == '':
            flash('Instructions cannot be empty')
            return False
        return True

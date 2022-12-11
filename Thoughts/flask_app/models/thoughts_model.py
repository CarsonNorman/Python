from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, render_template as render, redirect, request, session, flash, url_for

class Thought:
    def __init__(self, data):
        self.name = data['name']
        self.thought = data['thought']
        self.user_id = data['user_id']
    
    @classmethod 
    def create(cls, data):
        query = """
        INSERT INTO thoughts (thought,user_id)
        VALUES(%(thought)s, %(user_id)s)
        """
        results = connectToMySQL('thoughts').query_db(query, data)
        return results

    @classmethod
    def get_user_thoughts(cls, data):
        print('data', data)
        query="""
        SELECT users.name, thoughts.thought, users.id, thoughts.id AS thought_id
        FROM users JOIN thoughts ON users.id = thoughts.user_id
        WHERE users.id = %(id)s;
        """
        results = connectToMySQL('thoughts').query_db(query, data)
        print(results)
        return results

    @classmethod
    def get_all_thoughts(cls):
        query="""
        SELECT users.name, thought, users.id, thoughts.id AS thought_id
        FROM thoughts JOIN users ON thoughts.user_id = users.id
        """
        return connectToMySQL('thoughts').query_db(query)
    @classmethod
    def delete(cls, data):
        query="""
        Delete From likes WHERE
        thought_id = %(id)s;
        """
        connectToMySQL('thoughts').query_db(query, data)
        query="""
        DELETE FROM thoughts 
        WHERE id = %(id)s
        """
        results = connectToMySQL('thoughts').query_db(query, data)
        return results

    @classmethod
    def get_all_following(cls):
        return cls.get_all_thoughts()

    @staticmethod
    def like(data):
        query="""
        INSERT INTO likes(user_id, thought_id)
        VALUE(%(user)s, %(thought)s)
        """
        results = connectToMySQL('thoughts').query_db(query, data)
    @staticmethod
    def get_likes():
        query="""
        SELECT *
        from likes 
        """
        return connectToMySQL('thoughts').query_db(query)
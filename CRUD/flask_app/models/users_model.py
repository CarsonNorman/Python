# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['createdat']
        self.updated_at = data['updatedat']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append( cls(user) )
        return users
    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO users ( first_name , last_name, email, createdat, updatedat )
        VALUES ( %(first)s , %(last)s , %(email)s, now(), now());
        """
        return connectToMySQL('users').query_db(query, data)
    @classmethod
    def get_one(cls, data):
        query = '''
        SELECT * FROM users 
        WHERE id=%(id)s;
        '''
        results = connectToMySQL('users').query_db(query, data)
        if results:
            return cls(results[0])
        else:
            return False
    @classmethod
    def delete(cls, data):
        query=query = '''
        DELETE FROM users 
        WHERE id=%(id)s;
        '''
        return connectToMySQL('users').query_db(query, data)
    @classmethod
    def update(cls, data ):
        query = """
        UPDATE users 
        SET first_name = %(first)s, last_name = %(last)s, email=%(email)s, updatedat= now() WHERE id = %(id)s;
        """
        return connectToMySQL('users').query_db(query, data)
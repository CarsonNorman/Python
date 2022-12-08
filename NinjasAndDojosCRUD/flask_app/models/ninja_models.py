from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM ninjas
        """
        results = connectToMySQL('dojosandninjas').query_db(query)
        ninjas = []
        for ninja in ninjas:
            ninjas.append(cls(ninja))
        return ninja
    @classmethod
    def create_ninja(cls, data):
        query ="""
        INSERT INTO ninjas(first_name, last_name, age, created_at, updated_at, dojo_id)
        VALUES(%(fname)s, %(lname)s, %(age)s, now(), now(), %(dojo)s)
        """
        return connectToMySQL('dojosandninjas').query_db(query, data)
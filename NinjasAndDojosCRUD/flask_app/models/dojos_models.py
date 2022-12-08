from flask_app.config.mysqlconnection import connectToMySQL
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_dojos(cls):
        query = """
        SELECT * FROM dojos;
        """
        results = connectToMySQL('dojosandninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    @classmethod
    def get_all_info(cls, data):
        query="""
        SELECT dojos.name, ninjas.first_name, ninjas.last_name, ninjas.age
        FROM dojos JOIN ninjas on dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(id)s
        """
        results = connectToMySQL('dojosandninjas').query_db(query, data)
        return results
        
    @classmethod
    def create_dojo(cls, data):
        query= """
        INSERT INTO dojos(name, created_at, updated_at)
        VALUES (%(name)s, now(), now())
        """
        return connectToMySQL('dojosandninjas').query_db(query, data)
    @classmethod
    def delete_dojo(cls, data):
        query = """
        DELETE FROM dojos
        WHERE id=%(id)s
        """
        return connectToMySQL('dojosandninjas').query_db(query, data)

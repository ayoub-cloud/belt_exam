from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Show:
    def __init__(self,data):
        self.id=data['id']
        self.title=data['title']
        self.network=data['network']
        self.release_date=data['release_date']
        self.description=data['description']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.user_id=data['user_id']
        self.owner = user_model.User.get_by_id({'id':self.user_id})

    #create show
    @classmethod
    def save_show(cls, data):
        query="INSERT INTO shows (user_id,title,description,network,release_date) VALUES (%(user_id)s,%(title)s,%(description)s,%(network)s,%(release_date)s);"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    
    #get all shows
    @classmethod 
    def get_shows(cls): 
        query="SELECT * FROM shows;" 
        results= connectToMySQL(DATABASE).query_db(query)
        shows=[]
        for row in results:
            shows.append(cls(row))
        return shows
    
    #get one show by id
    @classmethod
    def get_by_id_show(cls,data):
        query="SELECT * FROM shows WHERE id=%(id)s;"
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])

    #update show
    @classmethod
    def update_show(cls,data):
        query="""UPDATE shows SET title=%(title)s,
                description=%(description)s,network=%(network)s,release_date=%(release_date)s
                WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #delete
    @classmethod
    def delete_show(cls,data):
        query="DELETE FROM shows WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    #validate
    @staticmethod
    def validate_show(data): 
        is_valid = True

        if len(data['title'])<3:
            flash("Title must be more than 3 characters!","show")
            is_valid = False
        if len(data['description'])<3:
            flash("Description must be more than 3 characters!","show")
            is_valid = False
        if len(data['network'])<3:
            flash("Network must be more than 3 characters!","show")
            is_valid=False
        if data['release_date']=="":
            flash("Release Date must be not blank!","show")
            is_valid = False
            
        return is_valid
    



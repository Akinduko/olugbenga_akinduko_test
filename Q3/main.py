from lrucache import lru_cache
from flask import Flask
from flask_restful import Api, Resource, reqparse

cache=lru_cache()
users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]

class Route(Resource):

    def get(self, name):
        if name=='cache':
            return cache.all(),200
        #cache in use
        try:
            cached = cache.view(name)  
            return {**cached,**{'cached':True}}, 200
        except:
            for user in users:
                if(name == user["name"]):
                    cache.update(name, user)
                    return {**user,**{'cached':False}}, 200
            return "Route not found", 404

    def post(self, name):
        return "Method not available", 404

    def put(self, name):
       return "Method not available", 404

    def delete(self, name):
        return "Method not available", 404

class __init_server:
    def __init__(self):
        self.api={}

    def start_server(self): 
        app = Flask(__name__)
        api= Api(app)
        self.api=api
        api.add_resource(Route, "/cache/<string:name>")
        app.run(debug=True)
    
    def get_api(self):
       return self.api

server=__init_server()
server.start_server()
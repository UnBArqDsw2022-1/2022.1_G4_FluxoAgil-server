from flask import Flask
from flask_restful import Resource, Api

class HelloFluxoAgil(Resource):
    def get(self):
        return {'Welcome': 'to Fluxo Agil API'}

def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config['SECRET KEY'] = ''
    api.add_resource(HelloFluxoAgil, '/')
    return app
    
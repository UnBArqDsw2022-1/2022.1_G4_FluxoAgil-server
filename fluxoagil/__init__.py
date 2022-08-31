from flask import Flask
from flask_restful import Resource, Api
from fluxoagil.views import AcademicHistory, CoursesView


class HelloFluxoAgil(Resource):
    def get(self):
        return {'Welcome': 'to Fluxo Agil API'}


def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config['SECRET KEY'] = ''
    app.config['MAX_CONTENT_LENGTH'] = 512 * 1024   # limits maximum allowed upload size to 512KiB
    api.add_resource(HelloFluxoAgil, '/')
    api.add_resource(AcademicHistory, '/academic-history')
    api.add_resource(CoursesView, '/courses')
    return app

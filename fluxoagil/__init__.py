from flask import Flask
from flask_restful import Resource, Api
from fluxoagil.views import AcademicHistory, Recommendation
from flask_cors import CORS


class HelloFluxoAgil(Resource):
    def get(self):
        return {'Welcome': 'to Fluxo Agil API'}


def create_app():
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    app.config['SECRET KEY'] = ''
    # limits maximum allowed upload size to 512KiB
    app.config['MAX_CONTENT_LENGTH'] = 512 * 1024
    api.add_resource(HelloFluxoAgil, '/')
    api.add_resource(AcademicHistory, '/academic-history')
    api.add_resource(Recommendation, '/recommendation')
    return app

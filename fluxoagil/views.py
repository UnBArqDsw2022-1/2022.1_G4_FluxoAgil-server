from flask_restful import reqparse, Resource
from flask import jsonify, request
import werkzeug
import uuid
import os
from fluxoagil.extractor import ContentExtractor

UPLOAD_DIR = os.path.join(os.getcwd(), 'fluxoagil', 'uploads')

class AcademicHistory(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def post(self):
        self.parser.add_argument(
            'file',
            type=werkzeug.datastructures.FileStorage,
            location='files')
        args = self.parser.parse_args()

        if not args['file']:
            resp = jsonify({'error': 'No files uploaded'})
            resp.status_code = 400
            return resp

        file = args['file']
        file_name = file.filename

        if not AcademicHistory.allowed_file(file_name):
            resp = jsonify({'error': 'File type not supported (must be PDF)'})
            resp.status_code = 400
            return resp

        new_file_name = str(uuid.uuid4()) + '.pdf'
        file_path = os.path.join(UPLOAD_DIR, new_file_name)
        file.save(file_path)

        academic_history = ContentExtractor(file_path).academic_history

        os.remove(file_path)

        return academic_history

    def allowed_file(filename):
        ALLOWED_EXTENSIONS = {'pdf'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class Recommendation(Resource): 
    def post(self): 
        json_data = request.get_json(force=True)
        print(json_data)
        return json_data
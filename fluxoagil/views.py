from flask_restful import reqparse, Resource
from flask import jsonify
import werkzeug
import uuid
import os
from utils import ContentExtractor

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

        approved_courses = ContentExtractor(file_path).aproved_courses

        os.remove(file_path)

        return approved_courses

    def allowed_file(filename):
        ALLOWED_EXTENSIONS = {'pdf'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

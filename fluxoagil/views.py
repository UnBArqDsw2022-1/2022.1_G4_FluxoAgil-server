from flask_restful import reqparse, Resource
import werkzeug
import uuid
import os
from utils import ContentExtractor

UPLOAD_DIR = ""


class AcademicHistory(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def post(self):

        self.parser.add_argument(
            "file",
            type=werkzeug.datastructures.FileStorage,
            location="files")
        args = self.parser.parse_args()

        file = args.get("file")
        file_name = str(uuid.uuid4()) + ".pdf"
        file_path = os.path.join(UPLOAD_DIR, file_name)
        file.save(file_path)

        approved_courses = ContentExtractor(file_path).aproved_courses

        os.remove(file_path)

        return approved_courses

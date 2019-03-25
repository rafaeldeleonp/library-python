from flask_restful import Resource
from bson.objectid import ObjectId
from library.utils import format_response


class Book(Resource):
    def __init__(self, **kwargs):
        self.model = kwargs['db'].books

    def get(self, id):
        book = self.model.find_one({"_id": ObjectId(id)})

        # If the document does not exist in db, return a 404 error.
        if not (book):
            return {'message': 'Not found', 'data': {}}, 404

        return {'message': 'Success', 'code': '200', 'data': format_response(book)}, 200

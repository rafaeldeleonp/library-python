from flask_restful import Resource
from bson.objectid import ObjectId
from library.utils import format_response


class Page(Resource):
    def __init__(self, **kwargs):
        self.model = kwargs['db'].pages

    def get(self, id, page_number, format):
        page = self.model.find_one(
            {"book_id": ObjectId(id), "number": page_number})

        # If the document does not exist in db, return a 404 error.
        if not (page):
            return {'message': 'Not found', 'data': {}}, 404

        return {'message': 'Success', 'code': '200', 'data': page["content"]}, 200

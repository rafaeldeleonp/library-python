import mongoengine


class Book(mongoengine.Document):
    ISBN = mongoengine.StringField(required=True)
    title = mongoengine.StringField(required=True)
    summary = mongoengine.StringField(required=True)
    authors = mongoengine.ListField(required=True)
    genres = mongoengine.ListField(required=True)
    pages = mongoengine.IntField(required=True)

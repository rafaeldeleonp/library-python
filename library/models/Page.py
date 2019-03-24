import mongoengine


class Page(mongoengine.Document):
    book_id = mongoengine.StringField(required=True)
    content = mongoengine.StringField(required=True)
    number = mongoengine.IntField(required=True)

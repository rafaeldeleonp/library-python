import mongoengine


class Author(mongoengine.Document):
    first_name = mongoengine.StringField(required=True)
    last_name = mongoengine.StringField(required=True)
    born = mongoengine.DateField(required=True)
    died = mongoengine.DateField(required=True)

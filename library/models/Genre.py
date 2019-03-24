import mongoengine


class Genre(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    description = mongoengine.StringField()

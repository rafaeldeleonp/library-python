from library import app
from mongoengine import *

app.config.from_pyfile('config.py')

connect(name="library", host=app.config["MONGO_URI"])

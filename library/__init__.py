# Import the framework
import logging as logger
from flask import Flask
from flask_restful import Api
from library.db import connect_db, initialize_data
from library.resources.book import Book
from library.resources.page import Page

logger.basicConfig(level="DEBUG")

# Create an instance of Flask
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

# Create API
api = Api(app)

# Get MongoClient
client = connect_db(app.config["MONGO_URI"], logger)

db_name = app.config["MONGO_DATABASE"]

# Always drop database. This is just for this testing project.
client.drop_database(db_name)

db = client[db_name]

# Initialize MongoDB data
initialize_data(db, logger)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# Resources routes
api.add_resource(Book, '/book/<string:id>', resource_class_kwargs={'db': db})
api.add_resource(Page, '/book/<string:id>/page/<int:page_number>/<string:format>',
                 resource_class_kwargs={'db': db})

# Import the framework
import logging as logger
from flask import Flask
from library.db import get_client
from library.seeds.authors import get_authors

logger.basicConfig(level="DEBUG")

# Create an instance of Flask
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

# Get MongoClient
client = get_client(app.config["MONGO_URI"], logger)

# Always drop library database
client.drop_database('library')

db = client.library

# Insert authors data
authors = get_authors()
authors_collection = db.authors
result = authors_collection.insert_many(authors)
logger.info("Inserted authors documents %s" % result.inserted_ids)


@app.route('/')
def todo():
    return "Hello!"

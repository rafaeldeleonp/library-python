# Import the framework
import logging as logger
from flask import Flask
from library.db import get_client, initialize_data

logger.basicConfig(level="DEBUG")

# Create an instance of Flask
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

# Get MongoClient
client = get_client(app.config["MONGO_URI"], logger)

db_name = app.config["MONGO_DATABASE"]

# Always drop database. This is just for this testing project.
client.drop_database(db_name)

db = client[db_name]

# Initialize MongoDB data
initialize_data(db, logger)


@app.route('/')
def todo():
    return "Hello!"

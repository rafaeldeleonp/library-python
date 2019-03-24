# Import the framework
from flask import Flask
# Import MongoClient
from pymongo import MongoClient

# Create an instance of Flask
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

client = MongoClient(app.config["MONGO_URI"])
db = client.library


@app.route('/')
def todo():
    return "Hello!"

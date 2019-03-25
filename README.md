# library-python

Project to learn python and to test syntax. When you run the application, it will automatically run the seed and when you stop the application it will drop the database.

## Getting started

Create a folder at root named `instance` and inside it create a `config.py` file with the following variables: 

```sh
HOST = '0.0.0.0'
PORT = 3000
MONGO_URI = "mongodb://mongo:27017/"
MONGO_DATABASE = 'library'
```

## Run application

To run the app execute the following commands:

```sh
docker-compose build
```

```sh
docker-compose up

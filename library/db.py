from pymongo import MongoClient


def get_client(mongoURI, logger):
    try:
        client = MongoClient(mongoURI)
        logger.info("MongoDB connected successfully on URI: %s" % (mongoURI))
    except:
        logger.error("Could not connect to MongoDB")

    return client

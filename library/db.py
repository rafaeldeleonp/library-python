from pymongo import MongoClient
from library.seeds.authors import get_authors
from library.seeds.genres import get_genres


def get_client(mongoURI, logger):
    try:
        client = MongoClient(mongoURI)
        logger.info("MongoDB connected successfully on URI: %s" % (mongoURI))
    except:
        logger.error("Could not connect to MongoDB")

    return client


def initialize_data(db, logger):
    # Insert authors data
    authors = get_authors()
    authors_result = db.authors.insert_many(authors)
    logger.info("Inserted authors documents %s" % authors_result.inserted_ids)

    # Insert genres data
    genres = get_genres()
    genres_result = db.genres.insert_many(genres)
    logger.info("Inserted genres documents %s" % genres_result.inserted_ids)

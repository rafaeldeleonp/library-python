from pymongo import MongoClient
from library.seeds.authors import get_authors
from library.seeds.genres import get_genres
from library.seeds.books import get_books


def get_authors_ids(author, data):
    items = author.split(",")
    authors = []

    for item in items:
        for d in data:
            fullname = d["first_name"] + " " + d["last_name"]

            if fullname == item:
                authors.append(d["_id"])
                break

    return authors


def get_genres_ids(genre, data):
    items = genre.split(",")
    genres = []

    for item in items:
        for d in data:
            if d["name"] == item:
                genres.append(d["_id"])
                break

    return genres


def format_books(books, authors, genres):
    formatted_books = []

    for book in books:
        formatted_books.append({
            "ISBN": book["ISBN"],
            "title": book["title"],
            "summary": book["summary"],
            "authors": get_authors_ids(book["authors"], authors),
            "genres": get_genres_ids(book["genres"], genres),
        })

    return formatted_books


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

    # Insert books data
    books = get_books()
    formatted_books = format_books(books, authors, genres)
    books_result = db.books.insert_many(formatted_books)
    logger.info("Inserted books documents %s" % books_result.inserted_ids)

    # Insert pages data

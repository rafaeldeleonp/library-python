from pymongo import MongoClient
from library.seeds.authors import get_authors
from library.seeds.genres import get_genres
from library.seeds.books import get_books
from library.seeds.pages import get_pages
from library.utils import format_books, format_pages


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
    pages = get_pages()
    formatted_books = format_books(books, authors, genres, pages)
    books_result = db.books.insert_many(formatted_books)
    logger.info("Inserted books documents %s" % books_result.inserted_ids)

    # Insert pages data
    formatted_pages = format_pages(pages, books)
    pages_result = db.pages.insert_many(formatted_pages)
    logger.info("Inserted pages documents %s" % pages_result.inserted_ids)

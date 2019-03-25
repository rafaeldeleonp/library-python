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


def get_book_pages(book, pages):
    count = 0

    for page in pages:
        if book["ISBN"] == page["ISBN"]:
            count += 1

    return count


def format_books(books, authors, genres, pages):
    formatted_books = []

    for book in books:
        formatted_books.append({
            "_id": book["_id"],
            "ISBN": book["ISBN"],
            "title": book["title"],
            "summary": book["summary"],
            "authors": get_authors_ids(book["authors"], authors),
            "genres": get_genres_ids(book["genres"], genres),
            "pages": get_book_pages(book, pages)
        })

    return formatted_books


def get_book_id(ISBN, books):
    book_id = 0

    for book in books:
        if book["ISBN"] == ISBN:
            book_id = book["_id"]
            break

    return book_id


def format_pages(pages, books):
    formatted_pages = []

    for page in pages:
        formatted_pages.append({
            "_id": page["_id"],
            "book_id": get_book_id(page["ISBN"], books),
            "content": page["content"],
            "number": page["number"]
        })

    return formatted_pages

from model import db
from model.book.book import Book

class BookService:

    def search():
        books = Book.query.filter().all()
        return books
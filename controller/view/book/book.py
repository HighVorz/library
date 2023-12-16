
from flask import Blueprint

from flask import render_template
from controller.model.book.bookservice import BookService

route_book = Blueprint('book', __name__)


@route_book.route("/")
def table():
    books = BookService.search()
    return render_template("book/book.html", books = books)



# 配置网页URL

from app import app


from controller.view.book.book import route_book
from controller.view.index import route_index


def register_all():
    app.register_blueprint(route_index, url_prefix='/')
    app.register_blueprint(route_book, url_prefix='/book')
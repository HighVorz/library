import os
from app import app
from flask.cli import FlaskGroup
from model import db
from model.book.book import Book

from www import register_all

cli = FlaskGroup(app)

if __name__ == '__main__':
    try:
        import sys 
        register_all()

        with app.test_request_context():
            db.create_all()
        
        sys.exit(cli())
    except Exception as e:
        import traceback
        traceback.print_exc()
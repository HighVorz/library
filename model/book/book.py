from model import db
from sqlalchemy import Column, Integer, String, Date, DateTime
class Book(db.Model):
    __table__name = 'book'

    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    publisher = Column(String(100), nullable=False)
    isbn = Column(String(13), nullable=True)
    publish_date = Column(Date, nullable=True)
    quantity = Column(Integer, nullable=False)
    


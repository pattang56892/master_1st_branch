from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    # Define a one-to-many relationship between User and Book
    books = relationship('Book', back_populates='user')

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    status = Column(String(20), default='inactive')

    # Define a many-to-one relationship between Book and User
    user = relationship('User', back_populates='books')

# Create an SQLite database
engine = create_engine('sqlite:///cloud_reading_app.db')
Base.metadata.create_all(engine)

print("Database schema created successfully.")

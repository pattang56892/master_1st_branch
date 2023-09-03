from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

Base = declarative_base()

# Define the User table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    # Define a one-to-many relationship between User and Book
    books = relationship('Book', back_populates='user')

# Define the Book table
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    status = Column(String(20), default='inactive')

# Create an SQLite database
engine = create_engine('sqlite:///cloud_reading_app.db')
Base.metadata.create_all(engine)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cloud_reading_app.db'
db = SQLAlchemy(app)

# Define the User-Book relationship table
users_books = db.Table('users_books',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('status', db.String(20), nullable=False)
)

# User table
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    # Define a one-to-many relationship between User and Book
    books = db.relationship('Book', back_populates='user')

@app.route('/login')
def index():
    # Display user's library of books
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        books = user.books
        return render_template('library.html', books=books)
    else:
        return redirect(url_for('login'))

# Implement other routes for registration, login, logout, etc.

if __name__ == '__main__':
    app.secret_key = 'your-secret-key'
    app.run(debug=True)

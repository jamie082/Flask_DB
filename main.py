from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import json
app = Flask(__name__)
# definitng URL or Path to save our DB
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://books.db"
# Creating DB instance to reference throughout the code
db = SQLAlchemy(app)

# The following code block is used to create a db instance from flask_sqlalchemy and
# DEfine a model class
class Book(db.model):
    isbn = db.Column(db.String(150, primary_key=True)
    title = db.Column(db.String(150))
    author = db.Column(db.String(150))

    @property
    def as_json(self):
        """ Returns object data in a serializable format
        """
        return {
            'isbn' self.isbn,
            'title': self.title,
            'author': self.author
        }
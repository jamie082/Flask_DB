from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import json
# If the DB doesn't exit recreate it else don't overwrite it
if not os.path.exists('books.db'):
    with app.app_context():
        db.create_all()

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    # GET request for getting all books from DB
    if request.method == "GET":
        # retreiving all teh books from DB
        books = Book.query.all()
        # serializing objects so that we can send them in a JSON object
        serialized_books = [book.as_json for book in books]
        # sending all books back to the client in JSON obkect
        return jsonify(serialized_books)
    
    if request.method == "POST":
        payload = request.get_json()
        book = Book(isbn=payload['isbn'],
                title=payload['title'],
                author=payload['author'])
    
        # add new book object to DB
        db.session.add(book)

        # commit db to save changes
        db.session.commit()

        # return the same book to let the user know that it has been added to the DB
        return jsonify(json.dumps(payload))

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000, debug=True)
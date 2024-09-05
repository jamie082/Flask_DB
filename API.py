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
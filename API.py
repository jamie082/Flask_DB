# If the DB doesn't exit recreate it else don't overwrite it
if not os.path.exists('books.db'):
    with app.app_context():
        db.create_all()

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    # GET request for getting all
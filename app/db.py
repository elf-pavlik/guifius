import sqlite3

from app import app
from contextlib import closing
'''
Creates a database and sets up the schema and injects all starter
data needed to run this application.
'''
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()
'''
Initializes the connection to the database. Generally,
this should only be called once when the application begins
'''
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

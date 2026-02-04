import os
import sqlite3

from flask import g

DATABASE = "database.db"


# Initialize DB from schema.sql
def init_db():
    print("Initializing database...")

    # Delete the database if it already exists
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
        print("Existing database removed.")

    with sqlite3.connect(DATABASE) as conn:
        # Create tables based on the schema
        with open("schema.sql", "r") as f:
            conn.executescript(f.read())

        # Populate the database with some data
        with open("seed.sql", "r") as f:
            conn.executescript(f.read())

    print("Database ready.")


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

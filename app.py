import sqlite3
from flask import Flask, render_template

# returns a database connnection to the local sqlite3 file
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/')
def index():
    # gets the database connection, selects all posts and closes the connection
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    # renders the page as "index.html" (which must use the "posts" variable)
    return render_template('index.html', posts=posts)


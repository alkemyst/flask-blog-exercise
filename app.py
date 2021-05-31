import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

# returns a database connnection to the local sqlite3 file
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# gets a single post from the database
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)

# the main page (index.html)
@app.route('/')
def index():
    # gets the database connection, selects all posts and closes the connection
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    # renders the page as "index.html" (which must use the "posts" variable)
    return render_template('index.html', posts=posts)

# the page of a single post
@app.route('/<int:post_id>')
def post(post_id):
    # gets the post (defined above) and renders it via the "post.html" page and the variable "post" used thereby
    post = get_post(post_id)
    return render_template('post.html', post=post)


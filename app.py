import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        number_parts = request.form['number_parts']
        created_date = request.form['created_date']
        updated_date = request.form['updated_date']
 
        if not name:
            flash('Name is required!')
        elif not number_parts:
            flash('Number of Parts is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (name, number_parts, created_date, updated_date) VALUES (?, ?, ?, ?)',
                         (name, number_parts, created_date, updated_date))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        name = request.form['name']
        number_parts = request.form['number_parts']
        created_date = request.form['created_date']
        updated_date = request.form['updated_date']

        if not name:
            flash('Name is required!')

        elif not number_parts:
            flash('Number of Parts is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET name = ?, number_parts = ?, created_date = ?, updated_date = ?'
                         ' WHERE id = ?',
                         (name, number_parts, created_date, updated_date, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
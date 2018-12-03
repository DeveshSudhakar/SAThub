from flask import Flask, render_template, flash, redirect, url_for, session, request, logging

# from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from web import get_links

app = Flask(__name__)

# Config MySQL
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '123456'
# app.config['MYSQL_DB'] = 'myflaskapp'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
# mysql = MySQL(app)

#Articles = Articles()

# Index
@app.route('/')
def index():
    return render_template('home.html')


# About
# @app.route('/about')
# def about():
    # return render_template('about.html')

@app.route('/event')
def event():
    print
    return get_links()


if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)

import os
import click
from flask import Flask, request, make_response, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'NoSecretKey:-(')


@app.route('/')
def hello():
    name = request.args.get('name')
    if name is None:
        # Get the cookies stored in the session.
        name = session.get('name', 'Blanker000')
    return 'Hello, {name}!'.format(name=name)


@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('hello')))
    response.set_cookie('name', name)
    return response


@app.route('/login')
def login():
    session['logged_in'] = True
    session['name'] = 'Blanker111'
    print(session.get('name'))
    return redirect(url_for('hello'))

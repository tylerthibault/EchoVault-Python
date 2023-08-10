from functools import wraps
from flask import g, request, redirect, url_for, session
from flask_app import super_level

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'token' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function

def super_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'token' not in session:
            return redirect('/')
        
        if session['token']['level'] < super_level:
            return redirect('/')
        return f(*args, **kwargs)
    return decorated_function
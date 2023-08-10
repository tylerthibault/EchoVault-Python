from flask_app import app, bcrypt
from flask import render_template, redirect, session, request, flash
from flask_app.models import user_model
from flask_app.config.helpers import set_token, page_back, page_history
from flask_app.config.my_decorators import login_required, super_required


@app.route('/super/users')
@super_required
def super_user_new():
    page_history()
    context = {
        'all_users': user_model.User.get_all()
    }
    return render_template('/views/super/users/all.html', **context)

@app.route('/super/user/<int:id>')
@super_required
def user_one(id):
    context = {
        'one_user': user_model.User.get(id=id)
    }
    return render_template('/views/super/users/one.html', **context)
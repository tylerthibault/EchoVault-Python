from flask_app import app, bcrypt
from flask import render_template, redirect, session, request, flash
from flask_app.models import user_model
from flask_app.config.my_decorators import login_required
from flask_app.config.helpers import set_token, page_back

@app.route('/users/register', methods=['POST'])
def user_register():
    data = {**request.form}
    # validate form
    if not user_model.User.validate_register(data):
        return redirect('/')
    
    # hash pw
    hash_pw = bcrypt.generate_password_hash(data['password'])
    data['password'] = hash_pw

    # create user
    id = user_model.User.create_one(**data)
    last_page = page_back()
    if (last_page == '/'):
        data['id'] = id
        data['level'] = 1
        set_token(data)
        return redirect("/dashboard")
    flash("New User Created", "my_err_toast_msg")
    return redirect(last_page)

@app.route('/users/login', methods=['POST'])
def users_login():
    data = {**request.form}
    # validate
    if not user_model.User.validate_login(data):
        return redirect('/')
    # redirect
    return redirect('/dashboard')

@app.route('/users/logout')
def users_logout():
    del session['token']
    return redirect('/')

@app.route('/user/<int:id>/delete')
@login_required
def user_delete(id):
    if session['token']['id'] == id:
        user_model.User.delete_one(id=id)
    else:
        msg = """
            <span class='text-2xl'>Cannot Delete User</span>
        """
        flash(msg, "my_err_toast_msg")
    return redirect(page_back())
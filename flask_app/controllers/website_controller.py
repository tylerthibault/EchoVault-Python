from flask_app import app, bcrypt, super_level
from flask import render_template, redirect, session, request, flash
from flask_app.models import user_model, website_model, page_model
from flask_app.config.helpers import set_token, page_back, page_history
from flask_app.config.my_decorators import login_required, super_required

@app.route('/super/websites')
@super_required
def super_websites():
    page_history()
    context = {
        'all_users': user_model.User.get_all(),
        'all_websites': website_model.Website.get_all()
    }
    return render_template('/views/super/websites/all.html', **context)

@app.route('/super/website/create', methods=['POST'])
@super_required
def super_website_create():
    # create the website
    website_id = website_model.Website.create_one(**request.form)
    # create the middle table
    website_model.WebsiteHasUser.create_one(
        website_id=website_id,
        user_id= request.form['user_id']
    )
    return redirect(page_back())

@app.route('/website/<int:id>')
@login_required
def super_website_show(id):
    page_history()
    session['website_id'] = id
    context = {
        'website': website_model.Website.get(id = id)[0],
        'all_pages': page_model.Page.get(website_id=id)
    }
    if session['token']['level'] > super_level:
        return render_template('/views/super/websites/one.html', **context)
    return render_template('/views/user/websites/one.html', **context)

@app.route('/super/website/<int:id>/delete')
@super_required
def super_website_deactivate(id):
    if not session['token']['level'] > super_level:
        return redirect(page_back())
    website_model.Website.delete_one(id=id)
    return redirect(page_back())
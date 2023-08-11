from flask_app import app, super_level
from flask import render_template, redirect, session, request
from flask_app.config.my_decorators import login_required
from flask_app.config.helpers import page_history, page_back
from flask_app.models import website_model

@app.route('/')
def index():
    if 'token' in session:
        return redirect('/dashboard')

    page_history()
    return render_template('/index.html')

@app.route('/dashboard')
@login_required
def dashboard():
    page_history()
    context = {
        'websites': website_model.Website.get_all()
    }

    if session['token']['level'] < super_level:
        website_id_list = website_model.WebsiteHasUser.get(user_id=session['token']['id'])
        website_list = []
        for dict in website_id_list:
            web = website_model.Website.get(id = dict['website_id'])[0]
            website_list.append(web)
        context['websites'] = website_list
    return render_template('/views/dashboard.html', **context)

@app.route('/go_back')
def go_back():
    return redirect(page_back(2))
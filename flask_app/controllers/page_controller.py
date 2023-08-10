from flask_app import app, bcrypt, super_level
from flask import render_template, redirect, session, request, flash
from flask_app.models import page_model, section_model
from flask_app.config.helpers import set_token, page_back, page_history
from flask_app.config.my_decorators import login_required, super_required

@app.route('/super/pages/create', methods=['POST'])
@super_required
def super_page_create():
    data = {**request.form}
    data['website_id'] = session['website_id']
    page_model.Page.create_one(**data)
    return redirect(page_back())

@app.route('/page/<int:id>')
@login_required
def super_page_show(id):
    page_history()
    session['page_id'] = id
    context = {
        'all_sections' : section_model.Section.get(page_id=id),
        'all_pages': page_model.Page.get(website_id=session['website_id']),
        'current_page': page_model.Page.get(id=session['page_id'])[0]
    }
    if session['token']['level'] > super_level:
        return render_template('views/super/pages/one.html', **context)
    return render_template('views/admin/pages/one.html', **context)

from flask_app import app, bcrypt, super_level
from flask import render_template, redirect, session, request, flash, jsonify
from flask_app.models import section_model
from flask_app.config.helpers import set_token, page_back, page_history
from flask_app.config.my_decorators import login_required, super_required

@app.route('/super/section/create', methods=['POST'])
@super_required
def super_section_create():
    data = {
        **request.form,
        'page_id': session['page_id']
            }
    print(data)
    section_model.Section.create_one(**data)
    return redirect(page_back())

@app.route('/section/<int:id>/update', methods=['POST'])
@login_required
def section_update(id):
    data = {
        **request.form,
            }
    section_model.Section.update_one(where={'id':id}, **data)
    return redirect(page_back())

@app.route('/api/section/<int:id>')
def api_section(id):
    msg = section_model.Section.get(id=id)
    return jsonify(msg)
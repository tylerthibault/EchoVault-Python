from flask_app.models import base_model
from flask import flash, session

class Page(base_model.Base):
    table_name = "pages"
    attributes = ['name', 'website_id']
    required_attributes = ['name', 'website_id']
    def __init__(self, data):
        super().__init__(data)

        self.name = data['name']
        self.website_id = data['website_id']
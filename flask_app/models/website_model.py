from flask_app.models import base_model
from flask import flash, session

class Website(base_model.Base):
    table_name = "websites"
    attributes = ['name', 'description']
    required_attributes = ['name', 'description']
    def __init__(self, data):
        super().__init__(data)

        self.name = data['name']
        self.description = data['description']

class WebsiteHasUser(base_model.Base):
    table_name = "websites_has_users"
    attributes = ['user_id', 'website_id']
    required_attributes = ['user_id', 'website_id']
    def __init__(self, data):
        super().__init__(data)

        self.user_id = data['user_id']
        self.website_id = data['website_id']
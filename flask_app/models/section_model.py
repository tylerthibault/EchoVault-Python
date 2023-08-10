from flask_app.models import base_model
from flask import flash, session

class Section(base_model.Base):
    table_name = "sections"
    attributes = ['title', 'content', 'page_id']
    required_attributes = ['title', 'content', 'page_id']
    def __init__(self, data):
        super().__init__(data)

        self.title = data['title']
        self.content = data['content']
        self.page_id = data['page_id']
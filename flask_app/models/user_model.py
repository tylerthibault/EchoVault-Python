from flask_app.models import base_model
from flask import flash, session
from flask_app import bcrypt
from flask_app.config.helpers import set_token
import re

EMAIL_PATTERN = re.compile('[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+')

class User(base_model.Base):
    table_name = "users"
    attributes = ['first_name', 'last_name', 'email', 'password']
    required_attributes = ['first_name', 'last_name', 'email', 'password']
    def __init__(self, data):
        super().__init__(data)

        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

    @staticmethod
    def validate_register(data):
        is_valid = True

        if len(data['first_name']) < 1:
            flash('First name is required', 'err_users_first_name')
            is_valid = False

        if len(data['last_name']) < 1:
            flash('Last name is required', 'err_users_last_name')
            is_valid = False

        if not EMAIL_PATTERN.match(data['email']):
            flash('Not a valid email', 'err_users_email')
            is_valid = False

        elif len(data['email']) < 1:
            flash('Email is required', 'err_users_email')
            is_valid = False

        if len(data['password']) < 1:
            flash('Password is required', 'err_users_password')
            is_valid = False

        if len(data['confirm_password']) < 1:
            flash('Confirm Password is required', 'err_users_confirm_password')
            is_valid = False

        if is_valid:
            potential_user = User.get(email=data['email'])
            if potential_user:
                flash("Email is already in use", 'err_users_email')
                is_valid = False
        
        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True

        if len(data['email']) < 1:
            flash('Email is required', 'err_users_email_login')
            is_valid = False

        if len(data['password']) < 1:
            flash('Password is required', 'err_users_password_login')
            is_valid = False

        if is_valid:
            potential_user = User.get(email = data['email'])[0]
            if not potential_user:
                flash("Invalid Credentials", 'err_users_email_login')
                is_valid = False
            else:
                if not bcrypt.check_password_hash(potential_user['password'], data['password']):
                    flash("Invalid Credentials", 'err_users_email_login')
                    is_valid = False
                else:
                    set_token(potential_user)


        return is_valid
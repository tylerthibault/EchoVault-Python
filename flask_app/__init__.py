from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os

app = Flask(__name__)
app.secret_key = "shhhhhhhhhhhhhhhhhhhhhhh"

bcrypt = Bcrypt(app)
CORS(app)

app.DB_HOST = os.getenv("DB_HOST")
app.DB_USERNAME = os.getenv("DB_USERNAME")
app.DB_PASSWORD = os.getenv("DB_PASSWORD")
app.DB_DATABASE = os.getenv("DB_DATABASE")

super_level = 7


from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "shhhhhhhhhhhhhhhhhhhhhhh"

bcrypt = Bcrypt(app)
CORS(app)

DATABASE = "shadow_forge_db"

super_level = 7
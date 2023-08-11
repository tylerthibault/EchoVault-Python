from flask_app import app

if __name__=="__main__":	
    app.DB_HOST = "localhost"
    app.DB_USERNAME = "root"
    app.DB_PASSWORD = "root"
    app.DB_DATABASE = "shadow_forge_db"
    
from flask_app.controllers import page_controller, routes_controller, users_controller, section_controller, website_controller
from flask_app.controllers.super import user_controller
import os



# keep this at the bottom of this file!!
if __name__=="__main__":	
    app.run(debug=True)	
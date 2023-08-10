from flask_app import app
from flask_app.controllers import page_controller, routes_controller, users_controller, section_controller, website_controller
from flask_app.controllers.super import user_controller
 

# keep this at the bottom of this file!!
if __name__=="__main__":	 
    app.run(debug=True)	
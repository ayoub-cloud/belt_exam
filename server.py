from flask_app import app
#! don't forget to import all controllers 
from flask_app.controllers import show_controller
from flask_app.controllers import user_controller
if __name__ == '__main__':
    app.run(debug=True)
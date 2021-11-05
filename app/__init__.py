from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
# from .config import DevConfig

# Initializing application
# app = Flask(__name__,instance_relative_config = True)
# app = Flask(__name__)

# Setting up configuration
# method to set up configuration and pass in the DevConfig subclass

# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# Initializing Flask Extensions
# bootstrap = Bootstrap(app)

# from app import views
# from app import error

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
mail = Mail()


def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app) 
    login_manager.init_app(app)
    mail.init_app(app)
    # db = SQLAlchemy(app)  

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # setting config
    from .request import configure_request
    configure_request(app)
    
    # configure UploadSet
    configure_uploads(app,photos)

    # Will add the views and forms

    return app
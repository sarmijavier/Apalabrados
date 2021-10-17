from flask import Flask
from config import Config, TestConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app = Flask(__name__)

local_path = os.environ.get('PATH_LOCAL')


app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)


from app import routes, models
from app.api import bp as api_bp
app.register_blueprint(api_bp, url_prefix='/api')
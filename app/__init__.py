from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restplus import Api

# Initialize app and related objects
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app, doc='/docs')

# Import modules for visibility
from app import (
    models,
    schemas,
    routes
)

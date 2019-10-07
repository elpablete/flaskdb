import os

db_path = os.path.join(os.path.dirname(__file__), 'app.db')
db_uri = f'sqlite:///{db_path}'
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
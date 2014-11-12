import os

def get_db_url():
    if 'DATABASE_URL' not in os.environ:
       return  'postgresql://localhost/flask_todo_dev'
    else:
        return os.environ['DATABASE_URL']

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'akqweubvaueaeaqqdfhj'
    SQLALCHEMY_DATABASE_URI = get_db_url()

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

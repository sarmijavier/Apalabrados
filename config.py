import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('CLEARDB_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(object):
    database = 'apalabrados_db'
    server = 'localhost:3306'
    username = 'root'
    password = ''
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://"+username+":"+password+"@"+server+"/"+database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

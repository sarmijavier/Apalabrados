import os

class Config(object):
    database = os.environ.get('DB')
    server = os.environ.get('ENDPOINT')
    username = os.environ.get('USERNAME_DB')
    password = os.environ.get('PASSWORD')
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user=username, password=password, server=server, database=database)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(object):
    database = 'apalabrados_db'
    server = 'localhost:3306'
    username = 'root'
    password = ''
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://"+username+":"+password+"@"+server+"/"+database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

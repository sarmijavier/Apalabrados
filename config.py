class Config(object):
    database = 'art_catalogue'
    server = 'dbitlookssimple.cmsj7x8axmnv.us-east-2.rds.amazonaws.com'
    username = 'adminitlookssim'
    password = 'EZpdf2l45xCQCfNlbrtv'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://"+username+":"+password+"@"+server+"/"+database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(object):
    database = 'art_catalogue'
    server = 'localhost:3306'
    username = 'root'
    password = ''
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://"+username+":"+password+"@"+server+"/"+database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

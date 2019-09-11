HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_sqlalchemy_demo'
USERNAME = 'root'
PASSWORD = 'abc80231124'

DB_UI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf-8".format(username=USERNAME,
                                                                                        password=PASSWORD,
                                                                                        host=HOSTNAME, db=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_UI
SQLALCHEMY_TRACK_MODIFICATIONS = False

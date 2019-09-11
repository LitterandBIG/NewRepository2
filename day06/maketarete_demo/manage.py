from flask_script import Manager
from app import app
from models import User
from ext import db
from flask_migrate import Migrate,MigrateCommand

manager = Manager(app)
Manager(app,db)
manager.add_command("db",MigrateCommand)

if __name__ =="__main__":
    manager.run()
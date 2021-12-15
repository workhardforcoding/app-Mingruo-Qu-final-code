from flask_mongoengine import MongoEngine
from services.CustomerService import init_customers
from services.LogisticsService import init_logistics
from services.UserService import init_users
from mongoengine import *

db = MongoEngine()

def initialize_db(app):
    db.init_app(app) #create the db
    init_users()
    init_logistics()
    init_customers()

def fetch_engine():
    return db

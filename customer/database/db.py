from flask_mongoengine import MongoEngine
from services.CustomerService import init_customers
from mongoengine import *

db = MongoEngine()

def initialize_db(app):
    db.init_app(app) #create the db
    init_customers() #populate with default products

def fetch_engine():
    return db

from flask_mongoengine import MongoEngine
from services.ProductService import init_products
from mongoengine import *

db = MongoEngine()

def initialize_db(app):
    db.init_app(app) #create the db
    init_products() #populate with default products

def fetch_engine():
    return db

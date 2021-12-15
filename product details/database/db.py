from flask_mongoengine import MongoEngine
from services.ProductDetailsService import init_productDetails
from mongoengine import *

db = MongoEngine()

def initialize_db(app):
    db.init_app(app) #create the db
    init_productDetails() #populate with default products

def fetch_engine():
    return db

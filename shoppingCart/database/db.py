from flask_mongoengine import MongoEngine
from services.ShoppingCartService import init_shoppingcart
from mongoengine import *

db = MongoEngine()

def initialize_db(app):
    db.init_app(app) #create the db
    init_shoppingcart() #populate with default products

def fetch_engine():
    return db

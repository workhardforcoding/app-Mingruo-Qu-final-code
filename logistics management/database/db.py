from flask_mongoengine import MongoEngine
from services.LogisticsService import init_logistics
from mongoengine import *

db = MongoEngine()

def initialize_db(app):
    db.init_app(app) #create the db
    init_logistics() #populate with default products

def fetch_engine():
    return db

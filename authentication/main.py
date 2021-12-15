from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from jwt import exceptions as jwt_exception

from database.db import initialize_db
from utils.JSONEncoder import MongoEngineJSONEncoder
from resources.SessionResource import Sessions
from resources.CustomerResource import Customer

from resources.UserResource import Users
from resources.LogisticsResource import LogisticsResource


app = Flask(__name__)  # Creating a FLASK app
app.config['MONGODB_SETTINGS'] = {
    'db': 'app-rest',
    'host': 'mongodb://localhost:27017/app-rest'
}

app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
app.config['JWT_SECRET_KEY'] = 'JWT_SECRET_KEY'  # Change this!
app.config['PROPAGATE_EXCEPTIONS'] = True

initialize_db(app)
jwt = JWTManager(app)
app.json_encoder = MongoEngineJSONEncoder
api = Api(app)  # Creating a REST API for the app

# http://localhost:5000/register?email=value&password=value
api.add_resource(Users, '/users')

# http://localhost:5000/login?email=value&password=value
api.add_resource(Sessions, '/sessions')

# http://localhost:5000/rider
# http://localhost:5000/rider/rider_id
# http://localhost:5000/rider/rider_id?arg=value
api.add_resource(Customer,
                 '/customer',
                 '/customer/<string:email>&<string:password>',
                 '/customer/<string:customer_id>')

# http://localhost:5000/rider/rider_id/trip?arg=value
api.add_resource(LogisticsResource,
                 '/logistics',
                 '/logistics/<string:logistics_id>')

@app.route('/')
def hello_world():
    #raise jwt_exception.ExpiredSignatureError()
    return 'Hello World!'
    #return 'Hello World!'


if __name__ == "__main__":
    app.run()  # Runs web app @ http://localhost:5000 by default for me.
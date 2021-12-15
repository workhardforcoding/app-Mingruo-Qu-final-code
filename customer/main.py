from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.CustomerResource import CustomerResource
from utils.JSONEncoder import MongoEngineJSONEncoder

app = Flask(__name__)  # Creating a FLASK app
app.config['MONGODB_SETTINGS'] = {
    'db': 'app-rest',
    'host': 'mongodb://localhost:27017/app-rest'
}

initialize_db(app)
app.json_encoder = MongoEngineJSONEncoder
api = Api(app)  # Creating a REST API for the app


# http://localhost:5000/rider
# http://localhost:5000/rider/rider_id
# http://localhost:5000/rider/rider_id?arg=value
api.add_resource(CustomerResource,
                 '/customers',
                 '/customers/',
                 '/customers/<string:customer_id>')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    app.run()  # Runs web app @ http://localhost:5000 by default for me.
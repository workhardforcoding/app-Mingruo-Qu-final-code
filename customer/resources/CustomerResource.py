from flask_restful import reqparse, Resource
from flask import make_response
from services.CustomerService import *
import json

post_parser = reqparse.RequestParser()
post_parser.add_argument('customer_name', type=str)
post_parser.add_argument('customer_bankaccount', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('customer_name', type=str)
patch_parser.add_argument('customer_bankaccount', type=str)

headers = {'Content-Type': 'application/json'}

class CustomerResource(Resource):
    def get(self, customer_id = None):
        response = get_customer(customer_id)
        return make_response(response.to_json(), 400, headers)

    def post(self):
        args = post_parser.parse_args()
        response = create_customer(args.customer_name, args.customer_bankaccount)
        return make_response(response.to_json(), 400, headers)

    def patch(self, customer_id = None):
        if customer_id is not None:
            args = patch_parser.parse_args()
            response = update_customer(args.customer_name, args.customer_bankaccount, args.customer_softdelete)
            return make_response(response.to_json(), 400, headers)
        return 400



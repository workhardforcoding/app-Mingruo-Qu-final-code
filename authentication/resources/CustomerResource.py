from flask_restful import reqparse, Resource
from flask import make_response, abort
from services.CustomerService import *
from flask_jwt_extended import jwt_required, get_jwt_identity
import json

post_parser = reqparse.RequestParser()
post_parser.add_argument('name', type=str)
post_parser.add_argument('email', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('name', type=str)

headers = {'Content-Type': 'application/json'}

class Customer(Resource):
    @jwt_required()
    def get(self, customer_id = None):
        email_identity = get_jwt_identity()
        if customer_id is None:
            customer = get_customers_by_email(email_identity)
        else:
            customer = get_customer_by_id(customer_id)
        if customer and email_identity == customer.email:
            return make_response(customer.to_json(), 200, headers)
        else:
            return abort(403)

    @jwt_required()
    def post(self):
        email_identity = get_jwt_identity()
        args = post_parser.parse_args()
        if len(args.name) == 0 or len(args.email) == 0:
            abort(400, "ERROR! name and email are required fields.")
        elif email_identity == args.email:
            customer = get_customers_by_email(args.email)
            if customer is None:
                response = create_customer(args.name, args.email)
                return make_response(response.to_json(), 200, headers)
            else:
                abort(400, "ERROR! Customer with this email already exists.")
        else:
            return abort(403)

    @jwt_required()
    def patch(self, customer_id):
        email_identity = get_jwt_identity()
        customer = get_customer_by_id(customer_id)
        if customer and email_identity == customer.email:
            args = patch_parser.parse_args()
            customer = update_customer(customer_id, args.name)
            return make_response(customer.to_json(), 200, headers)
        else:
            abort(403)
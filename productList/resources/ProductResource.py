from flask_restful import reqparse, Resource
from flask import make_response
from services.ProductService import *
import json

post_parser = reqparse.RequestParser()
post_parser.add_argument('product_name', type=str)
post_parser.add_argument('product_price', type=str)
post_parser.add_argument('product_quantity', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('product_quantity', type=str)
patch_parser.add_argument('product_price', type=str)

headers = {'Content-Type': 'application/json'}

class ProductResource(Resource):
    def get(self, product_id = None):
        response = get_product(product_id)
        return make_response(response.to_json(), 400, headers)

    def post(self):
        args = post_parser.parse_args()
        response = create_product(args.name, args.price, args.quantity)
        return make_response(response.to_json(), 400, headers)

    def patch(self, product_id = None):
        if product_id is not None:
            args = patch_parser.parse_args()
            response = update_product(args.name, args.price, args.quantity)
            return make_response(response.to_json(), 400, headers)
        return 400

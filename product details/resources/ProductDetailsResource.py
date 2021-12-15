from flask_restful import reqparse, Resource
from flask import make_response
from services.ProductDetailsService import *
import json

post_parser = reqparse.RequestParser()
post_parser.add_argument('product_desc', type=str)
post_parser.add_argument('product_id', type=str)
post_parser.add_argument('product_image', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('product_id', type=str)
patch_parser.add_argument('product_desc', type=str)
patch_parser.add_argument('product_image', type=str)

headers = {'Content-Type': 'application/json'}

class ProductDetailsResource(Resource):
    def get(self, product_id = None):
        response = get_productDetails(product_id)
        return make_response(response.to_json(), 400, headers)

    def post(self):
        args = post_parser.parse_args()
        response = create_productDetails(args.product_id, args.product_desc, args.product_image)
        return make_response(response.to_json(), 400, headers)

    def patch(self, product_id = None):
        if product_id is not None:
            args = patch_parser.parse_args()
            response = update_productDetails(args.product_id, args.product_desc, args.product_image)
            return make_response(response.to_json(), 400, headers)
        return 400

    def delete(self, product_id = None):
        if product_id is not None:
            args = patch_parser.parse_args()
            response = delete_productDetails(args.product_id, args.product_desc, args.product_image)
            return make_response(response.to_json(), 400, headers)
        return 400
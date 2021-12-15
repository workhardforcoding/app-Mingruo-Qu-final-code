from flask_restful import reqparse, Resource
from flask import make_response
from services.ShoppingCartService import *
import json

post_parser = reqparse.RequestParser()
post_parser.add_argument('customer_id', type=str)
post_parser.add_argument('product_id', type=str)
post_parser.add_argument('item_id', type=str)
post_parser.add_argument('selected_quantity', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('product_id', type=str)
patch_parser.add_argument('item_id', type=str)
patch_parser.add_argument('selected_quantity', type=str)

headers = {'Content-Type': 'application/json'}

class ShoppingCartResource(Resource):
    def get(self, customer_id = None):
        response = get_shoppingCart(customer_id)
        return make_response(response.to_json(), 400, headers)

    def post(self):
        args = post_parser.parse_args()
        response = create_items(args.customer_id, args.product_id, args.item_id, args.selected_quantity)
        return make_response(response.to_json(), 400, headers)

    def patch(self, customer_id = None):
        if customer_id is not None:
            args = patch_parser.parse_args()
            response = update_items(args.customer_id, args.item_id, args.selected_quantity)
            return make_response(response.to_json(), 400, headers)
        return 400

    def delete(self, customer_id = None):
        if customer_id is not None:
            args = patch_parser.parse_args()
            response = delete_items(args.customer_id, args.item_id)
            return make_response(response.to_json(), 400, headers)
        return 400
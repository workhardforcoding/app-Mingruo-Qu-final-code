from flask_restful import reqparse, Resource
from flask import make_response
from services.LogisticsService import *
import json

post_parser = reqparse.RequestParser()
post_parser.add_argument('logistics_manager_name', type=str)
# post_parser.add_argument('logistics_manager_id', type=str)
post_parser.add_argument('logistics_manager_title', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('logistics_manager_name', type=str)
# patch_parser.add_argument('logistics_manager_id', type=str)
patch_parser.add_argument('logistics_manager_title', type=str)

headers = {'Content-Type': 'application/json'}

class LogisticsResource(Resource):
    def get(self, logistics_id = None):
        response = get_logistics(logistics_id)
        return make_response(response.to_json(), 400, headers)

    def post(self):
        args = post_parser.parse_args()
        response = create_logistics(args.logistics_manager_name, args.logistics_manager_title)
        return make_response(response.to_json(), 400, headers)

    def patch(self, logistics_id = None):
        if logistics_id is not None:
            args = patch_parser.parse_args()
            response = update_logistics(args.logistics_manager_name, args.logistics_manager_title, args.logistics_manager_softdelete)
            return make_response(response.to_json(), 400, headers)
        return 400



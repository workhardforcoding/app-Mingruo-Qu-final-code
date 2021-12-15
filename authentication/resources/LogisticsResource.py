from flask_restful import reqparse, Resource
from flask import make_response
from services.LogisticsService import *
from flask_jwt_extended import jwt_required, get_jwt_identity
import json

post_parser = reqparse.RequestParser()
post_parser.add_argument('logistics_name', type=str)
post_parser.add_argument('logistics_email', type=str)

patch_parser = reqparse.RequestParser()
patch_parser.add_argument('logistics_name', type=str)

headers = {'Content-Type': 'application/json'}

class LogisticsResource(Resource):
    @jwt_required()
    def get(self, logistics_id):
        email_identity = get_jwt_identity()
        logistics = get_logistics_by_id(logistics_id)
        if logistics and email_identity == logistics.email:
            logistics = logistics(logistics_id)
            return make_response(logistics.to_json(), 200, headers)
        else:
            return 403

    @jwt_required()
    def post(self, logistics_id):
        email_identity = get_jwt_identity()
        logistics = get_logistics_by_id(logistics_id)
        args = post_parser.parse_args()
        if len(args.email) == 0:
            return "ERROR! email is a required field.", 400
        elif email_identity == logistics.email:
            logistics = create_logistics(logistics_id, args.name, args.email)
            return make_response(logistics.to_json(), 200, headers)
        else:
            return 403



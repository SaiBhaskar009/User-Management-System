from flask import request, jsonify, make_response
from models.users_model import User_Database
from schemas.users_schema import user, users
from flask_restful import Resource
from conn_db import db 
from blueprints import u_blp
from flask_jwt_extended import create_access_token
import datetime

class UserAuth(Resource):

    @u_blp.route('/login', methods=['POST'])
    def login():
    
       data = request.get_json()
       username = data['username']
       password = data['password']

       post = User_Database.query.filter_by(Employee_name=username).first()

       expires = datetime.timedelta(minutes=60)

       if post and password == post.password:
           access_token = create_access_token(identity=username, expires_delta=expires)
           return jsonify({'access_token': access_token})
       else:
           return jsonify({'message': 'Invalid credentials'}), 401
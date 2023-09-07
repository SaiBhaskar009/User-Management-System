from flask import request, json, jsonify
from flask_restful import Resource
from blueprints import u_blp
from schemas.users_schema import user, users
from models.users_model import User_Database
from conn_db import db 

class UserRequirements(Resource):

    @u_blp.route('/test')
    def Test():
        return "Running Successfully"
    
     #getting Every user in the list
    @u_blp.route('/getallusers', methods=['GET'])  
    def get():
        lists = User_Database.query.all()
        result = users.dump(lists)
        return jsonify({"List of Users": result})
    
    #Adding new User 
    @u_blp.route('/adduser', methods=['POST'])
    def post():
        new_user = User_Database(
            Employee_name = request.json['Employee_name'],
            Employee_Id = request.json['Employee_Id'],
            Job_type = request.json['Job_type']
        )
        db.session.add(new_user)
        db.session.commit()
        result = user.dump(new_user)
        return jsonify({
            "Successfully Added New User": result
        })

    #Getting User by their Id
    @u_blp.route('/getuser/<int:user_id>', methods=['GET'])
    def get_item(user_id):
        post = User_Database.query.get_or_404(user_id)
        result =user.dump(post)
        return jsonify({
            "User is present": result
        })

    
    #Modifying Partial Resources
    @u_blp.route('/p_update/<int:user_id>', methods=['PATCH'])
    def patch(self, user_id):
        post = User_Database.query.get_or_404(user_id)
        
        if 'Employee_name' in request.json: 
            post.Employee_name = request.json['Employee_name']
        if 'Employee_Id' in request.json:
            post.Employee_Id = request.json['Employee_Id']
        
        db.session.commit()
        result =user.dump(post)
        return jsonify({
            "User Partial details Updated": result
        })
  
    #Modifying Every Resources
    @u_blp.route('/f_update/<int:user_id>', methods=['PUT'])
    def put(self, user_id):
        post = User_Database.query.get_or_404(user_id)

        if 'Employee_name' in request.json: 
            post.Employee_name = request.json['Employee_name']
        if 'Employee_Id' in request.json:
            post.Employee_Id = request.json['Employee_Id']
        if 'Job_type' in request.json:
            post.Job_type = request.json['Job_type']
            
        db.session.commit()
        result =user.dump(post)
        return jsonify({
            "User Updated": result
        })
    
    #Deleting a User 
    @u_blp.route('/delete/<int:user_id>', methods=['DELETE'])
    def delete(user_id):
        post = User_Database.query.get_or_404(user_id)
        db.session.delete(post)
        db.session.commit()
        return jsonify({
                    'status': '200',
                    'msg': 'Successful deleted the User by ID'
                })
   
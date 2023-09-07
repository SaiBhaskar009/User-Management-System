from flask import request, json, jsonify
from flask_restful import Resource
from schemas.tacs_schema import tacs, tac
from models.tacs_model import Tac_Database
from blueprints import t_blp
from conn_db import db 

class TacRequirements(Resource):

    @t_blp.route('/test_Tac_Database')
    def test():
        return "Test"
    
    @t_blp.route('/getalldata', methods=['GET'])
    def get():
        lists = Tac_Database.query.all()
        result= tacs.dump(lists)
        return jsonify({"List of Tac data": result})
    
    @t_blp.route('/add', methods=['POST'])
    def post():
        new_tac = Tac_Database(
                profile_sourced = request.json["profile_sourced"],
                interviewed = request.json["interviewed"],
                offer_released = request.json["offer_released"],
                data_date= request.json["data_date"]
                
        )
        db.session.add(new_tac)
        db.session.commit()
        result= tac.dump(new_tac)
        return jsonify({
            "Successfully Added New Tac Data": result
        })
    
 
    @t_blp.route('getdata/<int:tac_id>', methods=['GET'])
    def get_item(tac_id):
        post = Tac_Database.query.get_or_404(tac_id)
        result= tac.dump(post)
        return jsonify({
            "Tac Data of Certain is present": result
        })
    
    @t_blp.route('/update/<int:tac_id>', methods=['PATCH'])
    def patch(tac_id):
        post = Tac_Database.query.get_or_404(tac_id)

        if 'profile_sourced' in request.json:
            post.profile_sourced = request.json['profile_sourced']
        if 'yash_id' in request.json:
            post.interviewed = request.json['interviewed']
        
        db.session.commit()
        result= tac.dump(post)
        return jsonify({
            "Tac Data details Updated": result
        })
    
    @t_blp.route('/delete/<int:tac_id>', methods=['DELETE'])
    def delete(tac_id):
        post = Tac_Database.query.get_or_404(tac_id)
        db.session.delete(post)
        db.session.commit()
        return jsonify({
                    'status': '200',
                    'msg': 'Successful deleted the User by ID'
                })
    
    @t_blp.route('/getdatabydate/<date>', methods=['GET'])
    def getdata_date(date):
        post = Tac_Database.query.filter_by(data_date=date).all()
        result = tacs.dump(post)
        return jsonify({
            "The Needed Data by Date": result
        })
    
    @t_blp.route('/getdatabyyear/<year>', methods=['GET'])
    def getdata_year(year):
        post = Tac_Database.query.filter(db.extract('year',Tac_Database.data_date)== year).all()
        result = tacs.dump(post)
        return jsonify({
            "The Needed data w.r.t to Year": result
        })
    
    @t_blp.route('/getdatabymonth/<year>/<month>', methods=['GET'])
    def getdata_by_month(year, month):
        post = Tac_Database.query.filter(db.extract('year', Tac_Database.data_date)== year, db.extract('month', Tac_Database.data_date)== month).all()
        result = tacs.dump(post)
        return jsonify({
            "The Needed data w.r.t month": result
        })
    




    
   
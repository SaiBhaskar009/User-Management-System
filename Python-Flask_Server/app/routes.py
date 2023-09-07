from flask_restful import Api
from views.users_resources import UserRequirements
from views.tacs_resources import TacRequirements


def config_routes(app):
    
    api = Api()

    api.add_resource(UserRequirements, '/users_data',methods=['GET', 'POST'])
    #api.add_resource(UserRequirements, '/users/<int:user_id>', methods=['GET','PUT','PATCH','DELETE'])

    api.add_resource(TacRequirements, '/tac_data', methods=['GET','POST'])
    #api.add_resource(TacRequirements, '/tac_data/<int:tac_id>', methods=['GET','PUT','PATCH','DELETE'])
    
    api.init_app(app)
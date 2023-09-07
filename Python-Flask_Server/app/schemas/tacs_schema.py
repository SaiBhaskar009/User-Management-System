from marshmallow import Schema, fields

class Tac_schema(Schema):
    id = fields.Int()
    profile_sourced = fields.Str(required=True)
    interviewed = fields.Str(required=True)
    offer_released = fields.Str(required=True)
    data_date = fields.Date()
   

tac = Tac_schema()
tacs = Tac_schema(many=True)
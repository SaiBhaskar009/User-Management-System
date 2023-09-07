from marshmallow import Schema, fields


class User_schema(Schema):
    id = fields.Int()
    Employee_name = fields.Str(required=True)
    Employee_Id = fields.Int(required=True)
    Job_type = fields.Str(required=True)
    


user = User_schema()
users = User_schema(many=True)
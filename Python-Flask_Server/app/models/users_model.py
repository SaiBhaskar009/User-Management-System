from conn_db import db 

class User_Database(db.Model):

    __tablename__ = "users_info"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Employee_name = db.Column(db.String(255))
    Employee_Id = db.Column(db.Integer)
    Job_type = db.Column(db.String(255))
    

    def __init__(self, Employee_name, Employee_Id, Job_type):

        self.Employee_name = Employee_name
        self.Employee_Id = Employee_Id
        self.Job_type = Job_type
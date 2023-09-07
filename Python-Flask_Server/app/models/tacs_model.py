from conn_db import db 
from datetime import datetime

import uuid

import sqlalchemy_utils
from sqlalchemy.orm import backref


class Tac_Database(db.Model):

    __tablename__ = "tacs_info"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    profile_sourced = db.Column(db.String(200), nullable=False)
    interviewed = db.Column(db.String(200), nullable=False)
    offer_released = db.Column(db.String(200), nullable=False)
    data_date = db.Column(db.Date)
   
    user_id = db.Column(db.Integer, db.ForeignKey("users_info.id", ondelete='CASCADE'))
    user= db.relationship('User_Database', backref=backref('users', passive_deletes=True))

    
    def __init__(self, profile_sourced, interviewed, offer_released, data_date):

        self.profile_sourced = profile_sourced
        self.interviewed = interviewed
        self.offer_released = offer_released
        self.data_date = data_date
    


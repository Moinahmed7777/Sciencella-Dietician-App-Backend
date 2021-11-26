# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:45:05 2021

@author: Necro
"""

from db import db



class Meal_log(db.Model):
    __tablename__ = 'meal_log'
    id = db.Column(db.String(36), primary_key=True)
    uuid = db.Column(db.String(36), nullable=False)
    meal = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(40), nullable=False)
    time = db.Column(db.String(40), nullable=False)
    meal_name = db.Column(db.String(50), nullable=False)
    #email = db.Column(db.String(80), unique=True, index=True)

    #physical = db.relationship('PhysicalModel', backref='usermodel', uselist=False)

    def __init__(self, id, uuid, meal, date,time,meal_name):
        self.id = id
        self.uuid = uuid
        self.meal = meal
        self.date = date
        self.time = time
        self.meal_name= meal_name
        #self.email = email

    def json(self):
        return {'id': self.id,
                'uuid': self.uuid,
                'meal': self.meal,
                'date': self.date,
                'time': self.time,
                'meal_name': self.meal_name
                }

    @classmethod
    def find_by_name(cls, first_name, last_name):
        return cls.query.filter_by(first_name=first_name, last_name=last_name).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod 
    def find_by_uuid(cls, uuid):
        return cls.query.filter_by(uuid=uuid).all()
    
    @classmethod 
    def find_by_uuid_time(cls, uuid,time):
        return cls.query.filter_by(uuid=uuid,time=time).all()
    @classmethod 
    def find_by_uuid_date(cls, uuid,date):
        return cls.query.filter_by(uuid=uuid,date=date).all()
    @classmethod
    def find_by_uuid_datetime(cls, uuid,date,time):
        return cls.query.filter_by(uuid=uuid,date=date,time=time).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
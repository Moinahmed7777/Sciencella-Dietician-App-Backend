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
    timestamp = db.Column(db.String(40), nullable=False)
    #email = db.Column(db.String(80), unique=True, index=True)

    #physical = db.relationship('PhysicalModel', backref='usermodel', uselist=False)

    def __init__(self, id, uuid, meal, timestamp):
        self.id = id
        self.uuid = uuid
        self.meal = meal
        self.timestamp = timestamp
        #self.email = email

    def json(self):
        return {'id': self.id,
                'uuid': self.uuid,
                'meal': self.meal,
                'timestamp': self.timestamp
                }

    @classmethod
    def find_by_name(cls, first_name, last_name):
        return cls.query.filter_by(first_name=first_name, last_name=last_name).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_uuid_timestamp(cls, uuid,timestamp):
        return cls.query.filter_by(uuid=uuid,timestamp=timestamp).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
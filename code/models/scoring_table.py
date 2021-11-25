# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 13:57:57 2021

@author: Necro
"""

from db import db
#from sqlalchemy import Table, Column, Integer, ForeignKey


class ScoringModel(db.Model):
    __tablename__ = 'scoring_table'

    uuid = db.Column(db.String(36),primary_key=True)
    meal_count = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.String(40), nullable=False)
    running_score = db.Column(db.Float, nullable=False)
    
    def __init__(self,uuid,meal_count,timestamp,running_score):
        self.uuid=uuid
        self.meal_count=meal_count
        self.timestamp=timestamp
        self.running_score=running_score
        
    def json(self):
        return {'uuid': self.uuid,
                'meal_count': self.meal_count,
                'timestamp': self.timestamp,
                'running_score': self.running_score}
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def find_by_uuid(cls,uuid):
        return cls.query.filter_by(uuid=uuid).first()
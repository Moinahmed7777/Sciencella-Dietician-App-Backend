# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 12:30:35 2021

@author: Necro
"""

from flask_restful import Resource, reqparse,abort,fields,marshal_with
from models.scoring_table import ScoringModel
from models.user import UserModel
import datetime


class Scoring(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uuid',
    type=str
    )
    parser.add_argument('meal_count', type=int, required=False)
    #parser.add_argument('timestamp', type=int, required=False)
    parser.add_argument('running_score', type=int, required=False)
    
    def get(self):
        data = Scoring.parser.parse_args()
        scoring = ScoringModel.find_by_uuid(data['uuid'])
        #result = NutrientModel.query.filter_by(id = idx).first()
        
        if scoring:
            return scoring.running_score
        return {'message' : 'score not found'},404
    
    def put(self):
        data = Scoring.parser.parse_args()
        ct = datetime.datetime.now()
        ts= str(ct.year)+"-"+str(ct.month)+"-"+str(ct.day)+" "+str(ct.hour)+':'+str(ct.minute)+':'+str(ct.second)
        if UserModel.find_by_uuid(data['uuid']):
            if ScoringModel.find_by_uuid(data['uuid'])==None:
                uuid_1 = data['uuid']
                
                scoring = ScoringModel(str(uuid_1),
                                         data['meal_count'],
                                         ts,
                                         data['running_score'])
                
                try:
                    scoring.save_to_db()
                except:
                    return {"message": "An error occurred creating the nutrient."}, 500 # Internal Server Error
            else:
                scoring = ScoringModel.find_by_uuid(data['uuid'])
                if data['meal_count']:
                    scoring.meal_count = data['meal_count']
                
                scoring.timestamp = ts
                if data['running_score']:
                    scoring.running_score = data['running_score']
                try:
                    scoring.save_to_db()
                except:
                    return {"message": "An error occurred creating the nutrient."}, 500 # Internal Server Error

            return scoring.uuid, 201
        
class ScoringList(Resource):
    def get(self):
        return {'scorings': [scoring.json() for scoring in ScoringModel.query.all()]}
            
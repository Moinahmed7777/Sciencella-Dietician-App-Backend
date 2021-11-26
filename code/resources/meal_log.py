# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:43:56 2021

@author: Necro
"""

from flask_restful import Resource, reqparse
from models.user import UserModel
from models.meal_log import Meal_log
#import uuid


class MealRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('uuid',
    type=str,
    help="This field cannot be blank."
    )
    parser.add_argument('date',
    type=str
    #required=True,
    #help="This field cannot be blank."
    )
    parser.add_argument('time',
    type=str
    #required=True,
    #help="This field cannot be blank."
    )
    

    def get(self):
        data = MealRegister.parser.parse_args()
        #
        if data['time']==None:
            if data['date']==None:
                meallog = Meal_log.find_by_uuid(data['uuid'])
            else:
                meallog = Meal_log.find_by_uuid_date(data['uuid'],data['date'])
        elif data['time']!=None:
            if data['date']==None:
                
                meallog = Meal_log.find_by_uuid_time(data['uuid'],data['time'])
            else:
                meallog = Meal_log.find_by_uuid_datetime(data['uuid'],data['date'],data['time'])
        
        #print("llalalaalaasdasdasdasdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",data['time'])
            
        #print(meallog)
        if meallog:
            return {'meal_logs': [meallog.json() for meallog in meallog]}
        return {'message': 'uuid+timestamp entry not found'}, 404

    def post(self):
        pass
        #data = MealRegister.parser.parse_args()

        #if MealRegister.find_by_email(data['email']):
            #return {"message": "A user with that name already exists."}, 400
        
        #print(str(uuid.uuid4()))
        #dm = 
        #dm_string = 

        #mealreg = MealRegister(data['uuid'], ,data['timestamp'])

        #try:
            #user.save_to_db()
        #except:
            #return {"message": "An error occurred creating the user."}, 500 # Internal Server Error

        #return user.uuid, 201

    def delete(self):
        data = MealRegister.parser.parse_args()
        
        user = UserModel.find_by_email(data['email'])
        if user:
            user.delete_from_db()
        return {'message': 'User deleted.'}


class UserList(Resource):
    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 01:57:54 2021

@author: Necro
"""

from models.dummy_DM import DM_Model
from flask_restful import Resource, reqparse,abort,fields,marshal_with,request
from models.user import UserModel
from models.meal_log import Meal_log
from usda import foodret
import uuid
import datetime
from foodpred import pred

class DM_register(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uuid',
    type=str
    )
    parser.add_argument('food',
    type=str
    )
    """
    parser.add_argument('energy', type=int, required=False)
    parser.add_argument('protein', type=int, required=False)
    parser.add_argument('total_lipid', type=int, required=False)
    parser.add_argument('carbohydrate', type=int, required=False)
    parser.add_argument('fiber', type=int, required=False)
    parser.add_argument('sugar', type=int, required=False)
    parser.add_argument('calcium', type=int, required=False)
    parser.add_argument('iron', type=int, required=False)
    parser.add_argument('sodium', type=int, required=False)
    #parser.add_argument('magnesium', type=int, required=False)
    parser.add_argument('vitamin_a', type=int, required=False)
    parser.add_argument('vitamin_c', type=int, required=False)
    parser.add_argument('vitamin_d', type=int, required=False)
    parser.add_argument('saturated_fatty_acid', type=int, required=False)
    parser.add_argument('monounsaturated_fatty_acid', type=int, required=False)
    parser.add_argument('polyunsaturated_fatty_acid', type=int, required=False)
    parser.add_argument('cholesterol', type=int, required=False)
    """

    
    def get(self):
        data = DM_register.parser.parse_args()
        nutrient = DM_Model.find_by_uuid(data['uuid'])
        #result = NutrientModel.query.filter_by(id = idx).first()
        
        if nutrient:
            return nutrient.json()
        return {'message' : 'physical not found'},404
        
        
    ## if uuid exists in the UserModel then NutrientModel is created with that uuid, 
    #  if uuid exists in the UserModel and also in the NutrientModel then it updates according to the args passed. 
    
    ##note:for DM_Model if attribute doesnt exist put 0 in that field
    
    def put(self):
        data1 = DM_register.parser.parse_args()
        ct = datetime.datetime.now()
        if UserModel.find_by_uuid(data1['uuid']):
            if DM_Model.find_by_uuid(data1['uuid'])==None:
                uuid_1 = data1['uuid']
                
                #comment this section 
                file = request.files['image']
                prediction = pred(file)
                
                food = prediction.replace("_", " ")
                print(food)
                #
                
                #uncomment this to insert food manually
                #food = data1['food'].replace("_", " ") #to replace "_" with emptyspace
                
                data = foodret(food)
                ts = str(ct.year)+"-"+str(ct.month)+"-"+str(ct.day)
                nutrient = DM_Model(str(uuid_1),
                                         data['energy'],
                                         data['protein'],
                                         data['total_lipid'],
                                         data['carbohydrate'],
                                         data['fiber'],
                                         data['sugar'],
                                         data['calcium'],
                                         data['iron'],
                                         data['sodium'],
                                         #data['magnesium'],
                                         data['vitamin_a'],
                                         data['vitamin_c'],
                                         data['vitamin_d'],
                                         data['saturated_fatty_acid'],
                                         data['monounsaturated_fatty_acid'],
                                         data['polyunsaturated_fatty_acid'],
                                         data['cholesterol'],
                                         str(1),
                                         ts)
                
                ##
                nutrient_str = str(data['energy']) + "," + str(data['protein']) + "," + str(data['total_lipid']) + ","+ str(data['carbohydrate']) + ","+ str(data['fiber']) + ","+ str(data['sugar']) + "," + str(data['calcium']) + "," + str(data['iron']) + "," + str(data['sodium']) + "," + str(data['vitamin_a']) + "," + str(data['vitamin_c']) + "," + str(data['vitamin_d']) + "," + str(data['saturated_fatty_acid']) + "," + str(data['monounsaturated_fatty_acid']) + "," + str(data['polyunsaturated_fatty_acid']) + "," + str(data['cholesterol'])
                print(nutrient_str)
                
                tstime=str(ct.hour)+':'+str(ct.minute)
                meal = Meal_log(str(uuid.uuid4()),data1['uuid'],nutrient_str ,ts,tstime,food)
                
                ##
                try:
                    nutrient.save_to_db()
                    meal.save_to_db()
                except:
                    return {"message": "An error occurred creating the nutrient."}, 500 # Internal Server Error
            else:
                nutrient = DM_Model.find_by_uuid(data1['uuid'])
                
                #comment this section 
                file = request.files['image']
                prediction = pred(file)
                #food = data1['food'].replace("_", " ") #to replace "_" with emptyspace
                food = prediction.replace("_", " ")
                print(food)
                #
                
                #uncomment to insert food manually
                #food = data1['food'].replace("_", " ")  #to replace "_" with emptyspace
                
                data = foodret(food)
                #data = foodret(data1['food'])
                
                ts = str(ct.year)+"-"+str(ct.month)+"-"+str(ct.day)
                if nutrient.date != ts:
                    nutrient.energy,nutrient.protein,nutrient.total_lipid,nutrient.carbohydrate,nutrient.sugar,nutrient.calcium,nutrient.iron,nutrient.sodium,nutrient.vitamin_a,nutrient.vitamin_c,nutrient.vitamin_d,nutrient.saturated_fatty_acid,nutrient.monounsaturated_fatty_acid,nutrient.polyunsaturated_fatty_acid,nutrient.cholesterol,nutrient.meal_count=[0]*16
                    nutrient.date = ts
                if data['energy']:
                    nutrient.energy = float(nutrient.energy) + float(data['energy'])
                if data['protein']:
                    nutrient.protein = float(nutrient.protein) + float(data['protein'])
                if data['total_lipid']:
                    nutrient.total_lipid = float(nutrient.total_lipid) + float(data['total_lipid'])
                if data['carbohydrate']:
                    nutrient.carbohydrate = float(nutrient.carbohydrate) + float(data['carbohydrate'])
                if data['sugar']:
                    nutrient.sugar = float(nutrient.sugar) + float(data['sugar'])
                if data['calcium']:
                    nutrient.calcium = float(nutrient.calcium) + float(data['calcium'])
                if data['iron']:
                    nutrient.iron = float(nutrient.iron) + float(data['iron'])
                if data['sodium']:
                    nutrient.sodium = float(nutrient.sodium) + float(data['sodium'])
                if data['vitamin_a']:
                    nutrient.vitamin_a = float(nutrient.vitamin_a) + float(data['vitamin_a'])
                if data['vitamin_c']:
                    nutrient.vitamin_c = float(nutrient.vitamin_c) + float(data['vitamin_c'])
                if data['vitamin_d']:
                    nutrient.vitamin_d = float(nutrient.vitamin_d) + float(data['vitamin_d'])
                if data['saturated_fatty_acid']:
                    nutrient.saturated_fatty_acid = float(nutrient.saturated_fatty_acid) + float(data['saturated_fatty_acid'])
                if data['monounsaturated_fatty_acid']:
                    nutrient.monounsaturated_fatty_acid = float(nutrient.monounsaturated_fatty_acid) + float(data['monounsaturated_fatty_acid'])
                if data['polyunsaturated_fatty_acid']:
                    nutrient.polyunsaturated_fatty_acid = float(nutrient.polyunsaturated_fatty_acid) + float(data['polyunsaturated_fatty_acid'])
                if data['cholesterol']:
                    nutrient.cholesterol = float(nutrient.cholesterol) + float(data['cholesterol'])
                
                nutrient.meal_count = int(nutrient.meal_count)+1
                
                ##
                nutrient_str = str(data['energy']) + "," + str(data['protein']) + "," + str(data['total_lipid']) + ","+ str(data['carbohydrate']) + ","+ str(data['fiber']) + ","+ str(data['sugar']) + "," + str(data['calcium']) + "," + str(data['iron']) + "," + str(data['sodium']) + "," + str(data['vitamin_a']) + "," + str(data['vitamin_c']) + "," + str(data['vitamin_d']) + "," + str(data['saturated_fatty_acid']) + "," + str(data['monounsaturated_fatty_acid']) + "," + str(data['polyunsaturated_fatty_acid']) + "," + str(data['cholesterol'])
                print(nutrient_str)
                x = nutrient_str.split(",")
                print(x)
                ts = str(ct.year)+"-"+str(ct.month)+"-"+str(ct.day)
                tstime=str(ct.hour)+':'+str(ct.minute)
                meal = Meal_log(str(uuid.uuid4()),data1['uuid'],nutrient_str ,ts,tstime,food)
                
                ##
                
                try:
                    nutrient.save_to_db()
                    meal.save_to_db()
                except:
                    return {"message": "An error occurred creating the nutrient."}, 500 # Internal Server Error

        return meal.json(), 201
    
    

class DM_List(Resource):
    def get(self):
        return {'dms': [dm.json() for dm in DM_Model.query.all()]}


class DM_delete(Resource):
    #pass uuid from the NutrientModel to delete
    def delete(self):
        data = DM_register.parser.parse_args()
        nutrient = DM_Model.find_by_uuid(data['uuid'])
        #result = NutrientModel.query.filter_by(id = idx).first()
        
        if nutrient:
            nutrient.delete_from_db()
        return {'message' : 'physical deleted'},404
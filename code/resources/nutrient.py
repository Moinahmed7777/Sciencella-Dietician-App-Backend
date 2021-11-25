"""
note:
get,post,delete works
problem with update
"""

from models.nutrient import NutrientModel
from flask_restful import Resource, reqparse,abort,fields,marshal_with
from models.user import UserModel
import uuid

class Nutrient(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uuid',
    type=str
    )
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

    
    def get(self):
        data = Nutrient.parser.parse_args()
        nutrient = NutrientModel.find_by_uuid(data['uuid'])
        #result = NutrientModel.query.filter_by(id = idx).first()
        
        if nutrient:
            return nutrient.json()
        return {'message' : 'physical not found'},404
        
        
    ## if uuid exists in the UserModel then NutrientModel is created with that uuid, 
    #  if uuid exists in the UserModel and also in the NutrientModel then it updates according to the args passed. 
    def put(self):
        data = Nutrient.parser.parse_args()
        if UserModel.find_by_uuid(data['uuid']):
            if NutrientModel.find_by_uuid(data['uuid'])==None:
                uuid_1 = data['uuid']
                nutrient = NutrientModel(str(uuid_1),
                                         data['energy'],
                                         data['protein'],
                                         data['total_lipid'],
                                         data['carbohydrate'],
                                         data['fiber'],
                                         data['sugar'],
                                         data['calcium'],
                                         data['iron'],
                                         data['sodium'],
                                         data['vitamin_a'],
                                         data['vitamin_c'],
                                         data['vitamin_d'],
                                         data['saturated_fatty_acid'],
                                         data['monounsaturated_fatty_acid'],
                                         data['polyunsaturated_fatty_acid'],
                                         data['cholesterol'])
                try:
                    nutrient.save_to_db()
                except:
                    return {"message": "An error occurred creating the nutrient."}, 500 # Internal Server Error
            else:
                nutrient = NutrientModel.find_by_uuid(data['uuid'])
                if data['energy']:
                    nutrient.energy = data['energy']
                if data['protein']:
                    nutrient.protein = data['protein']
                if data['total_lipid']:
                    nutrient.total_lipid = data['total_lipid']
                if data['carbohydrate']:
                    nutrient.carbohydrate = data['carbohydrate']
                if data['sugar']:
                    nutrient.sugar = data['sugar']
                if data['calcium']:
                    nutrient.calcium = data['calcium']
                if data['iron']:
                    nutrient.iron = data['iron']
                if data['sodium']:
                    nutrient.sodium = data['sodium']
                #if data['magnesium']:
                    #nutrient.magnesium = data['magnesium']
                if data['vitamin_a']:
                    nutrient.vitamin_a = data['vitamin_a']
                if data['vitamin_c']:
                    nutrient.vitamin_c = data['vitamin_c']
                if data['vitamin_d']:
                    nutrient.vitamin_d = data['vitamin_d']
                if data['saturated_fatty_acid']:
                    nutrient.saturated_fatty_acid = data['saturated_fatty_acid']
                if data['monounsaturated_fatty_acid']:
                    nutrient.monounsaturated_fatty_acid = data['monounsaturated_fatty_acid']
                if data['polyunsaturated_fatty_acid']:
                    nutrient.polyunsaturated_fatty_acid = data['polyunsaturated_fatty_acid']
                if data['cholesterol']:
                    nutrient.cholesterol = data['cholesterol']
                try:
                    nutrient.save_to_db()
                except:
                    return {"message": "An error occurred creating the nutrient."}, 500 # Internal Server Error

        return nutrient.uuid, 201
    
    

class NutrientList(Resource):
    def get(self):
        return {'nutrients': [nutrient.json() for nutrient in NutrientModel.query.all()]}


class Nutrient_delete(Resource):
    #pass uuid from the NutrientModel to delete
    def delete(self):
        data = Nutrient.parser.parse_args()
        nutrient = NutrientModel.find_by_uuid(data['uuid'])
        #result = NutrientModel.query.filter_by(id = idx).first()
        
        if nutrient:
            nutrient.delete_from_db()
        return {'message' : 'physical deleted'},404
        
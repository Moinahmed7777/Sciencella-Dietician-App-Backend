# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 02:10:19 2021

@author: Necro
"""

from flask_restful import Resource, reqparse,abort,fields,marshal_with
from models.nutrient import NutrientModel
from models.dummy_DM import DM_Model

class meal_calc(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uuid',
    type=str
    )
    
    def get(self):
        data = meal_calc.parser.parse_args()
        req = NutrientModel.find_by_uuid(data['uuid'])
        intake = DM_Model.find_by_uuid(data['uuid'])
        
        cummulative_score=100
        if intake == None:
            return 0
        #energy
        min_e = float(req.energy)*(.80)
        max_e = float(req.energy)*(1.30)
        if float(intake.energy)<=min_e or float(intake.energy)>=max_e:
            print("e")
            cummulative_score = cummulative_score - 6.25
        
        #protein
        min_p = float(req.protein)*(.80)
        max_p = float(req.protein)*(1.30)
        if float(intake.protein)<=min_p or float(intake.protein)>=max_p:
            print("p")
            cummulative_score = cummulative_score - 6.25
        
        #total_lipid
        min_tl = float(req.total_lipid)*(.80)
        max_tl = float(req.total_lipid)*(1.30)
        if float(intake.total_lipid)<=min_tl or float(intake.total_lipid)>=max_tl:
            print("tl")
            cummulative_score = cummulative_score - 6.25
        
        #carbohydrate
        min_carb = float(req.carbohydrate)*(.80)
        max_carb = float(req.carbohydrate)*(1.30)
        if float(intake.carbohydrate)<=min_carb or float(intake.carbohydrate)>=max_carb:
            print("carb")
            cummulative_score = cummulative_score - 6.25
        
        #fiber
        min_f = float(req.fiber)*(.80)
        max_f = float(req.fiber)*(1.30)
        if float(intake.fiber)<=min_f or float(intake.fiber)>=max_f:
            print("fib")
            cummulative_score = cummulative_score - 6.25
        
        #sugar
        min_s = float(req.sugar)*(.80)
        max_s = float(req.sugar)*(1.30)
        if float(intake.sugar)<=min_s or float(intake.sugar)>=max_s:
            print("sug")
            cummulative_score = cummulative_score - 6.25
        
        #calcium
        min_ca = float(req.calcium)*(.80)
        max_ca = float(req.calcium)*(1.30)
        if float(intake.calcium)<=min_ca or float(intake.calcium)>=max_ca:
            print("calc")
            cummulative_score = cummulative_score - 6.25
        
        #iron
        min_i = float(req.iron)*(.80)
        max_i = float(req.iron)*(1.30)
        if float(intake.iron)<=min_i or float(intake.iron)>=max_i:
            print("iron")
            cummulative_score = cummulative_score - 6.25
        
        #sodium
        min_sod = float(req.sodium)*(.80)
        max_sod = float(req.sodium)*(1.30)
        if float(intake.sodium)<=min_sod or float(intake.sodium)>=max_sod:
            print("sod")
            cummulative_score = cummulative_score - 6.25
        
        #magnesium
        #min_mag = float(req.magnesium)*(.80)
        #max_mag = float(req.magnesium)*(1.30)
        #if float(intake.energy)<=min_mag or float(intake.energy)>=max_mag:
            #cummulative_score = cummulative_score + 6.25
        
        #vitamin_a
        min_va = float(req.vitamin_a)*(.80)
        max_va = float(req.vitamin_a)*(1.30)
        if float(intake.vitamin_a)<=min_va or float(intake.vitamin_a)>=max_va:
            print("vita")
            cummulative_score = cummulative_score - 6.25
        
        #vitamin_c
        min_vc = float(req.vitamin_c)*(.80)
        max_vc = float(req.vitamin_c)*(1.30)
        if float(intake.vitamin_c)<=min_vc or float(intake.vitamin_c)>=max_vc:
            print("vitc")
            cummulative_score = cummulative_score - 6.25
        
        #vitamin_d
        min_vd = float(req.vitamin_d)*(.80)
        max_vd = float(req.vitamin_d)*(1.30)
        if float(intake.vitamin_d)<=min_vd or float(intake.vitamin_d)>=max_vd:
            print("vitd")
            cummulative_score = cummulative_score - 6.25
        
        #saturated_fatty_acid
        min_sfa = float(req.saturated_fatty_acid)*(.80)
        max_sfa = float(req.saturated_fatty_acid)*(1.30)
        if float(intake.saturated_fatty_acid)<=min_sfa or float(intake.saturated_fatty_acid)>=max_sfa:
            print("sfa")
            cummulative_score = cummulative_score - 6.25
        
        #monounsaturated_fatty_acid
        min_mfa = float(req.monounsaturated_fatty_acid)*(.80)
        max_mfa = float(req.monounsaturated_fatty_acid)*(1.30)
        if float(intake.monounsaturated_fatty_acid)<=min_mfa or float(intake.monounsaturated_fatty_acid)>=max_mfa:
            print("mfa")
            cummulative_score = cummulative_score - 6.25
        
        #polyunsaturated_fatty_acid
        min_pfa = float(req.polyunsaturated_fatty_acid)*(.80)
        max_pfa = float(req.polyunsaturated_fatty_acid)*(1.30)
        if float(intake.polyunsaturated_fatty_acid)<=min_pfa or float(intake.polyunsaturated_fatty_acid)>=max_pfa:
            print("pfa")
            cummulative_score = cummulative_score - 6.25
            
        #cholesterol
        min_chol = float(req.cholesterol)*(.80)
        max_chol = float(req.cholesterol)*(1.30)
        if float(intake.cholesterol)<=min_chol or float(intake.cholesterol)>=max_chol:
            print("chol")
            cummulative_score = cummulative_score - 6.25
        
        #result = NutrientModel.query.filter_by(id = idx).first()
        print(cummulative_score)
        if req==None:
            return {'message' : 'nutrient for that uuid not found'},404
        if intake==None:
            return {'message' : 'dailymeal for that uuid not found'},404
        return cummulative_score
        #return {'message' : 'physical not found'},404
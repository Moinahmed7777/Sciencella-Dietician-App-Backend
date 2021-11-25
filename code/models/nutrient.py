from db import db
from sqlalchemy import Table, Column, Integer, ForeignKey


class NutrientModel(db.Model):
    __tablename__ = 'nutrient'

    uuid = db.Column(db.String(36),primary_key=True)
    energy = db.Column(db.Integer, nullable=False)
    protein = db.Column(db.Integer, nullable=False)
    total_lipid = db.Column(db.Integer, nullable=False)
    carbohydrate = db.Column(db.Integer, nullable=False)
    fiber = db.Column(db.Integer, nullable=False)
    sugar = db.Column(db.Integer, nullable=False)
    calcium = db.Column(db.Integer, nullable=False)
    iron = db.Column(db.Integer, nullable=False)
    sodium = db.Column(db.Integer, nullable=False)
    #magnesium = db.Column(db.Integer, nullable=False)
    vitamin_a = db.Column(db.Integer, nullable=False)
    vitamin_c = db.Column(db.Integer, nullable=False)
    vitamin_d = db.Column(db.Integer, nullable=False)
    saturated_fatty_acid = db.Column(db.Integer, nullable=False)
    monounsaturated_fatty_acid = db.Column(db.Integer, nullable=False)
    polyunsaturated_fatty_acid = db.Column(db.Integer, nullable=False)
    cholesterol = db.Column(db.Integer, nullable=False)
    
    #user_id = db.Column(db.Integer, ForeignKey('user.uuid'), nullable=False)
    
    
    def __init__(self,uuid,energy, protein, total_lipid, carbohydrate, fiber, sugar,
                 calcium, iron, sodium, vitamin_a, vitamin_c, vitamin_d,
                 saturated_fatty_acid, monounsaturated_fatty_acid, polyunsaturated_fatty_acid, cholesterol
                 ):
        self.uuid=uuid
        self.energy = energy
        self.protein = protein
        self.total_lipid = total_lipid
        self.carbohydrate = carbohydrate
        self.fiber = fiber
        self.sugar = sugar
        self.calcium = calcium
        self.iron = iron
        self.sodium = sodium
        #self.magnesium = magnesium
        self.vitamin_a = vitamin_a
        self.vitamin_c = vitamin_c
        self.vitamin_d = vitamin_d
        self.saturated_fatty_acid = saturated_fatty_acid
        self.monounsaturated_fatty_acid = monounsaturated_fatty_acid
        self.polyunsaturated_fatty_acid = polyunsaturated_fatty_acid
        self.cholesterol = cholesterol
        
    def json(self):
        return {'uuid': self.uuid,
                
                #'id': self.id,
                
                'energy': self.energy,
                'protein': self.protein,
                'total_lipid': self.total_lipid,
                'carbohydrate': self.carbohydrate,
                'fiber': self.fiber,
                'sugar': self.sugar,
                'calcium': self.calcium,
                'iron': self.iron,
                'sodium': self.sodium,
                #'magnesium': self.magnesium,
                'vitamin_a': self.vitamin_a,
                'vitamin_c': self.vitamin_c,
                'vitamin_d': self.vitamin_d,
                'saturated_fatty_acid': self.saturated_fatty_acid,
                'monounsaturated_fatty_acid': self.monounsaturated_fatty_acid,
                'polyunsaturated_fatty_acid': self.polyunsaturated_fatty_acid,
                'cholesterol': self.cholesterol
                
                }
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    @classmethod
    def find_by_uuid(cls,uuid):
        return cls.query.filter_by(uuid=uuid).first()
    
    
        
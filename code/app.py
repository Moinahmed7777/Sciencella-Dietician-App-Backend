from flask import Flask
from flask_restful import Api
#from flask_mysqldb import MySQL
from resources.user import UserRegister, UserList , Update_User
from resources.physical import Physical, PhysicalList
from resources.nutrient import Nutrient, NutrientList, Nutrient_delete
from resources.scoring_table import Scoring, ScoringList
from resources.dummy_DM import DM_register, DM_List,DM_delete
from resources.meal_score import meal_calc
from resources.meal_score_count import mealcalc_count
from resources.meal_log import MealRegister
from foodpred import pred
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://admin:8fmH8iuKLEBEHnaXWXdF@development-db.c7heidgc11xf.us-east-1.rds.amazonaws.com"
#app.config["SQLALCHEMY_DATABASE_URI"]= 'mysql://admin:8fmH8iuKLEBEHnaXWXdF@development-db.c7heidgc11xf.us-east-1.rds.amazonaws.com/sciencella'
#app.config["SQLALCHEMY_DATABASE_URI"]= 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='admin', password='8fmH8iuKLEBEHnaXWXdF', server='development-db.c7heidgc11xf.us-east-1.rds.amazonaws.com', database='sciencella')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['MYSQL_HOST'] = 'development-db.c7heidgc11xf.us-east-1.rds.amazonaws.com' 
#app.config['MYSQL_USER'] = 'admin'
#app.config['MYSQL_PASSWORD'] = '8fmH8iuKLEBEHnaXWXdF'
#app.config['MYSQL_DB'] = 'sciencella'
#api = MySQL(app)


api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()
    #db.drop_all()


api.add_resource(UserRegister, '/user')
api.add_resource(UserList, '/users')

api.add_resource(Update_User, '/update_user')

api.add_resource(Physical, '/physical')
api.add_resource(PhysicalList, '/physicals')

api.add_resource(Nutrient, '/nutrient')
api.add_resource(NutrientList, '/nutrients')
api.add_resource(Nutrient_delete, '/nutrient_delete')

api.add_resource(Scoring, '/scoring')
api.add_resource(ScoringList, '/scorings')

api.add_resource(DM_register, '/dm')
api.add_resource(DM_List, '/dms')
api.add_resource(DM_delete, '/dm_delete')

api.add_resource(meal_calc, '/meal_calc')

api.add_resource(MealRegister, '/meal')

api.add_resource(mealcalc_count, '/mealcalc_count')
#api.add_resource(pred, '/pred')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)

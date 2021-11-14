from flask import Flask
from flask_restful import Api

from resources.user import UserRegister, UserList
from resources.physical import Physical, PhysicalList
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://admin:8fmH8iuKLEBEHnaXWXdF@development-db.c7heidgc11xf.us-east-1.rds.amazonaws.com"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UserRegister, '/user')
api.add_resource(UserList, '/users')
api.add_resource(Physical, '/physical')
api.add_resource(PhysicalList, '/physicals')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)

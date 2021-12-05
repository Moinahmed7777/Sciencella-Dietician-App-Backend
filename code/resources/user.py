from flask_restful import Resource, reqparse
from models.user import UserModel
import uuid


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('uuid',
    type=str,
    )
    parser.add_argument('first_name',
    type=str
    )
    parser.add_argument('last_name',
    type=str
    )
    parser.add_argument('email',
    type=str
    )

    def get(self):
        data = UserRegister.parser.parse_args()
        
        user = UserModel.find_by_uuid(data['uuid'])
        if user:
            return user.json()
        return {'message': 'User not found'}, 404

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {"message": "A user with that name already exists."}, 400
        
        print(str(uuid.uuid4()))
        '''
        user = UserModel.find_by_uuid(data['uuid'])
        if user != None:
            if data['first_name']:
                user.first_name = data['first_name']
            if data['last_name']:
                user.last_name = data['last_name']   
        else:
        '''
        user = UserModel(str(uuid.uuid4()), data['first_name'], data['last_name'], data['email'])

        try:
            user.save_to_db()
        except:
            return {"message": "An error occurred creating the user."}, 500 # Internal Server Error

        return user.uuid, 201

    def delete(self):
        data = UserRegister.parser.parse_args()
        
        user = UserModel.find_by_email(data['email'])
        if user:
            user.delete_from_db()
        return {'message': 'User deleted.'}


class UserList(Resource):
    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}

class Update_User(Resource):
    up_parser = reqparse.RequestParser()
    up_parser.add_argument('uuid',
    type=str
    )
    up_parser.add_argument('first_name',
    type=str
    )
    up_parser.add_argument('last_name',
    type=str
    )
    
    def put(self):
        data = Update_User.up_parser.parse_args()
        user = UserModel.find_by_uuid(data['uuid'])
        if user != None:
            if data['first_name']:
                user.first_name = data['first_name']
            if data['last_name']:
                user.last_name = data['last_name']   
        else:
            return {"message": "A user with that uuid doesn't exists."}, 400
        try:
            user.save_to_db()
        except:
            return {"message": "An error occurred creating the user."}, 500 # Internal Server Error

        return user.uuid, 201

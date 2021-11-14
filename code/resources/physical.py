from flask_restful import Resource, reqparse
from models.physical import PhysicalModel

class Physical(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('uuid',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('age',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('gender',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('weight',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('height',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )


    def get(self):
        data = Physical.parser.parse_args()
        
        physical = PhysicalModel.find_by_uuid(data['uuid'])
        if physical:
            return physical.json()
        return {'message': 'Physical not found'}, 404

    def delete(self):
        data = Physical.parser.parse_args()
        
        physical = PhysicalModel.find_by_uuid(data['uuid'])
        if physical:
            physical.delete_from_db()
        return {'message': 'Physical deleted.'}

    def put(self):
        data = Physical.parser.parse_args()
        uuid = data['uuid']

        physical = PhysicalModel.find_by_uuid(uuid)

        if physical is None:
            physical = PhysicalModel(uuid,
                                    data['age'],
                                    data['gender'],
                                    data['weight'],
                                    data['height']
                                    )
        else:
            physical.age = data['age']
            physical.gender = data['gender']
            physical.weight = data['weight']
            physical.height = data['height']

        physical.save_to_db()

        return physical.json()


class PhysicalList(Resource):
    def get(self):
        return {'physical': [physical.json() for physical in PhysicalModel.query.all()]}

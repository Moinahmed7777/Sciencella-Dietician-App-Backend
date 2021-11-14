from db import db

class PhysicalModel(db.Model):
    __tablename__ = 'physical'

    uuid = db.Column(db.String(36), primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)

    #uuid = db.Column(db.Integer, db.ForeignKey('user.uuid'), unique=True)
    #user = db.relationship('UserModel')

    def __init__(self, uuid, age, gender, weight, height):
        self.uuid = uuid
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height

    def json(self):
        return {'age': self.age,
                'gender': self.gender,
                'weight': self.weight,
                'height': self.height
                }

    @classmethod
    def find_by_uuid(cls, uuid):
        return cls.query.filter_by(uuid=uuid).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

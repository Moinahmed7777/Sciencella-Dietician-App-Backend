from db import db



class UserModel(db.Model):
    __tablename__ = 'user'

    uuid = db.Column(db.String(36), primary_key=True)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(80), unique=True, index=True)

    #physical = db.relationship('PhysicalModel', backref='usermodel', uselist=False)

    def __init__(self, uuid, first_name, last_name, email):
        self.uuid = uuid
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def json(self):
        return {'uuid': self.uuid,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email
                }

    @classmethod
    def find_by_name(cls, first_name, last_name):
        return cls.query.filter_by(first_name=first_name, last_name=last_name).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_uuid(cls, uuid):
        return cls.query.filter_by(uuid=uuid).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

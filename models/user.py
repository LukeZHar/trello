from init import db, ma
from marshmallow import fields

class User(db.Model):
    # NAme of the table
    __tablename__ = 'users'

    # Attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    cards = db.relationship('Card', back_populates='user')
    
class UserSchema(ma.Schema):
    class Meta:
        cards = fields.List(fields.Nested('CardSchema', exclude=['user']))

        fields = ('id', 'name', 'email', 'password', 'is_admin', 'cards')

# To handle a single user object
user_schema = UserSchema(exclude=['password'])

# To handle a list of user objects
users_schema = UserSchema(many=True, exclude=['password'])
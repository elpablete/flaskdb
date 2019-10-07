from app import api
from flask_restplus import Resource, fields
from requests import request

from app.models import User
from app.schemas import UserSchema


api_ns = api.namespace('api', description='API Project')

# this will be used to add parameter in swagger for inserting/updating record
userSwagger = api.model('User', {
    'username': fields.String(required=True, description="User's username"),
    'email': fields.String(required=True, description="User's email address"),
    'description': fields.String(required=False, description="User's self description"),
})


@api_ns.route("/users")
class UserList(Resource):
    # you can add additional Swagger response information here
    @api.doc(
        responses=
        {
            200: 'OK',
            400: 'Invalid Argument',
            500: 'Mapping Key Error',
        })
    
    def get(self):
        users = User.query.all()
        result = []
        schema = UserSchema()
        for user in users:
            result.append(schema.dump(user))
        return {
            "data": result
        }



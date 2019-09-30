from flask_restful import Resource, reqparse
from models import TipoUserModel

parser = reqparse.RequestParser()

class Insert(Resource):
    def post(self):
        parser.add_argument('tipo',help='tipo missing', required=True)
        data = parser.parse_args()
        new_tipo = TipoUserModel(
            tipo=data['tipo']
        )
        try:
            new_tipo.save_to_db()
            return {
                'message': 'User type {}  was created'.format(data['tipo'])
            }
        except:
            return {'message' : 'Something went wrong'}, 500

class Update(Resource):
    def post(self):
        parser.add_argument('id',help='id missing', required=True)
        parser.add_argument('tipo',help='tipo missing', required=True)
        data = parser.parse_args()
        current_type = TipoUserModel.find_type_by_id(data['id'])
        if( not current_type ):
            { 'message': 'User type doesnt exists' }
        try:
            current_type.tipo = data['tipo']
            current_type.save_to_db()
            return { 'message': 'User type updated' }
        except:
            return { 'message': 'Cannot update user type' }
from flask_restful import Resource, reqparse
from models import UserModel
from flask_jwt_extended import (jwt_manager,create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

parser = reqparse.RequestParser()
class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        if (UserModel.find_by_username(data['username'])):
            return {'message': 'User {} already exists'.format(data['username'])}

        new_user = UserModel(
            username=data['username'],
            password=UserModel.generate_hash(data['password']),
            nombre=data['nombre'],
            telefono=data['telefono'],
            id_tipo=data['id_tipo']
        )
        try:
            new_user.save_to_db()
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity = data['username'])

            return {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
            }
        except:
            return {'message': 'Algo salio mal ):'}, 500

class UserLogin(Resource):
     def post(self):
        parser.add_argument('usrId',help='usrId missing', required=True)
        parser.add_argument('pwd',help='pwd missing', required=True)
        parser.add_argument('noTel',help='noTel missing', required=True)
        parser.add_argument('correo',help='correo missing', required=True)
        data = parser.parse_args()
        current_user =  UserModel.find_by_username(data['usrId'])
        if (not current_user):
            return {'message': 'Wrong credentials'}
        if (current_user.verify_hash(data['pwd'],current_user.pwd)):
            current_user.noTel = data['noTel']
            current_user.correo = data['correo']
            current_user.save_to_db()
            jsonUser = {
                'usrId': current_user.usrId,
                'nomUsr': current_user.nomUsr,
                'noTel': current_user.noTel,
                'correo': current_user.correo,
                'rfcTutor': current_user.rfcTutor,
                'fechaAlta': current_user.fechaAlta,
                'idTipoUsr': current_user.idTipoUsr
            }
            access_token = create_access_token(identity=jsonUser)
            #access_token = create_access_token(identity=data['usrId'])
            refresh_token = create_refresh_token(identity = jsonUser)
            return {
                 'message':'logged in as {} '.format(current_user.usrId),
                 'access_token': access_token,
                 'refresh_token': refresh_token
            }

        else:
            return { 'message': 'Wrong credentials' }
    
class UserUpdate(Resource):
    #@jwt_required #Uncomment this line to disable JSON WEB TOKEN Auth.
    def post(self):
        data = parser.parse_args()
        current = UserModel.find_by_username(data['username'])
        if (not current):
            return {'message': 'User doesnt exists'}
        try:
            current.telefono = data['telefono']
            current.id_tipo = data['id_tipo']
            current.password = UserModel.generate_hash(data['password'])
            current.nombre = data['nombre']
            current.save_to_db()            
            return {'message': 'user updated'}
        except:
            return {'message': 'Cannot update user'}, 500
        

      
class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout'}
      
      
class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}
      
      
class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}
      
      
class AllUsers(Resource):
    def get(self):
        return {'message': 'List of users'}

    def delete(self):
        return {'message': 'Delete all users'}
      
      
class SecretResource(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }
     
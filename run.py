from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)
app.config['UPLOAD_FOLDER'] = 'images'


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/avisos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'advices'
app.config['JWT_SECRET_KEY'] = 'tok_avisos_merife'

jwt = JWTManager(app)

db = SQLAlchemy(app)

import views, models, resources

# User endpoints
api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')
api.add_resource(resources.UserUpdate,'/users/update')

from controllers import tipouser_controller as UserTypeController
# TipoUser Endpoints
api.add_resource(UserTypeController.Insert, '/tipoUser/insert')
api.add_resource(UserTypeController.Update, '/tipoUser/update')

from controllers import avisos_controller as AvisosController
api.add_resource(AvisosController.InsertAviso, '/avisos/insert')

@app.before_first_request
def create_tables():
    db.create_all()
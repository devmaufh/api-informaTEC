from run import db
from flask_restful import Resource, reqparse
from passlib.hash import pbkdf2_sha256 as sha256

class AlumnosModel(db.Model):
    __tablename__ = 'alumnos'
    no_control = db.Column(db.String(10), primary_key = True, unique=True)
    nombre = db.Column(db.String(70), nullable = False)
    telefono = db.Column(db.String(10), nullable = False)
    correo = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(250), nullable = False)
    id_carrera = db.Column(db.Integer, db.ForeignKey('carreras.id'))
    semestre = db.Column(db.Integer, nullable = False)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    class Insert(Resource):
        def post(self):
            return {'message': 'Hello world'}
    
    class Update(Resource):
        def post(self):
            return {'message': 'update'}
    class Delete(Resource):
        def post(self):
            return {'message': 'delete'}
    class Select(Resource):
        def post(self):
            return {'message': 'get alumno'}
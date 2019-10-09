import os
from flask_restful import Resource, reqparse
from models import AvisoModel
import werkzeug
import uuid
parser = reqparse.RequestParser()

class InsertAviso(Resource):
    def post(self):
        parser.add_argument('usrId',help='usrId missing', required=True)
        parser.add_argument('titulo',help='titulo missing', required=True)
        parser.add_argument('descripcion',help='descripcion missing', required=True)
        parser.add_argument('fechaFin',help='fechaFin missing', required=True)
        parser.add_argument('fechaAlta',help='fechaAlta missing', required=True)
        parser.add_argument('prioridad',help='prioridad missing', required=True)
        parser.add_argument('img',type=werkzeug.datastructures.FileStorage, location='files')
        data = parser.parse_args()
        file = data['img']
        f_name = ''
        if(file):
            f_name = str(uuid.uuid4())+'.jpg'
            file.save('images/'+f_name)
        aviso_model = AvisoModel(
            usrId=data['usrId'],
            titulo=data['titulo'],
            descripcion=data['descripcion'],
            fechaFin=data['fechaFin'],
            fechaAlta=data['fechaAlta'],
            estado=1,
            imagen=f_name
        )
        try:
            aviso_model.save_to_db()
            return {
                'message': 'Aviso {}  was created'.format(data['titulo'])
                }
        except:
            return {'message' : 'Something went wrong'}, 500
            
        

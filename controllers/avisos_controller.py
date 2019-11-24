import os
from flask_restful import Resource, reqparse
from models import AvisoModel
import werkzeug
import uuid
import requests
from twilio.rest import Client

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
            # TWILIO MESSAGING
            if (data['prioridad'] == "1"):
                account_sid = 'ACba644bc2e547cc465bd41308af429c10'
                auth_token = '12e3a371e7472fc4523ccd85fc4f01eb'
                client = Client(account_sid, auth_token)
                message = client.messages \
                        .create(
                            body="INFORMATEC: "+data['descripcion'],
                            from_='+16788661949',
                            to='+524612180322')
            url = "https://fcm.googleapis.com/fcm/send"
            data_to_send = {"to":"/topics/all","notification":{"title": "Tienes un nuevo aviso","body":data['titulo']}}
            auth_head = {"Authorization": "key=AAAAQLWUJi0:APA91bFouaJIsigELqjh-CIzVVzKI3snTkXNvcMIgVC6_wJ9p56w3YK4Gxa-xG6xAzv7Bri3EerYjztbW9lo31ZW0z5kYvax6Iy_TmSR74NXiJW0oe7x3gkeAMSy1agg1s5K3iPZUjaZ","Content-Type" : "application/json"}
            x = requests.post(url, json = data_to_send, headers=auth_head)
            return {
                'message': 'Aviso {}  was created'.format(data['titulo'])
                }
        except:
            return {'message' : 'Something went wrong'}, 500
            
        
class AllAvisos(Resource):
    def get(self):
        return AvisoModel.return_all()
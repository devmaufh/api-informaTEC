from run import db
from passlib.hash import pbkdf2_sha256 as sha256



class TipoUserModel(db.Model):
    __tablename__ = 'tipousr'
    idTipoUsr  =  db.Column(db.Integer, primary_key = True)
    nomTipoUsr =  db.Column(db.String(60),nullable = False) 

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_type_by_id(cls, id):
        return cls.query.filter_by(idTipoUsr = id).first()

class UserModel(db.Model):
    __tablename__ = 'usuario'
    usrId    = db.Column(db.String(15), primary_key = True)
    nomUsr   = db.Column(db.String(126), nullable = False)
    pwd      = db.Column(db.String(255), nullable = False)    
    noTel    = db.Column(db.String(22), nullable = True)
    correo   = db.Column(db.String(126), nullable = False)
    rfcTutor = db.Column(db.String(30), nullable = True)
    fechaAlta= db.Column(db.Date, nullable  = False) 
    idTipoUsr= db.Column(db.Integer, db.ForeignKey('tipousr.idTipoUsr'))
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls,usrId):
        return cls.query.filter_by(usrId= usrId).first()
    
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    
    @staticmethod
    def verify_hash(password,hash):
        return sha256.verify(password,hash)



class AvisoModel(db.Model):
    __tablename__ = 'aviso'
    usrId   = db.Column(db.String(15), nullable = False)
    idAviso = db.Column(db.Integer, primary_key = True, nullable = False)
    titulo  = db.Column(db.String(60), nullable = False)
    descripcion = db.Column(db.String(256))
    fechaFin = db.Column(db.Date, nullable = False) 
    fechaAlta = db.Column(db.Date, nullable = False)
    estado = db.Column(db.Integer, nullable = False)
    imagen = db.Column(db.String(255), nullable = True)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def return_all(cls):
        def to_json(x):
            return {
                'idAviso': x.idAviso,
                'img': x.imagen,
                'usrId': x.usrId,
                'titulo':x.titulo,
                'descripcion':x.descripcion,
                'fechaFin':str(x.fechaFin),
                'fechaAlta':str(x.fechaAlta)
            }
        return {'avisos': list(map(lambda x: to_json(x), AvisoModel.query.all()))}

    


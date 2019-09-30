from run import db
from passlib.hash import pbkdf2_sha256 as sha256



class TipoUser(db.Model):
    __tablename__ = 'tipo_users'
    id       =  db.Column(db.Integer, primary_key = True)
    tipo     =  db.Column(db.String(50),nullable = False) 

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)    
    nombre   = db.Column(db.String(70), nullable = False)
    telefono = db.Column(db.String(10), nullable = False)
    id_tipo  = db.Column(db.Integer, db.ForeignKey('tipo_users.id'))


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    

    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username= username).first()
    
    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    
    @staticmethod
    def verify_hash(password,hash):
        return sha256.verify(password,hash)
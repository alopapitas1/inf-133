from database import db
from datetime import date
# `db.Model` es una clase base para todos los modelos de SQLAlchemy
# Define la clase `User` que hereda de `db.Model`
# `User` representa la tabla `users` en la base de datos
class User(db.Model):
    __tablename__ = 'users'
    # Define las columnas de la tabla `users`
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    
    e_mail = db.Column(db.String(50), nullable=False)
    contraseña = db.Column(db.String(50), nullable=False)
    fecha_nacimiento=db.Column(db.Date(), nullable=False)

    # Inicializa la clase `User`
    def __init__(self, first_name, last_name, e_mail, contraseña, fecha_nacimiento):
        self.first_name = first_name
        self.last_name = last_name
        
        self.e_mail=e_mail
        self.contraseña=contraseña
        anio,mes,dia = map(int,fecha_nacimiento.split("-"))
        self.fecha_nacimiento=date(anio,mes,dia)
        

    # Guarda un usuario en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los usuarios de la base de datos como se consluta es un query, todos los querys tiene que estar aqui
    @staticmethod
    def get_all():
        return User.query.all()

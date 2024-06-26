from database import db


# Define la clase `Animal` que hereda de `db.Model`
# `Animal` representa la tabla `animals` en la base de datos
class Animal(db.Model):
    __tablename__ = "animals"

    # Define las columnas de la tabla `animals`
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(50), nullable=False)
    peso = db.Column(db.Float(), nullable=False)
    sabor = db.Column(db.String(50), nullable=False)
    origen = db.Column(db.String(50), nullable=False)

    def __init__(self, marca, peso, sabor, origen):
        self.marca = marca
        self.peso = peso
        self.sabor = sabor
        self.origen=origen

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Animal.query.all()

    @staticmethod
    def get_by_id(id):
        return Animal.query.get(id)

    def update(self, marca=None, peso=None, sabor=None, origen=None):
        if marca is not None:
            self.marca = marca
        if peso is not None:
            self.peso = peso
        if sabor is not None:
            self.sabor = sabor
        if origen is not None:
            self.origen = origen
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

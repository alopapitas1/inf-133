from database import db

class Store(db.Model):
    ___tablename__="store"
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    descrption = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.String(30), nullable=False)
    
    def __init__(self, id, name, description, price, stock):
        self.id=id
        self.name=name
        self.descrption=description
        self.price=price
        self.stock=stock
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @staticmethod
    def get_all():
        return Store.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Store.query.get(id)
        
    def update(self, name=None, description=None, price=None, stock=None):
        if name is not None:
            self.name=name
        if description is not None:
            self.descrption=description
        if price is not None:
            self.price=price
        if stock is not None:
            self.stock=stock
        db.session.commit()
        
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
from app import db
import os
from sqlalchemy_serializer import SerializerMixin

class CustomSerializer():
    '''
    Class that serialize and unserialize
    - to_dict => serializes
    - from_dict => unserializes
    '''
    def to_dict(self):
        data = {}
        for field in self.fields:
            data[field] = self.__getattribute__(field)

        return data


    def from_dict(self, data):
        for field in self.fields:
            if field in data:
                setattr(self, field, data[field])

    @staticmethod
    def to_simple_collection_dict(query):
        r = []
        for i in query:
            r.append(i.to_dict())

        return r

class Numeros(db.Model, SerializerMixin, CustomSerializer):
    __tablename__ = 'numeros'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=True)
    acumulado = db.Column(db.Integer, nullable=True)

    fields = [
            'id',
            'numero',
            'acumulado'
        ]

    def __repr__(self):
        return f'<numeros {self.id}.>'


class Textos(db.Model, SerializerMixin, CustomSerializer):
    __tablename__ = 'textos'
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(10000))
    inicial = db.Column(db.String(1))
    final = db.Column(db.String(1))

    fields = [
            'id',
            'texto',
            'inicial',
            'final'
        ]

    def __repr__(self):
        return f'<textos {self.id}.>'


class Caracteres(db.Model, SerializerMixin, CustomSerializer):
    __tablename__ = 'caracteres'
    id = db.Column(db.Integer, primary_key=True)
    caracter = db.Column(db.String(1))
		
    fields = [
            'id',
            'caracter',
        ]

    def __repr__(self):
        return f'<caracteres {self.id}.>'
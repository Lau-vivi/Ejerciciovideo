from db import db

class Estudiante(db.Model):
    #Nombre de tabla

    __tablename__="estudiante"

    #Conjunto de atributos que van a ser los campos de la tabla 
    #Llave primaria
    id=db.Colum(db.Integer,primary_key=True)

    nombre=db.Colum(db.Sttring(50))
    email=db.Colum(db.Sttring(70))
    codigo=db.Colum(db.Sttring(15))

    #Metodo constructor para mapear datos a los campos definidos 
    def __init__(self, nombre, email, codigo):

        self.nombre=nombre
        self.email=email
        self.codigo=codigo
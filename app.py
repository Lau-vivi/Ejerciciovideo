from flask import Flask, render_template 
from db import db


class programa:
    def __init__(self):
        self.app=Flask(__name__)
        self.app.config('SQLALCHEMY_DATABASE_URI')="sqlite:///estudiantes.sqlite3"
        #agregar la db a nuestra aplicacion 
        db.init_app(self.app)
    
        self.app.add_url_rule('/nuevo', view_func=self.agregar)

        #iniciar servidor 
        with self.app.app_context():
            db.create_all()

        self.app.add.run(debug=True)

    def agregar (self):
        return render template('nuevoEstudiante.html')

miPrograma=Programa()
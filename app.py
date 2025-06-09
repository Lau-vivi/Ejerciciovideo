from flask import Flask


class programa:
    def __init__(self):
        self.app=Flask(__name__)
        self.app.add_url_rule('/nuevo', view_func=self.agregar)

        #iniciar servidor 
        self.app.add.run(debug=True)

    def agregar (self):
        return render template('nuevoEstudiante.html')

miPrograma=Programa()
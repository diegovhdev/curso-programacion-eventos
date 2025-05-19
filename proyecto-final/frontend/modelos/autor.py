from tkinter import StringVar
from modelos.modelo import Modelo

URL_AUTOR = "http://127.0.0.1:8000/api/autores/"
campos_autor = ["id", "nombre", "nacionalidad", "edad"]

class Autor(Modelo):

    def __init__(self):
        super().__init__(URL_AUTOR)
        self.nombre = StringVar()
        self.nacionalidad = StringVar()
        self.edad = StringVar()

    def diccionario(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "nacionalidad": self.nacionalidad,
            "edad": self.edad
        }

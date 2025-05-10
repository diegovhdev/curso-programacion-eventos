from tkinter import StringVar
from modelos.modelo import Modelo

class Autor(Modelo):

    def __init__(self):
        super().__init__("http://127.0.0.1:8000/api/autores")
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
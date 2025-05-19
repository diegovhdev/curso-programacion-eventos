from tkinter import StringVar
from modelos.modelo import Modelo

URL_LIBRO = "http://127.0.0.1:8000/api/libros/"
campos_libro = ["id", "fecha_de_publicacion", "titulo", "genero", "paginas"]

class Libro(Modelo):

    def __init__(self):
        super().__init__(URL_LIBRO)
        self.fecha_de_publicacion = StringVar()
        self.titulo = StringVar()
        self.genero = StringVar()
        self.paginas = StringVar()

    def diccionario(self):
        return {
            "id": self.id,
            "fecha_de_publicacion": self.fecha_de_publicacion,
            "titulo": self.titulo,
            "genero": self.genero,
            "paginas": self.paginas
        }



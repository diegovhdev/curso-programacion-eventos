from tkinter import StringVar

class Videojuego:

    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.id = StringVar()
        self.titulo = StringVar()
        self.graficos = StringVar()
        self.motor = StringVar()
        self.precio = StringVar()
        self.fecha_de_creacion = StringVar()

    def dictionary(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "graficos": self.graficos,
            "motor": self.motor,
            "precio": self.precio,
            "fecha_de_creacion": self.fecha_de_creacion
        }


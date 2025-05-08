from tkinter import Tk, Label, Entry, Button
from modelos.videojuego import Videojuego

class Interfaz:

    def __init__(self):
        self.row_index = 0
        self.ventana_principal = Tk()
        self.videojuego = Videojuego(self.ventana_principal)
        self.data = []


    def armar_interfaz(self):
        pasar_a_label = lambda texto: texto.capitalize().replace("_", " ") + ":"
        for key, value in self.videojuego.dictionary().items():
            Label(self.ventana_principal, text=pasar_a_label(key)).grid(row=self.row_index, column=0, padx=5, pady=5)
            Entry(self.ventana_principal, textvariable=value).grid(row=self.row_index, column=1, padx=5, pady=5)
            self.row_index += 1
        self.armar_botones()
        self.ventana_principal.mainloop()

    def armar_botones(self):
        botones = ["Guardar", "Consultar 1", "Consultar todos"]
        column_index = 0
        for boton in botones:
            (Button(self.ventana_principal, text=boton)
             .grid(row=self.row_index, column=column_index, padx=5, pady=5, sticky="nsew"))
            column_index += 1





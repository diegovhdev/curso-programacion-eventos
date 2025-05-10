from tkinter import Tk, Button
from modelos.autor import Autor
from modelos.libro import Libro
from vistas.interfaz_formulario import InterfazFormulario

class VentanaPrincipal(Tk):
    def __init__(self):
        super().__init__()
        self.formulario_autores = InterfazFormulario(self, Autor())
        self.formulario_libros = InterfazFormulario(self, Libro())

        self.boton_autores = Button(self, text="Autores", command=self.cambiar_a_autores)
        self.boton_autores.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.boton_libros = Button(self, text="Cambiar a libros", command=self.cambiar_a_libros)
        self.boton_libros.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.formulario_autores.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.formulario_libros.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.cambiar_a_autores()


    def cambiar_a_autores(self):
        self.title("Autores")
        self.boton_autores.config(text="Autores", bg="#E2DFD0")
        self.boton_libros.config(text="Cambiar a libros", bg="#d9d9d9")
        self.formulario_libros.grid_remove()
        self.formulario_autores.grid()

    def cambiar_a_libros(self):
        self.title("Libros")
        self.boton_libros.config(text="Libros", bg="#E2DFD0")
        self.boton_autores.config(text="Cambiar a autores", bg="#d9d9d9")
        self.formulario_autores.grid_remove()
        self.formulario_libros.grid()
from tkinter import Tk, Label, Entry, Button

from modelos.videojuego import Videojuego
from controladores.comunicacion import Comunicacion
from vistas.tabla import Tabla

class Interfaz:

    def __init__(self):
        self.row_index = 0
        self.ventana_principal = Tk()
        self.videojuego = Videojuego(self.ventana_principal)
        self.comunicacion = Comunicacion(self.ventana_principal)
        self.data = []
        formato = lambda texto: texto.capitalize().replace("_", " ")
        self.tabla = Tabla(self.ventana_principal, self.videojuego.obtener_campos(), self.data,  formato)


    def accion_guardar(self):
        self.comunicacion.guardar(self.videojuego.obtener_json())

    def accion_consultar_1(self):
        json = self.comunicacion.consultar(self.videojuego.id.get())
        self.tabla.refrescar([list(json.values())])

    def accion_consultar_todos(self):
        json = self.comunicacion.consultar_todos()
        self.tabla.refrescar([list(elemento.values()) for elemento in json])

    def obtener_comandos(self):
        return [
            [self.accion_guardar, "Guardar", "e"],
            [self.accion_consultar_1, "Consultar 1", ""],
            [self.accion_consultar_todos, "Consultar todos", "w"]
        ]


    def armar_interfaz(self):
        self.ventana_principal.title("Videojuegos Consulta")
        pasar_a_label = lambda texto: texto.capitalize().replace("_", " ") + ":"
        for key, value in self.videojuego.dictionary().items():
            Label(self.ventana_principal, text=pasar_a_label(key)).grid(
                row=self.row_index, column=0, padx=5, pady=5, sticky="e")
            Entry(self.ventana_principal, textvariable=value).grid(
                row=self.row_index, column=1, padx=5, pady=5, sticky="w")
            if key == "id":
                Button(self.ventana_principal, text="Buscar").grid(
                    row=self.row_index, column=2, padx=5, pady=5, sticky="w")
            self.row_index += 1
        self.armar_botones()
        self.tabla.tabla.grid(row=self.row_index, column=0, columnspan=len(self.videojuego.obtener_campos()))
        self.ventana_principal.mainloop()

    def armar_botones(self):
        configuracion_de_botones = self.obtener_comandos()
        column_index = 0
        for configuracion in configuracion_de_botones:
            Button(self.ventana_principal, text=configuracion[1], command=configuracion[0]).grid(
                row=self.row_index, column=column_index, padx=5, pady=5, sticky=configuracion[2])
            column_index += 1
        self.row_index += 1





from tkinter import Tk, Label, Entry, Button, Frame
from modelos.modelo import Modelo
from vistas.tabla import Tabla
from controladores.comunicacion import Comunicacion
from controladores.validacion import validaciones

class InterfazFormulario(Frame):

    def __init__(self, ventana_principal, modelo: Modelo):
        super().__init__(ventana_principal)
        self.row_index = 0
        self.modelo = modelo
        self.comunicacion = Comunicacion(modelo.api_url)
        self.data = []
        formato = lambda texto: texto.capitalize().replace("_", " ")
        self.tabla = Tabla(self, self.modelo.obtener_campos(), self.data, formato)
        self.labels_mensajes_de_error = []
        self.armar_interfaz()


    def accion_guardar(self):
        for i, entrada in enumerate(list(self.modelo.diccionario().values())[1:]):
            if self.labels_mensajes_de_error[i]["text"] != "" or entrada.get() == "":
                if entrada.get() == "":
                    self.labels_mensajes_de_error[i + 1].config(text="el campo no puede estar vacio", fg="red")
                return
        self.comunicacion.guardar(self.modelo.obtener_json())
        self.modelo.limpiar_campos()

    def accion_consultar_1(self):
        json = self.comunicacion.consultar(self.modelo.id.get())
        if "detail" in json and json["detail"]:
            self.labels_mensajes_de_error[0].config(text="El id no concuerda con ninguno existente", fg="red")
            return
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
        pasar_a_label = lambda texto: texto.capitalize().replace("_", " ") + ":"
        for key, value in self.modelo.diccionario().items():
            Label(self, text=pasar_a_label(key)).grid(
                row=self.row_index, column=0, padx=5, pady=5, sticky="e")
            entrada = Entry(self, textvariable=value)
            label = Label(self, text="")
            entrada.bind("<KeyRelease>", validaciones[key](value, label))
            entrada.grid(row=self.row_index, column=1, padx=5, pady=(5, 0), sticky="w")
            label.grid(row=self.row_index + 1, column=1, columnspan=2, padx=5, pady=(0, 5), sticky="w")
            self.labels_mensajes_de_error.append(label)
            self.row_index += 2
        self.armar_botones()
        self.tabla.tabla.grid(row=self.row_index, column=0, columnspan=3)

    def armar_botones(self):
        configuracion_de_botones = self.obtener_comandos()
        column_index = 0
        for configuracion in configuracion_de_botones:
            Button(self, text=configuracion[1], command=configuracion[0]).grid(
                row=self.row_index, column=column_index, padx=5, pady=5, sticky=configuracion[2])
            column_index += 1
        self.row_index += 1
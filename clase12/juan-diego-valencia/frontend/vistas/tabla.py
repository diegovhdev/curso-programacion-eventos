from tkinter import ttk

class Tabla:

    def __init__(self, ventana_principal, columnas, data, formato):
        self.tabla = ttk.Treeview(ventana_principal, columns=columnas, show='headings')
        for columna in columnas:
            self.tabla.heading(columna, text=formato(columna))
            self.tabla.column(columna, anchor="center")
        self.refrescar(data)

    def refrescar(self, data):
        self.tabla.delete(*self.tabla.get_children())
        print(data)
        for elemento in data:
            self.tabla.insert(parent='', index=0, values=elemento)
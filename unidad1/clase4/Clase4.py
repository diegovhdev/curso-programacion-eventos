#Julian Chavarria
import tkinter as tk
from tkinter import messagebox

class Jugador:
    def __init__(self, nombre, posicion, edad):
        self.nombre = nombre
        self.posicion = posicion
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} - {self.posicion} - {self.edad} años"

class EquipoFutbol:
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, nombre, posicion, edad):
        if nombre and posicion and edad:
            jugador = Jugador(nombre, posicion, edad)
            self.jugadores.append(jugador)
            return f"Jugador {nombre} agregado."
        else:
            return "Error: Todos los campos deben ser llenados."

class Interfaz:
    def __init__(self, root):
        self.equipo = EquipoFutbol()
        self.root = root
        self.root.title("Gestión de Equipo de Fútbol")

        # Variables StringVar
        self.nombre_var = tk.StringVar()
        self.posicion_var = tk.StringVar()
        self.edad_var = tk.StringVar()

        # Etiquetas y Entradas
        tk.Label(root, text="Nombre:").grid(row=0, column=0)
        tk.Entry(root, textvariable=self.nombre_var).grid(row=0, column=1)
        
        tk.Label(root, text="Posición:").grid(row=1, column=0)
        tk.Entry(root, textvariable=self.posicion_var).grid(row=1, column=1)
        
        tk.Label(root, text="Edad:").grid(row=2, column=0)
        tk.Entry(root, textvariable=self.edad_var).grid(row=2, column=1)
        
        tk.Button(root, text="Agregar Jugador", command=self.agregar_jugador).grid(row=3, column=0, columnspan=2)
        
        # Lista para mostrar jugadores
        self.lista_jugadores = tk.Listbox(root, width=40)
        self.lista_jugadores.grid(row=4, column=0, columnspan=2)
    
    def agregar_jugador(self):
        nombre = self.nombre_var.get()
        posicion = self.posicion_var.get()
        edad = self.edad_var.get()
        
        mensaje = self.equipo.agregar_jugador(nombre, posicion, edad)
        if "Error" in mensaje:
            messagebox.showerror("Error", mensaje)
        else:
            messagebox.showinfo("Éxito", mensaje)
            self.lista_jugadores.insert(tk.END, f"{nombre} - {posicion} - {edad} años")

if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()

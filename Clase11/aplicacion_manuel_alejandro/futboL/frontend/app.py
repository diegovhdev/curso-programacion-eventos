import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "http://127.0.0.1:8000/api/jugadores/"  # Asegúrate de que tu backend esté corriendo

class EquipoFutbol:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestión de Equipo de Fútbol 11")

        # Entradas
        tk.Label(master, text="ID (para buscar/actualizar/eliminar):").grid(row=0, column=0)
        self.entry_id = tk.Entry(master)
        self.entry_id.grid(row=0, column=1)

        tk.Label(master, text="Nombre:").grid(row=1, column=0)
        self.entry_nombre = tk.Entry(master)
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(master, text="Posición:").grid(row=2, column=0)
        self.entry_posicion = tk.Entry(master)
        self.entry_posicion.grid(row=2, column=1)

        tk.Label(master, text="Número:").grid(row=3, column=0)
        self.entry_numero = tk.Entry(master)
        self.entry_numero.grid(row=3, column=1)

        tk.Label(master, text="Edad:").grid(row=4, column=0)
        self.entry_edad = tk.Entry(master)
        self.entry_edad.grid(row=4, column=1)

        # Botones
        tk.Button(master, text="Guardar", command=self.guardar_jugador).grid(row=5, column=0)
        tk.Button(master, text="Buscar", command=self.buscar_jugador).grid(row=5, column=1)
        tk.Button(master, text="Actualizar", command=self.actualizar_jugador).grid(row=6, column=0)
        tk.Button(master, text="Eliminar", command=self.eliminar_jugador).grid(row=6, column=1)

        self.lista_jugadores = tk.Listbox(master, width=50)
        self.lista_jugadores.grid(row=7, columnspan=2)

    def guardar_jugador(self):
        datos = self.obtener_datos()
        if not datos:
            return
        response = requests.post(API_URL, json=datos)
        if response.status_code == 201:
            messagebox.showinfo("Éxito", "Jugador guardado correctamente.")
            self.limpiar_campos()
            self.mostrar_jugadores()
        else:
            messagebox.showerror("Error", "No se pudo guardar el jugador.")

    def buscar_jugador(self):
        id_jugador = self.entry_id.get()
        if not id_jugador.isdigit():
            messagebox.showwarning("Advertencia", "Debes ingresar un ID válido.")
            return
        response = requests.get(API_URL + id_jugador + "/")
        if response.status_code == 200:
            jugador = response.json()
            self.entry_nombre.delete(0, tk.END)
            self.entry_posicion.delete(0, tk.END)
            self.entry_numero.delete(0, tk.END)
            self.entry_edad.delete(0, tk.END)

            self.entry_nombre.insert(0, jugador["nombre"])
            self.entry_posicion.insert(0, jugador["posicion"])
            self.entry_numero.insert(0, jugador["numero"])
            self.entry_edad.insert(0, jugador["edad"])
        else:
            messagebox.showerror("Error", "Jugador no encontrado.")

    def actualizar_jugador(self):
        id_jugador = self.entry_id.get()
        if not id_jugador.isdigit():
            messagebox.showwarning("Advertencia", "Debes ingresar un ID válido.")
            return
        datos = self.obtener_datos()
        if not datos:
            return
        response = requests.put(API_URL + id_jugador + "/", json=datos)
        if response.status_code == 200:
            messagebox.showinfo("Éxito", "Jugador actualizado correctamente.")
            self.limpiar_campos()
            self.mostrar_jugadores()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el jugador.")

    def eliminar_jugador(self):
        id_jugador = self.entry_id.get()
        if not id_jugador.isdigit():
            messagebox.showwarning("Advertencia", "Debes ingresar un ID válido.")
            return
        response = requests.delete(API_URL + id_jugador + "/")
        if response.status_code == 204:
            messagebox.showinfo("Éxito", "Jugador eliminado correctamente.")
            self.limpiar_campos()
            self.mostrar_jugadores()
        else:
            messagebox.showerror("Error", "No se pudo eliminar el jugador.")

    def obtener_datos(self):
        nombre = self.entry_nombre.get()
        posicion = self.entry_posicion.get()
        numero = self.entry_numero.get()
        edad = self.entry_edad.get()

        if not (nombre and posicion and numero.isdigit() and edad.isdigit()):
            messagebox.showwarning("Advertencia", "Todos los campos deben estar completos y válidos.")
            return None

        return {
            "nombre": nombre,
            "posicion": posicion,
            "numero": int(numero),
            "edad": int(edad),
        }

    def limpiar_campos(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_posicion.delete(0, tk.END)
        self.entry_numero.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)

    def mostrar_jugadores(self):
        self.lista_jugadores.delete(0, tk.END)
        response = requests.get(API_URL)
        if response.status_code == 200:
            for jugador in response.json():
                self.lista_jugadores.insert(tk.END, f"ID {jugador['id']} - {jugador['nombre']} - {jugador['posicion']} - #{jugador['numero']} - {jugador['edad']} años")
        else:
            self.lista_jugadores.insert(tk.END, "No se pudieron cargar los jugadores.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EquipoFutbol(root)
    app.mostrar_jugadores()
    root.mainloop()

import tkinter as tk
from tkinter import messagebox
import requests

# Dirección base del backend (puedes reemplazarla por la real)
BASE_URL = "http://localhost:8000/api/videojuegos"

class VideojuegoForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulario de Videojuego")
        self.geometry("600x400")
        self.resizable(False, False)
        self.entries = {}

        self.crear_campos()
        self.crear_botones()

    def crear_campos(self):
        labels = ["ID", "Titulo", "Graficos", "Motor", "Precio", "Fecha_de_creacion"]

        for i, label in enumerate(labels):
            tk.Label(self, text=label + ":").grid(row=i, column=0, padx=10, pady=8, sticky="e")
            entry = tk.Entry(self, width=25)
            entry.grid(row=i, column=1, padx=10, pady=8, sticky="w")
            self.entries[label.lower()] = entry

            if label == "ID":
                buscar_btn = tk.Button(self, text="Buscar", command=self.buscar_videojuego)
                buscar_btn.grid(row=i, column=2, padx=5, pady=8)

    def crear_botones(self):
        frame = tk.Frame(self)
        frame.grid(row=7, column=0, columnspan=3, pady=30)

        guardar_btn = tk.Button(frame, text="Guardar", width=12, command=self.guardar_videojuego)
        actualizar_btn = tk.Button(frame, text="Actualizar", width=12, command=self.actualizar_videojuego)
        eliminar_btn = tk.Button(frame, text="Eliminar", width=12, command=self.eliminar_videojuego)

        guardar_btn.grid(row=0, column=0, padx=10)
        actualizar_btn.grid(row=0, column=1, padx=10)
        eliminar_btn.grid(row=0, column=2, padx=10)

    def get_datos_formulario(self):
        return {key: entry.get() for key, entry in self.entries.items()}

    def guardar_videojuego(self):
        data = self.get_datos_formulario()
        print(data)
        response = requests.post(f"{BASE_URL}/", json=data)
        if response.status_code == 201:
            messagebox.showinfo("Éxito", "Videojuego guardado correctamente.")
        else:
            messagebox.showerror("Error", f"No se pudo guardar. Código: {response.status_code}")


    def actualizar_videojuego(self):
        data = self.get_datos_formulario()
        vid = data.get("id")
        if not vid:
            messagebox.showwarning("Falta ID", "Por favor, ingresa un ID para actualizar.")
            return
        response = requests.put(f"{BASE_URL}/{vid}/", json=data)
        print(response)
        if response.status_code == 200:
            messagebox.showinfo("Éxito", "Videojuego actualizado correctamente.")
        else:
            messagebox.showerror("Error", f"No se pudo actualizar. Código: {response.status_code}")

    def eliminar_videojuego(self):
        vid = self.entries["id"].get()
        if not vid:
            messagebox.showwarning("Falta ID", "Por favor, ingresa un ID para eliminar.")
            return
        response = requests.delete(f"{BASE_URL}/{vid}/")
        if response.status_code == 204:
            messagebox.showinfo("Éxito", "Videojuego eliminado correctamente.")
            self.limpiar_formulario()
        else:
            messagebox.showerror("Error", f"No se pudo eliminar. Código: {response.status_code}")

    def buscar_videojuego(self):
        vid = self.entries["id"].get()
        if not vid:
            messagebox.showwarning("Falta ID", "Por favor, ingresa un ID para buscar.")
            return
        response = requests.get(f"{BASE_URL}/{vid}")
        if response.status_code == 200:
            datos = response.json()
            print(datos)
            for key, entry in self.entries.items():
                entry.delete(0, tk.END)
                entry.insert(0, datos.get(key, ""))
        else:
            messagebox.showerror("No encontrado", f"Videojuego no encontrado. Código: {response.status_code}")

    def limpiar_formulario(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    app = VideojuegoForm()
    app.mainloop()
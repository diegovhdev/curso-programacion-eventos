import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "http://localhost:8000/api/videojuegos/"  # Cambia si tu backend usa otro puerto o ruta

def agregar():
    data = {
        "titulo": campo_titulo.get(),
        "graficos": campo_graficos.get(),
        "motor": campo_motor.get(),
        "precio": campo_precio.get()
    }
    response = requests.post(API_URL, json=data)
    if response.status_code == 201:
        messagebox.showinfo("Éxito", "Videojuego agregado correctamente")
    else:
        messagebox.showerror("Error", "No se pudo agregar el videojuego")

def buscar():
    vid = campo_id.get()
    response = requests.get(API_URL + vid + "/")
    if response.status_code == 200:
        data = response.json()
        campo_titulo.delete(0, tk.END)
        campo_graficos.delete(0, tk.END)
        campo_motor.delete(0, tk.END)
        campo_precio.delete(0, tk.END)
        campo_titulo.insert(0, data["titulo"])
        campo_graficos.insert(0, data["graficos"])
        campo_motor.insert(0, data["motor"])
        campo_precio.insert(0, data["precio"])
    else:
        messagebox.showerror("Error", "Videojuego no encontrado")

def actualizar():
    vid = campo_id.get()
    data = {
        "titulo": campo_titulo.get(),
        "graficos": campo_graficos.get(),
        "motor": campo_motor.get(),
        "precio": campo_precio.get()
    }
    response = requests.put(API_URL + vid + "/", json=data)
    if response.status_code == 200:
        messagebox.showinfo("Éxito", "Videojuego actualizado")
    else:
        messagebox.showerror("Error", "No se pudo actualizar el videojuego")

def eliminar():
    vid = campo_id.get()
    response = requests.delete(API_URL + vid + "/")
    if response.status_code == 204:
        messagebox.showinfo("Éxito", "Videojuego eliminado")
        campo_titulo.delete(0, tk.END)
        campo_graficos.delete(0, tk.END)
        campo_motor.delete(0, tk.END)
        campo_precio.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "No se pudo eliminar el videojuego")

ventana = tk.Tk()
ventana.title("Gestión de Videojuegos")

# Campos de entrada
tk.Label(ventana, text="ID:").grid(row=0, column=0, sticky="e")
campo_id = tk.Entry(ventana)
campo_id.grid(row=0, column=1)

tk.Label(ventana, text="Título:").grid(row=1, column=0, sticky="e")
campo_titulo = tk.Entry(ventana)
campo_titulo.grid(row=1, column=1)

tk.Label(ventana, text="Gráficos:").grid(row=2, column=0, sticky="e")
campo_graficos = tk.Entry(ventana)
campo_graficos.grid(row=2, column=1)

tk.Label(ventana, text="Motor:").grid(row=3, column=0, sticky="e")
campo_motor = tk.Entry(ventana)
campo_motor.grid(row=3, column=1)

tk.Label(ventana, text="Precio:").grid(row=4, column=0, sticky="e")
campo_precio = tk.Entry(ventana)
campo_precio.grid(row=4, column=1)

# Botones
tk.Button(ventana, text="Agregar", width=15, command=agregar).grid(row=5, column=0, pady=5)
tk.Button(ventana, text="Buscar", width=15, command=buscar).grid(row=5, column=1, pady=5)
tk.Button(ventana, text="Actualizar", width=15, command=actualizar).grid(row=6, column=0, pady=5)
tk.Button(ventana, text="Eliminar", width=15, command=eliminar).grid(row=6, column=1, pady=5)

ventana.mainloop()

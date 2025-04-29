import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading
import time

# URL base de tu API
API_URL = "http://127.0.0.1:8000/api/"

# Funciones para Autores
def agregar_autor():
    nombre = entry_nombre.get()
    nacionalidad = entry_nacionalidad.get()
    edad = entry_edad.get()

    if nombre and nacionalidad and edad:
        try:
            edad = int(edad)
            data = {'nombre': nombre, 'nacionalidad': nacionalidad, 'edad': edad}
            response = requests.post(API_URL + 'autores/', json=data)
            print(response.status_code, response.json())
            if response.status_code == 201:
                messagebox.showinfo("Éxito", "Autor agregado correctamente.")
                entry_nombre.delete(0, tk.END)
                entry_nacionalidad.delete(0, tk.END)
                entry_edad.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Error al registrar autor.")
        except ValueError:
            messagebox.showerror("Error", "Edad debe ser un número.")
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")

def ver_autores():
    response = requests.get(API_URL + 'autores/')
    if response.status_code == 200:
        autores = response.json()
        lista = "\n".join([f"{a['nombre']} - {a['nacionalidad']} - {a['edad']} años" for a in autores])
        if lista:
            messagebox.showinfo("Autores Registrados", lista)
        else:
            messagebox.showinfo("Autores Registrados", "No hay autores registrados.")
    else:
        messagebox.showerror("Error", "Error al obtener autores.")

# Funciones para Libros
def agregar_libro():
    titulo = entry_titulo.get()
    genero = entry_genero.get()
    paginas = entry_paginas.get()
    fecha_de_publicacion = entry_fecha_de_pueblicacion.get()

    if titulo and genero and paginas and fecha_de_publicacion:
        try:
            paginas = int(paginas)
            fecha_de_publicacion = fecha_de_publicacion
            data = {'titulo': titulo, 'genero': genero, 'paginas': paginas, 'fecha_de_publicacion': fecha_de_publicacion}
            response = requests.post(API_URL + 'libros/', json=data)
            print(response.status_code, response.json())
            if response.status_code == 201:
                messagebox.showinfo("Éxito", "Libro agregado correctamente.")
                entry_titulo.delete(0, tk.END)
                entry_genero.delete(0, tk.END)
                entry_paginas.delete(0, tk.END)
                entry_fecha_de_pueblicacion.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Error al registrar libro.")
        except ValueError:
            messagebox.showerror("Error", "Páginas y Año deben ser números.")
    else:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")

def ver_libros():
    response = requests.get(API_URL + 'libros/')
    if response.status_code == 200:
        libros = response.json()
        lista = "\n".join([f"{l['titulo']} - {l['genero']} - {l['paginas']} páginas - {l['fecha_de_publicacion']}" for l in libros])
        if lista:
            messagebox.showinfo("Libros Registrados", lista)
        else:
            messagebox.showinfo("Libros Registrados", "No hay libros registrados.")
    else:
        messagebox.showerror("Error", "Error al obtener libros.")

# Función para copia de seguridad automática
def respaldo_automatico():
    while True:
        try:
            autores = requests.get(API_URL + 'autores/').json()
            libros = requests.get(API_URL + 'libros/').json()

            with open('respaldo_autores.txt', 'w', encoding='utf-8') as f_autores:
                for autor in autores:
                    f_autores.write(f"Nombre: {autor['nombre']}\n")
                    f_autores.write(f"Nacionalidad: {autor['nacionalidad']}\n")
                    f_autores.write(f"Edad: {autor['edad']}\n\n")

            with open('respaldo_libros.txt', 'w', encoding='utf-8') as f_libros:
                for libro in libros:
                    f_libros.write(f"Título: {libro['titulo']}\n")
                    f_libros.write(f"Género: {libro['genero']}\n")
                    f_libros.write(f"Páginas: {libro['paginas']}\n")
                    f_libros.write(f"Año: {libro['anio_publicacion']}\n\n")
        except Exception as e:
            print("Error en respaldo:", e)

        time.sleep(60)  # Espera 1 minuto

# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Autores y Libros")
root.geometry("800x400")

# Sección Autores
frame_autores = ttk.LabelFrame(root, text="Autores")
frame_autores.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

ttk.Label(frame_autores, text="Nombre:").grid(row=0, column=0, sticky="w")
entry_nombre = ttk.Entry(frame_autores)
entry_nombre.grid(row=0, column=1)

ttk.Label(frame_autores, text="Nacionalidad:").grid(row=1, column=0, sticky="w")
entry_nacionalidad = ttk.Entry(frame_autores)
entry_nacionalidad.grid(row=1, column=1)

ttk.Label(frame_autores, text="Edad:").grid(row=2, column=0, sticky="w")
entry_edad = ttk.Entry(frame_autores)
entry_edad.grid(row=2, column=1)

btn_agregar_autor = ttk.Button(frame_autores, text="Agregar Autor", command=agregar_autor)
btn_agregar_autor.grid(row=3, column=0, pady=10)

btn_ver_autores = ttk.Button(frame_autores, text="Ver Autores", command=ver_autores)
btn_ver_autores.grid(row=3, column=1, pady=10)

# Sección Libros
frame_libros = ttk.LabelFrame(root, text="Libros")
frame_libros.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

ttk.Label(frame_libros, text="Título:").grid(row=0, column=0, sticky="w")
entry_titulo = ttk.Entry(frame_libros)
entry_titulo.grid(row=0, column=1)

ttk.Label(frame_libros, text="Género:").grid(row=1, column=0, sticky="w")
entry_genero = ttk.Entry(frame_libros)
entry_genero.grid(row=1, column=1)

ttk.Label(frame_libros, text="Páginas:").grid(row=2, column=0, sticky="w")
entry_paginas = ttk.Entry(frame_libros)
entry_paginas.grid(row=2, column=1)

ttk.Label(frame_libros, text="Año de publicación:").grid(row=3, column=0, sticky="w")
entry_fecha_de_pueblicacion = ttk.Entry(frame_libros)
entry_fecha_de_pueblicacion.grid(row=3, column=1)

btn_agregar_libro = ttk.Button(frame_libros, text="Agregar Libro", command=agregar_libro)
btn_agregar_libro.grid(row=4, column=0, pady=10)

btn_ver_libros = ttk.Button(frame_libros, text="Ver Libros", command=ver_libros)
btn_ver_libros.grid(row=4, column=1, pady=10)

# Lanzar el hilo de respaldo automático
hilo_respaldo = threading.Thread(target=respaldo_automatico, daemon=True)
hilo_respaldo.start()

root.mainloop()

import threading
import time

import requests
from vistas.ventana_principal import VentanaPrincipal

BASE_URL = "http://127.0.0.1:8000/api/"

def respaldo_automatico():
    while True:
        try:
            autores = requests.get(BASE_URL + 'autores/').json()
            libros = requests.get(BASE_URL + 'libros/').json()

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
                    f_libros.write(f"Fecha de publicacion: {libro['fecha_de_publicacion']}\n\n")
        except Exception as e:
            print("Error en respaldo:", e)

        time.sleep(30)


hilo_respaldo = threading.Thread(target=respaldo_automatico, daemon=True)
hilo_respaldo.start()

ventana_principal = VentanaPrincipal()
ventana_principal.mainloop()
import threading
import time
import requests
from vistas.ventana_principal import VentanaPrincipal
from modelos.libro import URL_LIBRO, campos_libro
from modelos.autor import URL_AUTOR, campos_autor



def respaldo_automatico_libros(tiempo):
    while True:
        try:
            libros = requests.get(URL_LIBRO).json()
            with open('respaldo_libros.txt','w', encoding='utf-8') as f_libros:
                for libro in libros:
                    for campo in campos_libro:
                        f_libros.write(f"{campo.capitalize().replace("_", " ")}: {libro[campo]}\n")
                    f_libros.write("\n")

        except Exception as e:
            print("Error en respaldo:", e)

        time.sleep(tiempo)


def respaldo_automatico_autores(tiempo):
    while True:
        try:
            autores = requests.get(URL_AUTOR).json()
            with open('respaldo_autores.txt', 'w', encoding='utf-8') as f_autores:
                for autor in autores:
                    for campo in campos_autor:
                        f_autores.write(f"{campo.capitalize().replace("_", " ")}: {autor[campo]}\n")
                    f_autores.write("\n")

        except Exception as e:
            print("Error en respaldo:", e)

        time.sleep(tiempo)



hilo_respaldo_libros = threading.Thread(target=respaldo_automatico_libros, args=(60,),  daemon=True)
hilo_respaldo_libros.start()

hilo_respaldo_autores = threading.Thread(target=respaldo_automatico_autores, args=(60, ),  daemon=True)
hilo_respaldo_autores.start()

ventana_principal = VentanaPrincipal()
ventana_principal.mainloop()
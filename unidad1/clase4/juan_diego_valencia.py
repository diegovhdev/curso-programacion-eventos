import tkinter as tk
import re

ventana_principal = tk.Tk()
ventana_principal.title("Videojuego")

frame = tk.Frame(ventana_principal, width=600, height=600)

titulo = tk.StringVar()
etiqueta_titulo = tk.Label(frame, text="Titulo videojuego: ")
campo_titulo = tk.Entry(frame, textvariable=titulo)
label_validacion_titulo = tk.Label(frame, text="")

def crear_evento_validador_de_campo(variable, label_validacion, expresion_regular, mensaje_de_error):
    def evento_validador(event):
        if expresion_regular.match(variable.get()) is None:
            label_validacion.config(text=mensaje_de_error)
        else:
            label_validacion.config(text="")

    return evento_validador


campo_titulo.bind("<KeyRelease>", crear_evento_validador_de_campo(
    variable=titulo,
    label_validacion=label_validacion_titulo,
    expresion_regular=re.compile(r"^[A-Za-zñÑ ]*$"),
    mensaje_de_error="solo se permiten letras"
))


graficos = tk.StringVar()
etiqueta_graficos = tk.Label(frame, text="Graficos: ")
campo_graficos = tk.Entry(frame, textvariable=graficos)
label_validacion_graficos = tk.Label(frame, text="")


campo_graficos.bind("<KeyRelease>", crear_evento_validador_de_campo(
    variable=graficos,
    label_validacion=label_validacion_graficos,
    expresion_regular=re.compile(r"^([23][Dd]|)$"),
    mensaje_de_error="el formato debe ser 2d o 3d"
))


motor = tk.StringVar()
etiqueta_motor = tk.Label(frame, text="Motor: ")
campo_motor = tk.Entry(frame, textvariable=motor)
label_validacion_motor = tk.Label(frame, text="")


campo_motor.bind("<KeyRelease>", crear_evento_validador_de_campo(
    variable=motor,
    label_validacion=label_validacion_motor,
    expresion_regular=re.compile(r"^[a-zA-Z0-9 ]*$"),
    mensaje_de_error="no se permiten caracteres especiales"
))


precio = tk.StringVar()
etiqueta_precio = tk.Label(frame, text="Precio: ")
campo_precio = tk.Entry(frame, textvariable=precio)
label_validacion_precio = tk.Label(frame, text="")


campo_precio.bind("<KeyRelease>", crear_evento_validador_de_campo(
    variable=precio,
    label_validacion=label_validacion_precio,
    expresion_regular=re.compile(r"^\d*(\.\d{1,2})?$"),
    mensaje_de_error="solo se permiten numeros"
))


boton_agregar = tk.Button(frame, text="agregar")

etiqueta_titulo.grid(row=0, column=0, pady=5, padx=5)
campo_titulo.grid(row=0, column=1, pady=5, padx=5)
label_validacion_titulo.grid(row=1, columnspan=2)

etiqueta_graficos.grid(row=2, column=0, pady=5, padx=5)
campo_graficos.grid(row=2, column=1, pady=5, padx=5)
label_validacion_graficos.grid(row=3, columnspan=2)

etiqueta_motor.grid(row=4, column=0, pady=5, padx=5)
campo_motor.grid(row=4, column=1, pady=5, padx=5)
label_validacion_motor.grid(row=5, columnspan=2)

etiqueta_precio.grid(row=6, column=0, pady=5, padx=5)
campo_precio.grid(row=6, column=1, pady=5, padx=5)
label_validacion_precio.grid(row=7, columnspan=2)

boton_agregar.grid(row=8, columnspan=2, pady=5, padx=5)

frame.pack()

ventana_principal.mainloop()
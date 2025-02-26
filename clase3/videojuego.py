from tkinter import Frame, Tk, Entry, Label, Button

ventana_principal = Tk()
ventana_principal.title("Videojuego")

titulo = ""

frame = Frame(ventana_principal, width=600, height=400)

etiqueta_titulo = Label(frame, text="Titulo videojuego: ")
campo_titulo = Entry(frame)

etiqueta_graficos = Label(frame, text="Graficos: ")
campo_graficos = Entry(frame)

etiqueta_motor = Label(frame, text="Motor: ")
campo_motor = Entry(frame)

etiqueta_precio = Label(frame, text="Precio: ")
campo_precio = Entry(frame)

boton_agregar = Button(frame, text="agregar")

etiqueta_titulo.grid(row=0, column=0, pady=5, padx=5)
campo_titulo.grid(row=0, column=1, pady=5, padx=5)

etiqueta_graficos.grid(row=1, column=0, pady=5, padx=5)
campo_graficos.grid(row=1, column=1, pady=5, padx=5)

etiqueta_motor.grid(row=2, column=0, pady=5, padx=5)
campo_motor.grid(row=2, column=1, pady=5, padx=5)

etiqueta_precio.grid(row=3, column=0, pady=5, padx=5)
campo_precio.grid(row=3, column=1, pady=5, padx=5)

boton_agregar.grid(row=4, columnspan=2, pady=5, padx=5)

frame.pack()


ventana_principal.mainloop()
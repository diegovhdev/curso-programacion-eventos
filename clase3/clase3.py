from tkinter import Frame, Tk
from tkinter.messagebox import askyesno

ventana_principal = Tk()
ventana_principal.title("Mi titulo")

def accion_click(event):
    frame.focus_set()
    print("clicked at", event.x, event.y    )

def accion_tecla_presionada(event):
    frame.focus_set()
    print(f"Has presionado: {event.char}")

def usuario_quiere_salir():
    if askyesno("Salir de la aplicación", "¿Seguro que quieres salir de la aplicacion?"):
        ventana_principal.destroy()

frame = Frame(ventana_principal, width=500, height=500)
frame.bind("<Button-1>", accion_click)
frame.bind("<Key>", accion_tecla_presionada)
frame.pack()

ventana_principal.protocol("WM_DELETE_WINDOW", usuario_quiere_salir)

ventana_principal.mainloop()
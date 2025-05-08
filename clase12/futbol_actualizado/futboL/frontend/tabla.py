import tkinter as tk
from tkinter import ttk, messagebox
from controladores.comunicacion import obtener_todas_las_consolas

def mostrar_tabla():
    ventana = tk.Tk()
    ventana.title("Lista de Consolas")
    ventana.geometry("600x400")

    tree = ttk.Treeview(ventana)
    tree["columns"] = ("potencia", "almacenamiento", "conectividad", "diseno")
    tree.column("#0", width=50, minwidth=50)
    tree.column("potencia", width=120, anchor=tk.CENTER)
    tree.column("almacenamiento", width=120, anchor=tk.CENTER)
    tree.column("conectividad", width=120, anchor=tk.CENTER)
    tree.column("diseno", width=120, anchor=tk.CENTER)

    tree.heading("#0", text="ID", anchor=tk.CENTER)
    tree.heading("potencia", text="Potencia", anchor=tk.CENTER)
    tree.heading("almacenamiento", text="Almacenamiento", anchor=tk.CENTER)
    tree.heading("conectividad", text="Conectividad", anchor=tk.CENTER)
    tree.heading("diseno", text="Diseño", anchor=tk.CENTER)

    try:
        consolas = obtener_todas_las_consolas()
        for consola in consolas:
            tree.insert("", tk.END, text=consola["id"], values=(
                consola["potencia_de_procesamiento"],
                consola["capacidad_de_almacenamiento"],
                consola["conectividad"],
                consola["diseño_y_ergonomía"]
            ))
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron cargar las consolas: {e}")

    tree.pack(expand=True, fill=tk.BOTH)
    ventana.mainloop()
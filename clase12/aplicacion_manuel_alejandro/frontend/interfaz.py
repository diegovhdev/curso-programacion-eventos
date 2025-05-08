import tkinter as tk
from tkinter import messagebox
from controladores.comunicacion import crear_consola, obtener_consola, actualizar_consola, eliminar_consola

def interfaz():
    app = tk.Tk()
    app.title("Gestión de Consolas")
    app.geometry("400x400")

    # Entradas
    tk.Label(app, text="ID (para buscar/actualizar/eliminar)").pack()
    id_entry = tk.Entry(app)
    id_entry.pack()

    labels = ["Potencia", "Almacenamiento", "Conectividad", "Diseño"]
    entries = []

    for label in labels:
        tk.Label(app, text=label).pack()
        entry = tk.Entry(app)
        entry.pack()
        entries.append(entry)

    def get_data():
        return {
            "potencia_de_procesamiento": entries[0].get(),
            "capacidad_de_almacenamiento": entries[1].get(),
            "conectividad": entries[2].get(),
            "diseño_y_ergonomía": entries[3].get(),
        }

    def llenar_campos(data):
        entries[0].delete(0, tk.END)
        entries[0].insert(0, data["potencia_de_procesamiento"])
        entries[1].delete(0, tk.END)
        entries[1].insert(0, data["capacidad_de_almacenamiento"])
        entries[2].delete(0, tk.END)
        entries[2].insert(0, data["conectividad"])
        entries[3].delete(0, tk.END)
        entries[3].insert(0, data["diseño_y_ergonomía"])

    def guardar():
        data = get_data()
        res = crear_consola(data)
        messagebox.showinfo("Respuesta", f"Consola creada: {res}")

    def buscar():
        cid = id_entry.get()
        if not cid: return messagebox.showwarning("ID faltante", "Ingresa un ID para buscar")
        res = obtener_consola(cid)
        if "detail" in res:
            messagebox.showerror("Error", res["detail"])
        else:
            llenar_campos(res)

    def actualizar():
        cid = id_entry.get()
        if not cid: return messagebox.showwarning("ID faltante", "Ingresa un ID para actualizar")
        data = get_data()
        res = actualizar_consola(cid, data)
        messagebox.showinfo("Actualizado", f"Consola actualizada: {res}")

    def eliminar():
        cid = id_entry.get()
        if not cid: return messagebox.showwarning("ID faltante", "Ingresa un ID para eliminar")
        eliminar_consola(cid)
        messagebox.showinfo("Eliminado", "Consola eliminada")

    # Botones
    tk.Button(app, text="Guardar", command=guardar).pack(pady=5)
    tk.Button(app, text="Buscar", command=buscar).pack(pady=5)
    tk.Button(app, text="Actualizar", command=actualizar).pack(pady=5)
    tk.Button(app, text="Eliminar", command=eliminar).pack(pady=5)

    app.mainloop()

if __name__ == "__main__":
    interfaz()
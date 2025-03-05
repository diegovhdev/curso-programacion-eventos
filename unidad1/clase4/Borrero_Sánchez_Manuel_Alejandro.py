import tkinter as tk
import re
from tkinter import messagebox

def Validar_Letras(Value):
    Patron = re.compile("^[A-Za-zÁ-Úá-úñÑ ]*$")
    Resultado = Patron.match(Value.get()) is not None
    return Resultado

def Evento_Presionar_Tecla(event):
    global Texto_Validar_Nombre
    if Validar_Letras(Nombre):
        Texto_Validar_Nombre = ""
    else:
        Texto_Validar_Nombre = "Solo se permiten letras"
    LabelValidaciónNombre.config(text=Texto_Validar_Nombre)

def validar_numeros(text_widget):
    content = text_widget.get("1.0", tk.END).strip()
    return content.isdigit()

def validar_diseño(text_widget):
    content = text_widget.get("1.0", tk.END).strip().lower()
    keywords = ["cómodo", "ergonómico", "aestético", "diseño", "funcional", "práctico", "flexible", "versatil"]
    return any(keyword in content for keyword in keywords)

def validar_sin_texto(text_widget):
    content = text_widget.get("1.0", tk.END).strip()
    return len(content) == 0

def save_text(title, text_widget, validation_func):
    if validation_func(text_widget):
        content = text_widget.get("1.0", tk.END).strip()
        print(f"{title}: {content}")
        text_widget.delete("1.0", tk.END)
        messagebox.showinfo("Guardar Cambios", f"Contenido guardado para {title}.")
    else:
        messagebox.showwarning("Advertencia", f"Entrada no válida para {title}.")

def main():
    global Nombre, LabelValidaciónNombre, Texto_Validar_Nombre
    Texto_Validar_Nombre = ""

    root = tk.Tk()
    root.title("Consola de Videojuegos personalizada")

    frame_name = tk.Frame(root)
    frame_name.pack(pady=10, padx=10)

    LabelNombre = tk.Label(frame_name, text="Nombre")
    LabelNombre.pack(anchor='w')

    Nombre = tk.StringVar(frame_name)
    EntryNombre = tk.Entry(frame_name, textvariable=Nombre)
    EntryNombre.pack()
    EntryNombre.bind("<KeyRelease>", Evento_Presionar_Tecla)

    LabelValidaciónNombre = tk.Label(frame_name, text="")
    LabelValidaciónNombre.pack()

    attributes = {
        "Potencia de Procesamiento": ( "Describe la CAPACIDAD de la CPU-GPU de tu consola.", validar_numeros),
        "Capacidad de Almacenamiento": ( "Indica cuánto ESPACIO quieres en tu consola para juegos y datos.", validar_numeros),
        "Conectividad": ( "EXPLICA las opciones de conectividad. Como Wi-Fi, Bluetooth, etc.", lambda tw: True),
        "Diseño y Ergonomía": ( "COMENTA sobre el diseño físico y la comodidad de uso. Debe incluir palabras clave como 'cómodo', 'ergonómico', etc.", validar_diseño)
    }

    for title, (description, validation_func) in attributes.items():
        frame = tk.Frame(root)
        frame.pack(pady=10, padx=10)

        label = tk.Label(frame, text=title, font=("Sans serif", 14))
        label.pack(anchor='w')

        desc_label = tk.Label(frame, text=description)
        desc_label.pack(anchor='w')

        text_widget = tk.Text(frame, height=3, width=40)
        text_widget.pack(pady=5)

        save_button = tk.Button(frame, text="Guardar Cambios", 
                                command=lambda t=title, tw=text_widget, vf=validation_func: save_text(t, tw, vf))
        save_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()

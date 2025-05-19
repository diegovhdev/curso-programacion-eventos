import re

def crear_evento_validador_de_campo(variable, label_validacion, expresion_regex, mensaje_de_error, validar_vacio=True):
    def evento_validador(event):
        if variable.get().replace(" ", "") == "" and validar_vacio:
            label_validacion.config(text="el campo no puede estar vacio", fg="red")
        elif expresion_regex.match(variable.get()) is None and variable.get().replace(" ", "") != "":
            label_validacion.config(text=mensaje_de_error, fg="red")
        else:
            label_validacion.config(text="")

    return evento_validador

def solo_caracteres_de_alfabeto(variable, label_validacion):
    regex = re.compile(r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ\s]+$")
    mensaje_de_error = "Solo se permiten letras del alfabeto español"
    return crear_evento_validador_de_campo(variable, label_validacion, regex, mensaje_de_error)

def solo_caracteres_de_alfabeto_y_numeros(variable, label_de_validacion):
    regex = re.compile(r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ0-9 ]+$")
    mensaje_de_error = "Solo letras o numeros"
    return crear_evento_validador_de_campo(variable, label_de_validacion, regex, mensaje_de_error)

def solo_numeros_enteros_positivos(variable, label_validacion):
    regex = re.compile(r"^[1-9][0-9]*$")
    mensaje_de_error = "Solo numeros mayores a 0"
    return crear_evento_validador_de_campo(variable, label_validacion, regex, mensaje_de_error)

def solo_id_numerico(variable, label_validacion):
    regex = re.compile(r"^[1-9][0-9]*$")
    mensaje_de_error = "Solo numeros mayores a 0"
    return crear_evento_validador_de_campo(variable, label_validacion, regex, mensaje_de_error, validar_vacio=False)

def solo_fechas(variable, label_validacion):
    regex = re.compile(r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$")
    mensaje_de_error = "Solo se permiten fechas con el formato YYYY-MM-DD"
    return crear_evento_validador_de_campo(variable, label_validacion, regex, mensaje_de_error)

validaciones = {
    "id": solo_id_numerico,
    "nombre": solo_caracteres_de_alfabeto,
    "nacionalidad": solo_caracteres_de_alfabeto,
    "edad": solo_numeros_enteros_positivos,
    "fecha_de_publicacion": solo_fechas,
    "titulo": solo_caracteres_de_alfabeto_y_numeros,
    "genero": solo_caracteres_de_alfabeto,
    "paginas": solo_numeros_enteros_positivos,
}
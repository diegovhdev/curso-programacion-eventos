import requests

URL = "http://localhost:8000/api/consolas/"

def crear_consola(data):
    return requests.post(URL, json=data).json()

def obtener_consola(id):
    return requests.get(f"{URL}{id}/").json()

def actualizar_consola(id, data):
    return requests.put(f"{URL}{id}/", json=data).json()

def eliminar_consola(id):
    return requests.delete(f"{URL}{id}/")
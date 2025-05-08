import requests

class Comunicacion:

    def __init__(self, ventana_principal):
        self.url = "http://127.0.0.1:8000/api/videojuegos"
        self.ventana_principal = ventana_principal

    def guardar(self, json):
        try:
            resultado = requests.post(f"{self.url}/", json=json)
            print(resultado.json)
        except:
            pass

    def actualizar(self, json, _id):
        try:
            resultado = requests.post(f"{self.url}/{_id}/", json=json)
            print(resultado.json)
            return resultado
        except:
            pass

    def consultar(self, _id):
        resultado = requests.get(f"{self.url}/{_id}/")
        return resultado.json()

    def consultar_todos(self):
        resultado = requests.get(f"{self.url}/")
        return resultado.json()
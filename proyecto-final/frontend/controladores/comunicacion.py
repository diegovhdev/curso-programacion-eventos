import requests

class Comunicacion:

    def __init__(self, url):
        self.url = url

    def guardar(self, json):
        try:
            resultado = requests.post(f"{self.url}/", json=json)
            print(resultado.json)
        except:
            pass

    def consultar(self, _id):
        resultado = requests.get(f"{self.url}/{_id}/")
        return resultado.json()

    def consultar_todos(self):
        resultado = requests.get(f"{self.url}/")
        return resultado.json()
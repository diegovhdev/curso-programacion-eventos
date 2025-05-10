from abc import abstractmethod
from tkinter import StringVar

class Modelo:

    def __init__(self, api_url):
        self.api_url = api_url
        self.id = StringVar()

    @abstractmethod
    def diccionario(self) -> dict[str, StringVar]:
        pass

    def obtener_campos(self) -> list[str]:
        return list(self.diccionario().keys())

    def obtener_json(self):
        json = {}
        for key, value in self.diccionario().items():
            json[key] = value.get()
        del json["id"]
        return json

    def limpiar_campos(self):
        for _, value in self.diccionario().items():
            value.set("")




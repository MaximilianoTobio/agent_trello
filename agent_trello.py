import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TRELLO_API_KEY")
TOKEN = os.getenv("TRELLO_TOKEN")
BASE_URL = "https://api.trello.com/1"

def crear_tablero(nombre):
    url = f"{BASE_URL}/boards/"
    params = {
        'name': nombre,
        'key': API_KEY,
        'token': TOKEN
    }
    response = requests.post(url, params=params)
    return response.json()

def crear_lista(id_tablero, nombre_lista):
    url = f"{BASE_URL}/lists"
    params = {
        'name': nombre_lista,
        'idBoard': id_tablero,
        'key': API_KEY,
        'token': TOKEN
    }
    response = requests.post(url, params=params)
    return response.json()

def borrar_tablero(id_tablero):
    url = f"{BASE_URL}/boards/{id_tablero}"
    params = {
        'key': API_KEY,
        'token': TOKEN
    }
    response = requests.delete(url, params=params)
    return response.status_code == 200

if __name__ == "__main__":
    tablero = crear_tablero("Agente Trello - Sprint Test")
    print("Tablero creado:", tablero["url"])

    listas = ["Backlog", "Sprint", "Doing", "Done"]
    for nombre in listas:
        lista = crear_lista(tablero["id"], nombre)
        print(f"Lista '{nombre}' creada con ID:", lista["id"])

import os
import pytest
from agent_trello import crear_tablero, crear_lista

# Validamos que existan las variables de entorno
def test_env_variables():
    assert os.getenv("TRELLO_API_KEY") is not None
    assert os.getenv("TRELLO_TOKEN") is not None

# Creamos un tablero temporal para probar la API
def test_crear_tablero_y_listas():
    tablero = crear_tablero("Test desde Pytest")
    assert "id" in tablero
    assert "url" in tablero

    listas = ["Backlog", "Sprint", "Done"]
    for nombre in listas:
        lista = crear_lista(tablero["id"], nombre)
        assert lista["name"] == nombre
        assert lista["idBoard"] == tablero["id"]

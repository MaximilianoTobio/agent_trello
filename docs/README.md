# 🤖 Agente Trello IA – Sprint Automático

Este agente permite crear automáticamente tableros y listas en Trello usando la API oficial. Está diseñado para ser usado como módulo independiente en cualquier flujo de automatización o proyecto de gestión ágil.

## 🚀 ¿Qué hace?

- Crea un tablero nuevo en Trello
- Crea las listas básicas: `Backlog`, `Sprint`, `Doing`, `Done`

## 🛠 Requisitos

- Python 3.8+
- Cuenta de Trello
- Claves de API de Trello

## 🔧 Configuración

1. Crear un archivo `.env` con tus credenciales:
   ```
   TRELLO_API_KEY=...
   TRELLO_TOKEN=...
   ```

2. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```

3. Ejecutar el script:
   ```
   python agent_trello.py
   ```

## 🧠 Estructura futura

- Manejo de tarjetas
- Movimiento entre listas
- Agente IA que decide acciones en función del estado del tablero

## 📁 Estructura del Repo

```
public/
docs/
agent_trello.py
README.md
setup-agente-trello.md
```

# 🤖 Roadmap de Creación – Agente Trello IA (Blueprintfy)

**Objetivo:** Crear un agente en Python que se comunique con la API de Trello para automatizar tareas típicas de gestión Scrum, con validación humana en cada paso (pair programming IA+humano).

---

## 📅 Fases del Desarrollo

### 🔧 Fase 1 – Setup Básico

- [x] Crear repositorio del Power-Up
- [x] Desplegar front básico en Netlify
- [x] Obtener API Key y Token de Trello
- [ ] Crear entorno Python (venv)
- [ ] Instalar librerías: `requests`, `python-dotenv`, `trello`, etc.
- [ ] Cargar credenciales como variables de entorno

---

### 🧠 Fase 2 – Definición de Comandos del Agente

- Crear tablero Scrum
- Crear listas (Backlog, To Do, In Progress, Done)
- Crear tarjetas desde texto (user stories)
- Mover tarjetas según lógica Scrum
- Etiquetar por prioridad (Must, Should, Could)
- Generar resumen del estado del sprint

---

### ⚙️ Fase 3 – API Layer en Python

- Crear módulo `trello_agent.py`
- Encapsular funciones como:
  - `crear_tablero(nombre)`
  - `crear_lista(tablero_id, nombre)`
  - `crear_tarjeta(lista_id, titulo, descripcion)`
  - `mover_tarjeta(tarjeta_id, nueva_lista_id)`
- Agregar `try/except` + logs para trazabilidad

---

### 🧑‍⚖️ Fase 4 – Validación Humana

- Toda acción propuesta por IA debe ser validada por humano (input CLI o interfaz)
- Posibilidad de rechazar/modificar sugerencia

---

### 🔁 Fase 5 – Iteración y Expansión

- Conectar a flujo de pensamiento IA (ej: prompt + OpenAI + decision agent)
- Automatizar planificación y actualización de tablero por texto
- Exportar estado del sprint a Markdown o PDF

---

## 📚 Referencias útiles

- [API Trello Docs](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/)
- [Trello Power-Up Framework](https://developer.atlassian.com/cloud/trello/power-ups/)
- [Python Trello Wrapper](https://github.com/sarumont/py-trello)

---

🗓️ Última edición: 2025-05-18

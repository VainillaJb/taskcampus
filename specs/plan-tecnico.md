# Plan Técnico de Desarrollo - TaskCampus

## 1. Arquitectura del Sistema
El sistema seguirá una arquitectura cliente-servidor desacoplada:
* **Backend:** API REST construida en Python puro (utilizando el módulo nativo `http.server` o un microframework ligero)[cite: 47, 88].
* **Frontend:** Aplicación web SPA (Single Page Application) desarrollada con TypeScript, HTML5 y estilos con Tailwind CSS[cite: 43, 44, 45].
* **Persistencia:** Almacenamiento de datos local en un archivo en formato JSON (`tasks.json`).

## 2. Modelo de Datos (JSON)
Las tareas se almacenarán en la carpeta `backend/` dentro de un archivo `tasks.json` con la siguiente estructura de ejemplo:

```json
[
  {
    "id": "1",
    "titulo": "Proyecto de Redes",
    "descripcion": "Configurar los servidores DHCP y DNS en VMs",
    "asignatura": "Administración de Servidores",
    "fecha_entrega": "2026-05-30",
    "prioridad": "alta",
    "estado": "en proceso"
  }
]
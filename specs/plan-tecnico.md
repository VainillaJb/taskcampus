# Plan Técnico de Desarrollo - TaskCampus

## 1. Arquitectura del Sistema
El sistema seguirá una arquitectura cliente-servidor desacoplada:
* **Backend:** API REST construida en Python puro (utilizando el módulo nativo `http.server` o un microframework ligero)[cite: 47, 88].
* **Frontend:** Aplicación web SPA (Single Page Application) desarrollada con TypeScript, HTML5 y estilos con Tailwind CSS[cite: 43, 44, 45].
* **Persistencia:** Almacenamiento de datos local en PostgreSQL.

## 2. Modelo de Datos (PostgreSQL)
Modelo de Datos: Las tareas se almacenan en una tabla relacional llamada tasks en PostgreSQL con los campos: id (SERIAL), titulo (TEXT), descripcion (TEXT), asignatura (TEXT), fecha_entrega (DATE), prioridad (TEXT), estado (TEXT).

```json
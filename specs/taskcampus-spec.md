# Especificación del sistema TaskCampus

## Problema
[cite_start]Los estudiantes de noveno semestre necesitan organizar sus actividades académicas, fechas de entrega y estado de avance. [cite: 5, 71]

## Objetivo
[cite_start]Desarrollar una aplicación web básica (TaskCampus) para registrar, consultar, actualizar y eliminar tareas estudiantiles, aplicando control de versiones y una metodología basada en especificaciones. [cite: 3, 6, 10, 73]

## Usuarios
[cite_start]Estudiantes universitarios. [cite: 75]

## Historias de usuario
* [cite_start]Como estudiante, quiero registrar tareas para organizar mis actividades. [cite: 77]
* [cite_start]Como estudiante, quiero filtrar tareas por estado para identificar mis pendientes. [cite: 77]
* [cite_start]Como estudiante, quiero marcar tareas como finalizadas para controlar mi avance. [cite: 78]

## Requisitos funcionales

### [cite_start]Módulo de tareas [cite: 17]
El sistema debe permitir las siguientes acciones:
1. **RF01. [cite_start]Registrar tareas:** Crear una tarea con los siguientes campos obligatorios: [cite: 18, 19, 80]
   * Título [cite: 20]
   * [cite_start]Descripción [cite: 21]
   * [cite_start]Asignatura [cite: 22]
   * Fecha de entrega [cite: 23]
   * [cite_start]Prioridad (Baja, Media, Alta) [cite: 24]
   * [cite_start]Estado (Pendiente, En proceso, Finalizada) [cite: 25]
2. **RF02. [cite_start]Listar tareas:** Mostrar la lista de todas las tareas académicas registradas. [cite: 26, 81]
3. **RF03. [cite_start]Editar tareas:** Modificar los datos de una tarea ya existente. [cite: 32, 82]
4. **RF04. [cite_start]Eliminar tareas:** Borrar una tarea del sistema. [cite: 33, 83]
5. **RF05. [cite_start]Filtrar tareas:** Permitir la búsqueda o filtrado de tareas por su estado, prioridad o asignatura. [cite: 27, 29, 30, 31, 84]
6. **RF06. [cite_start]Mostrar resumen estadístico:** Presentar un panel con el total de tareas, tareas pendientes, finalizadas y de alta prioridad. [cite: 34, 35, 36, 38, 40, 85]

## Requisitos no funcionales
* [cite_start]**RNF01:** La interfaz de usuario debe ser clara y sencilla utilizando HTML y Tailwind. [cite: 44, 87]
* [cite_start]**RNF02:** El backend debe estar desarrollado en Python y exponer una API REST. [cite: 47, 88]
* [cite_start]**RNF03:** Los datos deben guardarse con una persistencia simple en un archivo JSON. [cite: 48]
* [cite_start]**RNF04:** El código debe estar completamente versionado en GitHub con uso obligatorio de ramas, commits y pull requests. [cite: 51, 53, 89]
* [cite_start]**RNF05:** El proyecto debe incluir documentación detallada de instalación en un archivo README. [cite: 90]

## Endpoints de la API REST (Backend sugerido)

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| GET | `/tasks` | [cite_start]Listar todas las tareas [cite: 92] |
| GET | `/tasks/{id}` | [cite_start]Consultar el detalle de una tarea específica [cite: 92] |
| POST | `/tasks` | [cite_start]Crear una nueva tarea [cite: 92] |
| PUT | `/tasks/{id}` | [cite_start]Actualizar una tarea existente [cite: 92] |
| DELETE | `/tasks/{id}` | [cite_start]Eliminar una tarea del archivo JSON [cite: 92] |
| GET | `/tasks/summary` | [cite_start]Mostrar el resumen estadístico de las tareas [cite: 92] |
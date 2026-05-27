# Especificación del sistema TaskCampus

## Problema
Los estudiantes de noveno semestre necesitan organizar sus actividades académicas, fechas de entrega y estado de avance.

## Objetivo
Desarrollar una aplicación web básica (TaskCampus) para registrar, consultar, actualizar y eliminar tareas estudiantiles, aplicando control de versiones y una metodología basada en especificaciones.

## Usuarios
Estudiantes universitarios.

## Historias de usuario
* Como estudiante, quiero registrar tareas para organizar mis actividades.
* Como estudiante, quiero filtrar tareas por estado para identificar mis pendientes.
* Como estudiante, quiero marcar tareas como finalizadas para controlar mi avance.

## Requisitos funcionales

### Módulo de tareas
El sistema debe permitir las siguientes acciones:
1. **RF01. Registrar tareas:** Crear una tarea con los siguientes campos obligatorios:
   * Título
   * Descripción
   * Asignatura
   * Fecha de entrega
   * Prioridad (Baja, Media, Alta)
   * Estado (Pendiente, En proceso, Finalizada)
2. **RF02. Listar tareas:** Mostrar la lista de todas las tareas académicas registradas.
3. **RF03. Editar tareas:** Modificar los datos de una tarea ya existente.
4. **RF04. Eliminar tareas:** Borrar una tarea del sistema.
5. **RF05. Filtrar tareas:** Permitir la búsqueda o filtrado de tareas por su estado, prioridad o asignatura.
6. **RF06. Mostrar resumen estadístico:** Presentar un panel con el total de tareas, tareas pendientes, finalizadas y de alta prioridad.

## Requisitos no funcionales
* **RNF01:** La interfaz de usuario debe ser clara y sencilla utilizando HTML y Tailwind.
* **RNF02:** El backend debe estar desarrollado en Python y exponer una API REST.
* **RNF03:** Los datos deben guardarse con persistencia en una base de datos local PostgreSQL.
* **RNF04:** El código debe estar completamente versionado en GitHub con uso obligatorio de ramas, commits y pull requests.
* **RNF05:** El proyecto debe incluir documentación detallada de instalación en un archivo README.

## Endpoints de la API REST (Backend sugerido)

| Método | Ruta | Descripción |
| :--- | :--- | :--- |
| GET | /tasks | Listar todas las tareas |
| GET | /tasks/{id} | Consultar el detalle de una tarea específica |
| POST | /tasks | Crear una nueva tarea |
| PUT | /tasks/{id} | Actualizar una tarea existente |
| DELETE | /tasks/{id} | Eliminar una tarea de la base de datos |
| GET | /tasks/summary | Mostrar el resumen estadístico de las tareas |
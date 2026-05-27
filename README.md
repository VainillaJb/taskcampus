# TaskCampus 🎓

TaskCampus es una aplicación web sencilla y desacoplada diseñada para que los estudiantes de noveno semestre puedan registrar, consultar, actualizar, eliminar y filtrar sus tareas académicas, permitiendo además visualizar un resumen estadístico de sus actividades pendientes.

Este proyecto fue desarrollado aplicando la metodología **Spec Driven Development (SDD)** y control de versiones estructurado.

## Estructura del Repositorio
* `specs/`: Contiene la especificación funcional y el plan técnico del sistema.
* `backend/`: Código fuente en Python de la API REST con persistencia en PostgreSQL.
* `frontend/`: Interfaz de usuario interactiva construida con HTML5, Tailwind CSS y JavaScript/TypeScript.
  * `frontend/app.ts` es el código fuente en TypeScript.
  * `frontend/app.js` es la versión compilada que se carga en el navegador.

## Requisitos Previos
* Python 3.14 o superior instalado localmente.
* PostgreSQL local instalado y en ejecución.
* Un navegador web moderno (Chrome, Edge, Firefox, etc.).

## Instrucciones de Instalación y Uso

### 1. Ejecución del Backend (Python)
1. Abra una terminal en la raíz del proyecto.
2. Navegue a la carpeta del servidor:
   ```bash
   cd backend
   ```
3. Instale dependencias Python si no lo ha hecho:
   ```bash
   pip install -r requirements.txt
   ```
4. Configuración de la Base de Datos

- Asegúrese de tener PostgreSQL instalado y corriendo.

- En pgAdmin, cree una base de datos llamada taskcampus.

- En la herramienta de consulta (Query Tool) de pgAdmin, ejecute el contenido del archivo backend/db_init.sql.

- Cree un archivo llamado .env dentro de la carpeta backend/ con sus credenciales:

   DB_NAME=taskcampus
   DB_USER=tu_usuario
   DB_PASSWORD=tu_contraseña
     ```
5. Inicie el servidor:
   ```bash
   python app.py
   ```
6. Deje la terminal abierta mientras use la aplicación.

### 2. Abrir el Frontend
1. Abra el archivo `frontend/index.html` en su navegador.
2. Si usa VS Code, puede hacer clic derecho en `frontend/index.html` y seleccionar "Open with Live Server" o abrirlo directamente en el navegador.
3. Asegúrese de que el backend esté corriendo en `http://localhost:5000`.

#### Compilar TypeScript (opcional pero recomendado)
Si quieres mantener `frontend/app.ts` y compilarlo a `frontend/app.js`, sigue estos pasos:

1. Asegúrate de tener Node.js y npm instalados.
2. Desde la raíz del proyecto ejecuta:

```bash
cd frontend
npm install
npm run build
```

Esto instalará TypeScript localmente y generará `frontend/app.js` a partir de `frontend/app.ts`.

### 3. Uso de la Aplicación
* Registrar una nueva tarea rellenando el formulario.
* Editar una tarea usando el botón "Editar".
* Eliminar una tarea usando el botón "Eliminar".
* Filtrar la lista por estado, prioridad o asignatura.
* El panel superior muestra el total de tareas, pendientes, finalizadas y prioridad alta.

### 4. Notas
* El backend usa PostgreSQL para almacenar las tareas.
* No cierre la terminal del backend mientras esté usando la app.

### 5. Autor
* Creadora: Nardy Jamileth Japón Bohórquez - 8vo A.

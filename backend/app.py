import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

# Nombre del archivo donde se guardarán las tareas académicas
DB_FILE = os.path.join(os.path.dirname(__file__), 'tasks.json')

def read_tasks():
    """Lee las tareas desde el archivo JSON."""
    if not os.path.exists(DB_FILE):
        return []
    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def write_tasks(tasks):
    """Guarda las tareas en el archivo JSON."""
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

class TaskCampusAPI(BaseHTTPRequestHandler):
    """Controlador de la API REST para gestionar las tareas."""

    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        # Habilitar CORS para que el frontend (TypeScript) se pueda conectar sin bloqueos de seguridad
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        """Maneja las peticiones de control de acceso (CORS)."""
        self._set_headers(200)

    def do_GET(self):
        """Maneja las peticiones GET (Listar tareas y Resumen)."""
        tasks = read_tasks()

        # Endpoint: /tasks/summary (Mostrar resumen estadístico)
        if self.path == '/tasks/summary':
            total = len(tasks)
            pendientes = sum(1 for t in tasks if t.get('estado') == 'pendiente')
            finalizadas = sum(1 for t in tasks if t.get('estado') == 'finalizada')
            alta_prioridad = sum(1 for t in tasks if t.get('prioridad') == 'alta')
            
            summary = {
                "total": total,
                "pendientes": pendientes,
                "finalizadas": finalizadas,
                "alta_prioridad": alta_prioridad
            }
            self._set_headers(200)
            self.wfile.write(json.dumps(summary).encode('utf-8'))
            return

        # Endpoint: /tasks (Listar todas las tareas)
        if self.path == '/tasks' or self.path.startswith('/tasks?'):
            self._set_headers(200)
            self.wfile.write(json.dumps(tasks).encode('utf-8'))
            return

        # Endpoint: /tasks/{id} (Consultar una tarea específica)
        if self.path.startswith('/tasks/'):
            task_id = self.path.split('/')[-1]
            task = next((t for t in tasks if t.get('id') == task_id), None)
            if task:
                self._set_headers(200)
                self.wfile.write(json.dumps(task).encode('utf-8'))
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Tarea no encontrada"}).encode('utf-8'))
            return

        self._set_headers(404)

    def do_POST(self):
        """Maneja las peticiones POST (Registrar una tarea)."""
        if self.path == '/tasks':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            new_task = json.loads(post_data.decode('utf-8'))

            tasks = read_tasks()
            # Generar un ID simple sumando 1 al ID más alto existente
            new_id = str(max([int(t['id']) for t in tasks]) + 1) if tasks else "1"
            
            # Estructura obligatoria de la tarea según la especificación
            task_data = {
                "id": new_id,
                "titulo": new_task.get('titulo'),
                "descripcion": new_task.get('descripcion'),
                "asignatura": new_task.get('asignatura'),
                "fecha_entrega": new_task.get('fecha_entrega'),
                "prioridad": new_task.get('prioridad', 'baja'),
                "estado": new_task.get('estado', 'pendiente')
            }

            tasks.append(task_data)
            write_tasks(tasks)

            self._set_headers(201)
            self.wfile.write(json.dumps(task_data).encode('utf-8'))
            return
        
        self._set_headers(404)

    def do_PUT(self):
        """Maneja las peticiones PUT (Editar una tarea existente)."""
        if self.path.startswith('/tasks/'):
            task_id = self.path.split('/')[-1]
            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length)
            updated_fields = json.loads(put_data.decode('utf-8'))

            tasks = read_tasks()
            task = next((t for t in tasks if t.get('id') == task_id), None)

            if task:
                task.update(updated_fields)
                write_tasks(tasks)
                self._set_headers(200)
                self.wfile.write(json.dumps(task).encode('utf-8'))
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Tarea no encontrada"}).encode('utf-8'))
            return
        
        self._set_headers(404)

    def do_DELETE(self):
        """Maneja las peticiones DELETE (Eliminar una tarea)."""
        if self.path.startswith('/tasks/'):
            task_id = self.path.split('/')[-1]
            tasks = read_tasks()
            
            # Filtrar la lista dejando fuera la tarea con el ID seleccionado
            new_tasks = [t for t in tasks if t.get('id') != task_id]
            
            if len(tasks) != len(new_tasks):
                write_tasks(new_tasks)
                self._set_headers(200)
                self.wfile.write(json.dumps({"success": True}).encode('utf-8'))
            else:
                self._set_headers(404)
                self.wfile.write(json.dumps({"error": "Tarea no encontrada"}).encode('utf-8'))
            return
        
        self._set_headers(404)

def run(server_class=HTTPServer, handler_class=TaskCampusAPI, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor Backend de TaskCampus corriendo en http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    run()
import json
import os
import psycopg2
import psycopg2.extras
import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

# Configuración usando variables de entorno
DB_NAME = os.getenv('DB_NAME', 'taskcampus')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
        host=DB_HOST, port=DB_PORT
    )

def normalize_task(task):
    if not task: return None
    task_dict = dict(task)
    for key, value in task_dict.items():
        if isinstance(value, (datetime.date, datetime.datetime)):
            task_dict[key] = value.isoformat()
        elif key == 'id':
            task_dict[key] = str(value)
    return task_dict

# --- CRUD Functions ---

def read_tasks():
    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute('SELECT * FROM tasks ORDER BY id;')
                return [normalize_task(row) for row in cur.fetchall()]
    except Exception as e:
        print(f'Error en read_tasks: {e}')
        return []

def insert_task(task_data):
    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute(
                    '''INSERT INTO tasks (titulo, descripcion, asignatura, fecha_entrega, prioridad, estado)
                       VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;''',
                    (task_data.get('titulo'), task_data.get('descripcion'), task_data.get('asignatura'), 
                     task_data.get('fecha_entrega'), task_data.get('prioridad', 'baja'), task_data.get('estado', 'pendiente'))
                )
                inserted_id = cur.fetchone()['id']
                conn.commit()
                task_data['id'] = str(inserted_id)
                return task_data
    except Exception as e:
        print(f'Error en insert_task: {e}')
        return None

def update_task(task_id, updated_fields):
    allowed_fields = {'titulo', 'descripcion', 'asignatura', 'fecha_entrega', 'prioridad', 'estado'}
    updates = {k: v for k, v in updated_fields.items() if k in allowed_fields}
    if not updates: return None

    try:
        with get_connection() as conn:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                set_clauses = [f"{key} = %s" for key in updates.keys()]
                query = f"UPDATE tasks SET {', '.join(set_clauses)} WHERE id = %s RETURNING *;"
                cur.execute(query, tuple(updates.values()) + (task_id,))
                task = cur.fetchone()
                conn.commit()
                return normalize_task(task)
    except Exception as e:
        print(f'Error en update_task: {e}')
        return None

def delete_task(task_id):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute('DELETE FROM tasks WHERE id = %s;', (task_id,))
                conn.commit()
                return cur.rowcount > 0
    except Exception as e:
        print(f'Error en delete_task: {e}')
        return False

# --- API Controller ---

class TaskCampusAPI(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        if self.path == '/tasks/summary':
            tasks = read_tasks()
            summary = {
                "total": len(tasks),
                "pendientes": sum(1 for t in tasks if t.get('estado') == 'pendiente'),
                "finalizadas": sum(1 for t in tasks if t.get('estado') == 'finalizada'),
                "alta_prioridad": sum(1 for t in tasks if t.get('prioridad') == 'alta')
            }
            self._send_json(summary)
        elif self.path == '/tasks':
            self._send_json(read_tasks())
        elif self.path.startswith('/tasks/'):
            task_id = self.path.split('/')[-1]
            # Usar read_task aquí (puedes agregarla siguiendo el patrón)
            self._send_json({"message": "Detalle por ID pendiente de implementación"})
        else:
            self._send_json({"error": "No encontrado"}, 404)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))
        result = insert_task(data)
        self._send_json(result or {"error": "Error al crear"}, 201 if result else 500)

if __name__ == '__main__':
    server = HTTPServer(('localhost', 5000), TaskCampusAPI)
    print("Servidor corriendo en http://localhost:5000")
    server.serve_forever()
"use strict";
// URL base de nuestro servidor backend en Python
const API_URL = 'http://localhost:5000/tasks';
// Elementos de la interfaz de usuario (DOM) con tipado estricto de TypeScript
const taskForm = document.getElementById('task-form');
const tasksContainer = document.getElementById('tasks-container');
const formTitle = document.getElementById('form-title');
const btnSubmit = document.getElementById('btn-submit');
const btnCancel = document.getElementById('btn-cancel');
// Campos del formulario
const taskIdInput = document.getElementById('task-id');
const tituloInput = document.getElementById('titulo');
const asignaturaInput = document.getElementById('asignatura');
const descripcionInput = document.getElementById('descripcion');
const fechaInput = document.getElementById('fecha_entrega');
const prioridadInput = document.getElementById('prioridad');
const estadoInput = document.getElementById('estado');
// Selectores de Filtros
const filterEstado = document.getElementById('filter-estado');
const filterPrioridad = document.getElementById('filter-prioridad');
const filterAsignatura = document.getElementById('filter-asignatura');
// Variable global tipada para almacenar las tareas temporalmente
let allTasks = [];
// --- FUNCIONES API (Consumo del Backend) ---
async function fetchTasks() {
    try {
        const response = await fetch(API_URL);
        allTasks = await response.json();
        renderTasks();
        fetchSummary();
    }
    catch (error) {
        if (tasksContainer) {
            tasksContainer.innerHTML = `<p class="text-center text-red-500 py-4 bg-white rounded-xl border">Error al conectar con el servidor Backend. Asegúrate de que app.py esté corriendo.</p>`;
        }
    }
}
async function fetchSummary() {
    try {
        const response = await fetch(`${API_URL}/summary`);
        const summary = await response.json();
        const totalEl = document.getElementById('stat-total');
        const pendEl = document.getElementById('stat-pendientes');
        const finEl = document.getElementById('stat-finalizadas');
        const altaEl = document.getElementById('stat-alta');
        if (totalEl)
            totalEl.innerText = summary.total;
        if (pendEl)
            pendEl.innerText = summary.pendientes;
        if (finEl)
            finEl.innerText = summary.finalizadas;
        if (altaEl)
            altaEl.innerText = summary.alta_prioridad;
    }
    catch (e) {
        console.error("Error al cargar resumen", e);
    }
}
if (taskForm) {
    taskForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        if (!tituloInput || !asignaturaInput || !descripcionInput || !fechaInput || !prioridadInput || !estadoInput || !taskIdInput)
            return;
        const taskData = {
            titulo: tituloInput.value,
            asignatura: asignaturaInput.value,
            descripcion: descripcionInput.value,
            fecha_entrega: fechaInput.value,
            prioridad: prioridadInput.value,
            estado: estadoInput.value
        };
        const id = taskIdInput.value;
        const url = id ? `${API_URL}/${id}` : API_URL;
        const method = id ? 'PUT' : 'POST';
        try {
            const response = await fetch(url, {
                method: method,
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(taskData)
            });
            if (response.ok) {
                resetForm();
                fetchTasks();
            }
        }
        catch (error) {
            alert('No se pudo guardar la tarea.');
        }
    });
}
async function deleteTask(id) {
    if (confirm('¿Estás seguro de eliminar esta tarea académica?')) {
        try {
            const response = await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
            if (response.ok)
                fetchTasks();
        }
        catch (error) {
            alert('Error al eliminar');
        }
    }
}
// --- LOGICA DE RENDERIZADO VISUAL ACTUALIZADA A TONOS CLAROS ---
function renderTasks() {
    if (!tasksContainer || !filterEstado || !filterPrioridad || !filterAsignatura)
        return;
    tasksContainer.innerHTML = '';
    const queryAsignatura = filterAsignatura.value.trim().toLowerCase();
    const filtered = allTasks.filter(task => {
        const matchEstado = filterEstado.value === 'todos' || task.estado === filterEstado.value;
        const matchPrioridad = filterPrioridad.value === 'todos' || task.prioridad === filterPrioridad.value;
        const matchAsignatura = queryAsignatura === '' || task.asignatura.toLowerCase().includes(queryAsignatura);
        return matchEstado && matchPrioridad && matchAsignatura;
    });
    if (filtered.length === 0) {
        tasksContainer.innerHTML = `<p class="text-center text-slate-400 py-8 bg-slate-50/50 rounded-xl border border-dashed border-slate-200 text-sm">No se encontraron tareas con los filtros seleccionados.</p>`;
        return;
    }
    filtered.forEach(task => {
        // Colores sutiles claros por prioridad
        const badgeColor = task.prioridad === 'alta'
            ? 'bg-rose-50 text-rose-700 border-rose-100'
            : task.prioridad === 'media'
                ? 'bg-amber-50 text-amber-700 border-amber-100'
                : 'bg-emerald-50 text-emerald-700 border-emerald-100';
        // Estilo especial si la tarea está terminada
        const opacityClass = task.estado === 'finalizada' ? 'opacity-50 border-slate-200 bg-slate-50/50' : 'border-sky-100/70 bg-white';
        const card = document.createElement('div');
        card.className = `p-4 rounded-xl border shadow-xs flex flex-col md:flex-row justify-between items-start md:items-center gap-4 transition hover:shadow-sm ${opacityClass}`;
        card.innerHTML = `
            <div class="space-y-1 flex-1">
                <div class="flex items-center gap-2 flex-wrap">
                    <h3 class="text-base font-bold text-slate-800">${task.titulo}</h3>
                    <span class="text-[10px] px-2 py-0.5 rounded-full font-bold uppercase tracking-wider border ${badgeColor}">${task.prioridad}</span>
                    <span class="text-[10px] bg-sky-50 text-sky-700 px-2 py-0.5 rounded-md border border-sky-100 font-medium">${task.asignatura}</span>
                </div>
                <p class="text-slate-600 text-sm leading-relaxed">${task.descripcion}</p>
                <p class="text-[11px] text-slate-400 flex items-center gap-1.5">
                    <span>📅 Entrega: <span class="font-semibold text-slate-500">${task.fecha_entrega}</span></span>
                    <span>•</span>
                    <span class="capitalize">Estado: <span class="font-semibold text-slate-500">${task.estado}</span></span>
                </p>
            </div>
            <div class="flex gap-2 w-full md:w-auto justify-end border-t border-slate-150 pt-2.5 md:border-t-0 md:pt-0">
                <button onclick="editTask('${task.id}')" class="text-xs bg-sky-50 text-sky-600 px-3 py-1.5 rounded-lg border border-sky-200/60 hover:bg-sky-100 font-semibold transition cursor-pointer">Editar</button>
                <button onclick="deleteTask('${task.id}')" class="text-xs bg-slate-50 text-slate-500 px-3 py-1.5 rounded-lg border border-slate-200 hover:bg-rose-50 hover:text-rose-600 hover:border-rose-200 transition cursor-pointer">Eliminar</button>
            </div>
        `;
        tasksContainer.appendChild(card);
    });
}
function editTask(id) {
    const task = allTasks.find(t => t.id === id);
    if (!task || !taskIdInput || !tituloInput || !asignaturaInput || !descripcionInput || !fechaInput || !prioridadInput || !estadoInput || !formTitle || !btnSubmit || !btnCancel)
        return;
    taskIdInput.value = task.id;
    tituloInput.value = task.titulo;
    asignaturaInput.value = task.asignatura;
    descripcionInput.value = task.descripcion;
    fechaInput.value = task.fecha_entrega;
    prioridadInput.value = task.prioridad;
    estadoInput.value = task.estado;
    formTitle.innerText = "✏️ Editar Tarea Académica";
    btnSubmit.innerText = "Actualizar Cambios";
    btnCancel.classList.remove('hidden');
}
function resetForm() {
    if (!taskForm || !taskIdInput || !formTitle || !btnSubmit || !btnCancel)
        return;
    taskForm.reset();
    taskIdInput.value = '';
    formTitle.innerText = "📝 Registrar Nueva Tarea";
    btnSubmit.innerText = "Guardar Tarea";
    btnCancel.classList.add('hidden');
}
window.editTask = editTask;
window.deleteTask = deleteTask;
if (filterEstado)
    filterEstado.addEventListener('change', renderTasks);
if (filterPrioridad)
    filterPrioridad.addEventListener('change', renderTasks);
if (filterAsignatura)
    filterAsignatura.addEventListener('input', renderTasks);
if (btnCancel)
    btnCancel.addEventListener('click', resetForm);
window.onload = fetchTasks;

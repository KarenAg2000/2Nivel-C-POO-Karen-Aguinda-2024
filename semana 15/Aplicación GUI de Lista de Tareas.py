import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Error de entrada", "Debe ingresar una tarea.")

def complete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.itemconfig(selected_task_index, {'fg': 'green'})  # Cambia el color de la tarea a verde
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(tk.END, f"{task} [Completada]")
    except IndexError:
        messagebox.showwarning("Error de selección", "Debe seleccionar una tarea.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Error de selección", "Debe seleccionar una tarea.")

def uncomplete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        if "[Completada]" in task:
            listbox_tasks.itemconfig(selected_task_index, {'fg': 'black'})  # Cambia el color de la tarea a negro
            task = task.replace(" [Completada]", "")
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, task)
        else:
            messagebox.showinfo("Aviso", "La tarea no está marcada como completada.")
    except IndexError:
        messagebox.showwarning("Error de selección", "Debe seleccionar una tarea.")

root = tk.Tk()
root.title("Lista de Tareas")

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)
entry_task.bind('<Return>', add_task)  # Añadir tarea al presionar Enter

btn_add_task = tk.Button(root, text="Añadir Tarea", width=20, command=add_task)
btn_add_task.pack(pady=5)

listbox_tasks = tk.Listbox(root, height=10, width=50, selectmode=tk.SINGLE)
listbox_tasks.pack(pady=10)

btn_complete_task = tk.Button(root, text="Marcar como Completada", width=20, command=complete_task)
btn_complete_task.pack(pady=5)

btn_uncomplete_task = tk.Button(root, text="Marcar como Incompleta", width=20, command=uncomplete_task)
btn_uncomplete_task.pack(pady=5)

btn_delete_task = tk.Button(root, text="Eliminar Tarea", width=20, command=delete_task)
btn_delete_task.pack(pady=5)

root.mainloop()

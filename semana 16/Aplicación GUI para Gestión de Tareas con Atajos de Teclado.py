import tkinter as tk
from tkinter import messagebox

class GestionTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("450x400")

        self.entrada_tarea = tk.Entry(self.root, font=("Arial", 14))
        self.entrada_tarea.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="we")
        self.entrada_tarea.bind("<Return>", lambda event: self.agregar_tarea())

        self.boton_agregar = tk.Button(self.root, text="Agregar Tarea", font=("Arial", 12), command=self.agregar_tarea)
        self.boton_agregar.grid(row=0, column=2, padx=10, pady=10)

        self.lista_tareas = tk.Listbox(self.root, font=("Arial", 12), selectmode=tk.SINGLE, height=12, width=50)
        self.lista_tareas.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.boton_completar = tk.Button(self.root, text="Marcar Completada", font=("Arial", 12), command=self.marcar_completada)
        self.boton_completar.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.boton_eliminar = tk.Button(self.root, text="Eliminar Tarea", font=("Arial", 12), command=self.eliminar_tarea)
        self.boton_eliminar.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.boton_salir = tk.Button(self.root, text="Salir", font=("Arial", 12), command=self.root.quit)
        self.boton_salir.grid(row=2, column=2, padx=10, pady=5, sticky="e")

        self.root.bind("<c>", lambda event: self.marcar_completada())
        self.root.bind("<d>", lambda event: self.eliminar_tarea())
        self.root.bind("<Delete>", lambda event: self.eliminar_tarea())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def agregar_tarea(self):
        """Agrega una nueva tarea a la lista de tareas."""
        tarea = self.entrada_tarea.get()
        if tarea.strip():
            self.lista_tareas.insert(tk.END, tarea)
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

    def marcar_completada(self):
        """Marca la tarea seleccionada como completada."""
        try:
            tarea_seleccionada = self.lista_tareas.curselection()[0]
            texto_tarea = self.lista_tareas.get(tarea_seleccionada)
            self.lista_tareas.delete(tarea_seleccionada)
            self.lista_tareas.insert(tarea_seleccionada, f"[Completada] {texto_tarea}")
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcarla como completada.")

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada de la lista."""
        try:
            tarea_seleccionada = self.lista_tareas.curselection()[0]
            self.lista_tareas.delete(tarea_seleccionada)
        except IndexError:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminarla.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionTareas(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

class AgendaPersonal:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        frame_lista = tk.Frame(root)
        frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(frame_lista, columns=('Fecha', 'Hora', 'Descripción'), show='headings')
        self.tree.heading('Fecha', text='Fecha')
        self.tree.heading('Hora', text='Hora')
        self.tree.heading('Descripción', text='Descripción')
        self.tree.pack(fill=tk.BOTH, expand=True)

        frame_entrada = tk.Frame(root)
        frame_entrada.pack(pady=10)

        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_fecha = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_hora = tk.Entry(frame_entrada)
        self.entry_hora.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_descripcion = tk.Entry(frame_entrada)
        self.entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

    def agregar_evento(self):
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_descripcion.get()

        if fecha and hora and descripcion:
            self.tree.insert('', 'end', values=(fecha, hora, descripcion))
            self.entry_hora.delete(0, tk.END)
            self.entry_descripcion.delete(0, tk.END)
        else:
            messagebox.showwarning("Datos incompletos", "Por favor, completa todos los campos.")

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este evento?")
            if confirmacion:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Sin selección", "Por favor, selecciona un evento para eliminar.")
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox

def agregar_elemento():
    """
    Función que toma el texto ingresado en el campo de texto,
    lo agrega a la lista y limpia el campo de entrada.
    Si el campo está vacío, muestra una advertencia.
    """
    dato = entry_dato.get()
    if dato:
        listbox.insert(tk.END, dato)
        entry_dato.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor ingresa un dato.")
def limpiar_lista():
    """
    Función que elimina todos los elementos de la lista.
    """
    listbox.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

label_instruccion = tk.Label(ventana, text="Ingrese un dato:")
label_instruccion.pack(pady=5)

entry_dato = tk.Entry(ventana, width=40)
entry_dato.pack(pady=5)

btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
btn_agregar.pack(pady=5)

listbox = tk.Listbox(ventana, width=50, height=10)  # Tamaño de la lista
listbox.pack(pady=5)

btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
btn_limpiar.pack(pady=5)

ventana.mainloop()

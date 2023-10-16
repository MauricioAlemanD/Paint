
import tkinter as tk
from tkinter.colorchooser import askcolor

def abrir_selector_color():
    color = askcolor()  # Abre el cuadro de diálogo de selección de color
    if color[1]:
        # La selección de color se realizó y se actualiza la variable
        color_elegido.set(color[1])

ventana = tk.Tk()
ventana.title("Selector de Color")

# Variable para almacenar el color seleccionado
color_elegido = tk.StringVar()

# Botón para abrir el selector de color
boton_color = tk.Button(ventana, text="Seleccionar Color", command=abrir_selector_color)
boton_color.pack()

# Etiqueta para mostrar el color seleccionado
etiqueta_color = tk.Label(ventana, textvariable=color_elegido)
etiqueta_color.pack()

ventana.mainloop()
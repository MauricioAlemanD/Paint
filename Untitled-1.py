import tkinter as tk
from tkinter import filedialog

def guardarArchivo(canvas):
    print("Guardando")
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPG files", "*.jpg")])
    if file_path:
        x = canvas.winfo_rootx()
        y = canvas.winfo_rooty()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        image = ImageGrab.grab((x, y, x1, y1))
        image.save(file_path)

root = tk.Tk()
Frame1 = tk.Frame(root, height=50, width=1300, bg="gray")
Frame1.grid(row=0, column=0, sticky="NW")
Frame2 = tk.Frame(root, height=500, width=1300, bg="white")
Frame2.grid(row=1, column=0)

canvas = tk.Canvas(Frame2, height=500, width=1300, bg="white")
canvas.grid(row=0, column=0)
canvas.create_line(100, 400, 440, 69)
canvas.create_rectangle(100, 100, 200, 200, fill="green")

# Crear el menú
menu = tk.Menu(root)
root.config(menu=menu)
save_menu = tk.Menu(menu)
menu.add_cascade(label="Archivo", menu=save_menu)

# Agregar una opción para guardar usando una función lambda
save_menu.add_command(label="Guardar", command=lambda: guardarArchivo(canvas))

root.mainloop()
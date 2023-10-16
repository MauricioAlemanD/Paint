from tkinter import *

root = Tk()
root.title("Vangogh")
root.geometry("1300x600")

Frame1 = Frame(root, height=100, width=1300, bg="gray")
Frame1.grid(row=0, column=0, sticky="NW")

toolsFrame = Frame(Frame1, height=100, width=100, bg="blue")
toolsFrame.grid(row=0, column=0)

# Función que se ejecutará cuando se haga clic en una opción del menú
def opcion_menu():
    # Puedes agregar la funcionalidad que desees aquí
    pass

# Crear un Menubutton en el marco toolsFrame
menu_button = Menubutton(toolsFrame, text="Menú")
menu_button.menu = Menu(menu_button)
menu_button["menu"] = menu_button.menu

# Agregar opciones al menú
menu_button.menu.add_command(label="Abrir", command=opcion_menu)
menu_button.menu.add_command(label="Guardar", command=opcion_menu)
menu_button.menu.add_separator()
menu_button.menu.add_command(label="Salir", command=root.quit)

menu_button.grid(row=0, column=0)

root.mainloop()
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import filedialog
from tkinter.ttk import Combobox
from PIL import Image, ImageGrab,ImageTk  # Agrega la importación de ImageGrab


root = Tk()
root.title("Vangogh")
root.geometry("1300x600")

# Creacion de variables de herramientas boleanas

lapizOn = True
gomaOn = False
paletaOn = False
archivoOn = False
nImg = False

posMX = 0
posMY = 0

# Creacion de las funciones abrir archivo y nuevo archivo

def abrirArchivo(canva):
    global archivoOn
    if archivoOn == False:
        archivoOn = True

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.gif *.bmp *.ppm *.pgm")])
    if file_path:
        imagen = Image.open(file_path)
        imagen = ImageTk.PhotoImage(imagen)
        canva.create_image(0, 0, anchor=NW, image=imagen)
        # Almacenamos la imagen como una propiedad del marco (Frame2) para evitar que se elimine
        canva.imagen = imagen
        global paletaOn
        if paletaOn == True:
            canvas.grid(row=0, column=1) 
        else:
            canvas.grid(row=0, column=0) 
        canva.tag_lower(imagen)


def nuevoArchivo():
    pass

# Creacion de las finciones de guardar archivo y guardar como

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

def guardarComo(canvas):
    print("Guardadno como")
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg")])
    if file_path:
        extension = file_path.split('.')[-1].lower()

        x = canvas.winfo_rootx()
        y = canvas.winfo_rooty()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        image = ImageGrab.grab((x, y, x1, y1))

        if extension == "jpg":
            image = image.convert("RGB")

        image.save(file_path)

# Creacion de la funcion de rehacer y deshacer

def deshacerCambio():
    pass
def rehacerCambio():
    pass
# Creacion de la barra de menú

menubar = Menu(root)
root.config(menu=menubar)

#Crea la barra del menu de archivo, del meunu de guardado y atras y adelantar

file_menu = Menu(menubar,tearoff=0)
save_menu = Menu(menubar,tearoff=0)

menubar.add_cascade(label="Archivo",menu=file_menu)
menubar.add_cascade(label="Guardar",menu=save_menu)
menubar.add_command(label="Deshacer cambio", command=deshacerCambio)
menubar.add_command(label="Rehacer cambio",command=rehacerCambio)

file_menu.add_command(label="Abrir archivo",command=lambda: abrirArchivo(canvas))
file_menu.add_command(label="Nuevo archivo",command=lambda: nuevoArchivo(canvas))

save_menu.add_command(label="Guardar",command=lambda: guardarArchivo(canvas))
save_menu.add_command(label="Guardar como",command=lambda: guardarComo(canvas))

# Crear la barra de herramientas

Frame1 = Frame(root , height = 50 , width = 1300 , bg="gray")
Frame1.grid(row=0,column=0 , sticky="NW")

#Funciones de seleccion de colores

ColorPrincipal = "#000000"
ColorSecundario = "#ffffff"
colorElegido =""
colorElegido2 = StringVar()

# Crear la funcion del color picker
def abrirColorPicker():
    color = askcolor()
    if color[1]:
        colorElegido2.set(color[1])
        print(colorElegido2.get())
        global ColorPrincipal
        ColorPrincipal = colorElegido2.get()
    btnColorPrincipal["bg"]=ColorPrincipal

def abrirColorPicker2():
    color = askcolor()
    if color[1]:
        colorElegido2.set(color[1])
        print(colorElegido2.get())
        global ColorSecundario
        ColorSecundario = colorElegido2.get()
    btnColorSecundario["bg"]=ColorSecundario


# Crear la funcion de cada boton de la barra de herramientas

def seleccionColor1():
    global ColorPrincipal
    ColorPrincipal = "#ff0000"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor2():
    global ColorPrincipal
    ColorPrincipal = "#00FF00"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor3():
    global ColorPrincipal
    ColorPrincipal = "#0000FF"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor4():
    global ColorPrincipal
    ColorPrincipal = "#FFFF00"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor5():
    global ColorPrincipal
    ColorPrincipal = "#00FFFF"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor6():
    global ColorPrincipal
    ColorPrincipal = "#FF00FF"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor7():
    global ColorPrincipal
    ColorPrincipal = "#FFFFFF"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor8():
    global ColorPrincipal
    ColorPrincipal = "#000000"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor9():
    global ColorPrincipal
    ColorPrincipal = "#808080"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor10():
    global ColorPrincipal
    ColorPrincipal = "#C0C0C0"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor11():
    global ColorPrincipal
    ColorPrincipal = "#FFD700"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor12():
    global ColorPrincipal
    ColorPrincipal = "#FFC0CB"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor13():
    global ColorPrincipal
    ColorPrincipal = "#FFA500"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor14():
    global ColorPrincipal
    ColorPrincipal = "#00FF00"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor15():
    global ColorPrincipal
    ColorPrincipal = "#800080"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor16():
    global ColorPrincipal
    ColorPrincipal = "#A52A2A"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor17():
    global ColorPrincipal
    ColorPrincipal = "#000080"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor18():
    global ColorPrincipal
    ColorPrincipal = "#40E0D0"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor19():
    global ColorPrincipal
    ColorPrincipal = "#808000"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal
def seleccionColor20():
    global ColorPrincipal
    ColorPrincipal = "#E6E6FA"
    print(ColorPrincipal)
    btnColorPrincipal["bg"]=ColorPrincipal


# Funcion Lapiz
def on_buttonLapiz_click():
    canvas.unbind("<Button-1>")  # Desvincular otros eventos
    print("Lapiz")
    global gomaOn
    global lapizOn

    if gomaOn == True and lapizOn == False:
        global colorElegido
        global ColorPrincipal
        global ColorSecundario
        print(ColorPrincipal)
        colorElegido = ColorPrincipal
        ColorPrincipal = ColorSecundario
        btnColorPrincipal["bg"]=ColorPrincipal
        ColorSecundario = colorElegido
        btnColorSecundario["bg"]=colorElegido

    gomaOn = False

    canvas.bind("<B1-Motion>" , paint)
    canvas.bind("<ButtonRelease-1>" , paint)
# Funcion Goma
def on_buttonGoma_click():
    print("Goma")
    canvas["cursor"] = DOTBOX
    global gomaOn
    global lapizOn
    global colorElegido
    global ColorPrincipal
    global ColorSecundario
    gomaOn = True
    lapizOn = False
    colorElegido = ColorPrincipal
    ColorPrincipal = ColorSecundario
    btnColorPrincipal["bg"]=ColorPrincipal
    ColorSecundario = colorElegido
    btnColorSecundario["bg"]=colorElegido
# Funcion Texto
def agregarTexto(event):
    # Función para agregar texto en la posición del clic
    x, y = event.x, event.y

    # Ventana emergente para ingresar el texto
    ventana_texto = Toplevel(root)
    ventana_texto.title("Ingresar Texto")
    # Cuadro de selección de tamaño
    tamano_label = Label(ventana_texto, text="Tamaño de letra:")
    tamano_label.pack()
    tamano = Combobox(ventana_texto, values=[10, 12, 14, 16, 18, 20])
    tamano.pack()
    fuente_label = Label(ventana_texto, text="Fuente:")
    fuente_label.pack()
    # Lista de fuentes comunes
    fuentes_comunes = ["Arial", "Times New Roman", "Courier New", "Verdana"]
    fuente = Combobox(ventana_texto, values=fuentes_comunes)
    fuente.pack()
    texto = Entry(ventana_texto)
    texto.pack()

    def insertarTexto():
        global ColorPrincipal
        texto_ingresado = texto.get()
        tamano_letra = tamano.get()
        fuente_letra = fuente.get()
        canvas.create_text(x, y, text=texto_ingresado, font=(fuente_letra, tamano_letra), fill=ColorPrincipal,anchor=W)
        ventana_texto.destroy()

    boton_insertar = Button(ventana_texto, text="Insertar", command=insertarTexto)
    boton_insertar.pack()

def on_buttonTexto_click():
    canvas.unbind("<Button-1>")  # Desvincular otros eventos
    canvas.bind("<Button-1>", agregarTexto)

# Funcion colocar imagen

def posicion(event,canvas):
    global paletaOn

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.gif *.bmp *.ppm *.pgm")])
    if file_path:
        imagen = Image.open(file_path)
        imagen = ImageTk.PhotoImage(imagen)
        nuevo_canvas = Canvas(canvas, height=500, width=1300,)
        nuevo_canvas.create_image(event.x, event.y, anchor=NW, image=imagen)
        nuevo_canvas.imagen = imagen
        if paletaOn:
            nuevo_canvas.grid(row=0, column=1)
        else:
            nuevo_canvas.grid(row=0, column=0)
        canvas.tag_lower(imagen)

def on_buttonImagen_click(canva):
    print("Imagen")
    canvas["cursor"] = "cross"
    canvas.unbind("<Button-1>")
    canvas.bind("<Button-1>", lambda event: posicion(event, canvas))

# Funcion Paleta de colores
def on_buttonPaleta_click():
    global paletaOn
    if paletaOn == False:
        paletaOn = True
    elif paletaOn == True:
        paletaOn = False
        Paleta.destroy()

    print("Paleta de colores")

    Paleta = Frame(Frame2,height=500,width=50)
    Paleta.grid(column=0,row=0,sticky="N")
    canvas.grid(column=1,row=0)
    # Crea seleccion de botones

    Color1 = Button(Paleta,bg="#ff0000",command=seleccionColor1)
    Color1.grid(row=0,column=0)
    
    Color2 = Button(Paleta,bg="#00FF00",command=seleccionColor2)
    Color2.grid(row=0,column=1)

    Color3 = Button(Paleta,bg="#0000FF",command=seleccionColor3)
    Color3.grid(row=1,column=0)

    Color4 = Button(Paleta,bg="#FFFF00",command=seleccionColor4)
    Color4.grid(row=1,column=1)

    Color5 = Button(Paleta,bg="#00FFFF",command=seleccionColor5)
    Color5.grid(row=2,column=0)

    Color6 = Button(Paleta,bg="#FF00FF",command=seleccionColor6)
    Color6.grid(row=2,column=1)
    
    Color7 = Button(Paleta,bg="#FFFFFF",command=seleccionColor7)
    Color7.grid(row=3,column=0)

    Color8 = Button(Paleta,bg="#000000",command=seleccionColor8)
    Color8.grid(row=3,column=1)

    Color9 = Button(Paleta,bg="#808080",command=seleccionColor9)
    Color9.grid(row=4,column=0)

    Color10 = Button(Paleta,bg="#C0C0C0",command=seleccionColor10)
    Color10.grid(row=4,column=1)

    Color11 = Button(Paleta,bg="#FFD700",command=seleccionColor11)
    Color11.grid(row=5,column=0)
    
    Color12 = Button(Paleta,bg="#FFC0CB",command=seleccionColor12)
    Color12.grid(row=5,column=1)

    Color13 = Button(Paleta,bg="#FFA500",command=seleccionColor13)
    Color13.grid(row=6,column=0)

    Color14 = Button(Paleta,bg="#00FF00",command=seleccionColor14)
    Color14.grid(row=6,column=1)

    Color15 = Button(Paleta,bg="#800080",command=seleccionColor15)
    Color15.grid(row=7,column=0)

    Color16 = Button(Paleta,bg="#A52A2A",command=seleccionColor16)
    Color16.grid(row=7,column=1)
    
    Color17 = Button(Paleta,bg="#000080",command=seleccionColor17)
    Color17.grid(row=8,column=0)

    Color18 = Button(Paleta,bg="#40E0D0",command=seleccionColor18)
    Color18.grid(row=8,column=1)

    Color19 = Button(Paleta,bg="#808000",command=seleccionColor19)
    Color19.grid(row=9,column=0)

    Color20 = Button(Paleta,bg="#E6E6FA",command=seleccionColor20)
    Color20.grid(row=9,column=1)

    ColorPersonalizado = Button(Paleta,image=imgPaleta,text="CP",command=abrirColorPicker)
    ColorPersonalizado.grid(row=10,column=0)

    
    



# Funcion seleccion
def on_buttonSeleccion_click():
    print("Seleccion")
# Funcion copiar
def on_buttonCopiar_click():
    print("Copiar")
# Funcion pegar
def on_buttonPegar_click():
    print("Pegar")
# Funcion cortar
def on_buttonCortar_click():
    print("Cortar")
# Funcion bote
def on_buttonBote_click():
    print("Bote")
# Funcion grafica
def on_buttonGrafica_click():
    print("Grafica")
# Funcion linea
def on_buttonLinea_click():
    print("linea")
# Funcion curva
def on_buttonCurva_click():
    print("Curva")
# Funcion formas
def on_buttonFormas_click():
    print("Formas")
#Funcion Pincel
def on_buttonPincel_click():
    print("Pincel")
# Funcion rotar
def on_buttonRotar_click():
    print("Rotar")
# Funcion ampliar
def on_buttonAmpliar_click():
    print("Ampliar")
# Funcion reducir
def on_buttonReducir_click():
    print("Reducir")


#Cargar imagen de nodos
imgLapiz = PhotoImage(file="resources/ico_lapiz.png")
imgGoma = PhotoImage(file="resources/ico_goma.png")
imgTexto = PhotoImage(file="resources/ico_texto.png")
imgImagen = PhotoImage(file="resources/ico_imagen.png")
imgPaleta = PhotoImage(file="resources/ico_paleta.png")
imgSeleccion = PhotoImage(file="resources/ico_seleccion.png")
imgCopiar = PhotoImage(file="resources/ico_copiar.png")
imgPegar = PhotoImage(file="resources/ico_pegar.png")
imgCortar = PhotoImage(file="resources/ico_cortar.png")
imgBote = PhotoImage(file="resources/ico_bote.png")
imgGrafica = PhotoImage(file="resources/ico_grafica.png")
imgLinea = PhotoImage(file="resources/ico_linea.png")
imgCurva = PhotoImage(file="resources/ico_curva.png")
imgFormas = PhotoImage(file="resources/ico_formas.png")
imgPincel = PhotoImage(file="resources/ico_pincel.png")
imgRotar = PhotoImage(file="resources/ico_rotar.png")
imgAmpliar = PhotoImage(file="resources/ico_ampliar.png")
imgReducir = PhotoImage(file="resources/ico_reducir.png")

# Crear boton de lapiz
btnLapiz = Button(Frame1,image=imgLapiz,command=on_buttonLapiz_click)
btnLapiz.grid(row=0,column=0)
# Crear boton de goma 
btnGoma = Button(Frame1,image=imgGoma,command=on_buttonGoma_click)
btnGoma.grid(row=0,column=1)
# Crear boton de texto
btnTexto = Button(Frame1,image=imgTexto,command=on_buttonTexto_click)
btnTexto.grid(row=0,column=2)
# Crear boton de imagen
btnImagen = Button(Frame1,image=imgImagen,command=lambda: on_buttonImagen_click(canvas))
btnImagen.grid(row=0,column=3)
# Crear boton de paleta de colores
btnPaleta = Button(Frame1,image=imgPaleta,command=on_buttonPaleta_click)
btnPaleta.grid(row=0,column=4)
# Crear boton de seleccion
btnSeleccion = Button(Frame1,image=imgSeleccion,command=on_buttonSeleccion_click)
btnSeleccion.grid(row=0,column=5)
# Crear boton de copiar
btnCopiar = Button(Frame1,image=imgCopiar,command=on_buttonCopiar_click)
btnCopiar.grid(row=0,column=6)
# Crear boton de pegar
btnPegar = Button(Frame1,image=imgPegar,command=on_buttonPegar_click)
btnPegar.grid(row=0,column=7)
# Crear boton de cortar
btnCortar = Button(Frame1,image=imgCortar,command=on_buttonCortar_click)
btnCortar.grid(row=0,column=8)
# Crear boton de bote
btnBote = Button(Frame1,image=imgBote,command=on_buttonBote_click)
btnBote.grid(row=0,column=9)
# Crear boton de grafica
btnGrafica = Button(Frame1,image=imgGrafica,command=on_buttonGrafica_click)
btnGrafica.grid(row=0,column=10)
# Crear boton de linea
btnLinea = Button(Frame1,image=imgLinea,command=on_buttonLinea_click)
btnLinea.grid(row=0,column=11)
# Crear boton de curva
btnCurva = Button(Frame1,image=imgCurva,command=on_buttonCurva_click)
btnCurva.grid(row=0,column=12)
# Crear boton de formas
btnFormas = Button(Frame1,image=imgFormas,command=on_buttonFormas_click)
btnFormas.grid(row=0,column=13)
# Crear boton de pincel
btnPincel = Button(Frame1,image=imgPincel,command=on_buttonPincel_click)
btnPincel.grid(row=0,column=14)
# Crear boton de rotar
btnRotar = Button(Frame1,image=imgRotar,command=on_buttonRotar_click)
btnRotar.grid(row=0,column=15)
# Crear boton de ampliar
btnAmpliar = Button(Frame1,image=imgAmpliar,command=on_buttonAmpliar_click)
btnAmpliar.grid(row=0,column=16)
# Crear boton de reducir
btnReducir = Button(Frame1,image=imgReducir,command=on_buttonReducir_click)
btnReducir.grid(row=0,column=17)
# Crear boton de color principal
btnColorPrincipal = Button(Frame1,text="Color principal",bg=ColorPrincipal,command=abrirColorPicker)
btnColorPrincipal.grid(row=0,column=19)
# Crear boton de color secundario
btnColorSecundario = Button(Frame1,text="Color secundario",bg=ColorSecundario,command=abrirColorPicker2)
btnColorSecundario.grid(row=0,column=20)
# Crear el canva para la edicion

Frame2 = Frame(root , height = 500 , width = 1300 , bg="white")
Frame2.grid(row=1,column=0)

canvas = Canvas(Frame2 , height = 500 , width = 1300 , bg = "white")
canvas.grid(row = 0   , column = 0)


prevPiont = [0,0]
currentPoint = [0,0]

print(ColorPrincipal)

def paint(event):
    print(event.type," ",ColorPrincipal)
    global prevPiont
    global currentPoint


    x = event.x
    y = event.y
    currentPoint = [x,y]
    #canvas.create_line(x,y,x+90,y+90,fill="blue")
    #canvas.create_rectangle(x,y,x+20,y+20,fill="black")
    #canvas.create_oval(x,y,x+20,y+20,fill="black")

    if prevPiont != [0,0]:
        global archivoOn 
        if archivoOn == True:
            canvas.create_line(prevPiont[0],prevPiont[1],currentPoint[0],currentPoint[1],fill=ColorPrincipal)
        else:
            canvas.create_line(prevPiont[0],prevPiont[1],currentPoint[0],currentPoint[1],fill=ColorPrincipal)
            
    prevPiont = currentPoint

    if event.type == "5":
        prevPiont = [0,0]

root.resizable(False,False)

root.mainloop()


import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import Funciones as Back
import FuncionesFront as Front
##################################################################################
# Configuracion de la raiz 
raiz = Tk()
raiz.title('Laboratorio Huffman')
raiz.iconbitmap('./usta.ico')
raiz.geometry('1000x500')
raiz.resizable(0,0)
raiz.config(bg='#FFFFFF')
# Variables Globales
colorBotones = '#F54500'
colorFondo = '#FFFFFF'
##################################################################################
# Frame Principal
principal = Frame(raiz)
principal.config(width="1500", height="500", bg=colorFondo)
principal.pack()
## Elementos del frame principal
### Textos
textPalindromo = ttk.Label(principal,
                           text='Codificación Huffman',
                           background=colorFondo,
                           font=('Calibri', 30, 'bold'))
textPalindromo.place(x=320, y=40)
textIngreso = ttk.Label(principal,
                        text='Ingrese el mensaje : ',
                        background=colorFondo,
                        font=('Calibri', 15, 'bold'))
textIngreso.place(x=400, y=110)
textIngreso2 = ttk.Label(principal,
                        text='Entre 10-50 caracteres, sin caracteres especiales',
                        background=colorFondo,
                        font=('Calibri', 12, 'bold'))
textIngreso2.place(x=308, y=135)
textError = ttk.Label(principal,
                    foreground='#FF0000',
                    font=('Calibri', 16, 'bold'),
                    background=colorFondo
                    )
textError.place_forget()
### Input 
mensaje = Text(principal)
mensaje.config(font=('Calibri', 14, 'bold'), 
            bg='#F59C6B',
            bd=0,
            width=60,
            height=1,
            padx=5,
            pady=15
            )
mensaje.place(x=200, y=170)
### Botones
#### Boton de Calcular
btnCalcular = Canvas(principal)
btnCalcular.config(highlightthickness=0, height=70, bg=colorFondo,)
btnCalcular.create_oval(0,0,200,60,fill=colorBotones,outline=colorBotones)
btnCalcular.create_text(100,30,fill=colorFondo,font="Calibri 16 bold",text="Calcular")
btnCalcular.place(x=390, y=270)
def CambiarResultado(event):   
    textMensaje = Back.back(mensaje.get('1.0', 'end-1c'))
    if textMensaje == 1:
        textError.config(text='Error1 : Tamaño del mensaje Invalido')
        mensaje.delete('1.0', tk.END)
        textError.place(x=320, y=360)
    elif textMensaje == 2:
        textError.config(text='Error2 : Contiene caracteres Invalidos')
        mensaje.delete('1.0', tk.END)
        textError.place(x=320, y=360)
    else:
        textR2.config(text=mensaje.get('1.0', 'end-1c'))
        textMB2.config(text=mensaje.get('1.0', 'end-1c'))
        longi = 'Long'
        ent = 'Entropia'
        efi = 'Eficiencia'
        r = 'Taza_De_Comprencion'
        textV2.config(text=f'Longitud Promedio = {textMensaje[longi]}')
        textMensaje.pop(longi)
        textV3.config(text=f'Entropia = {textMensaje[ent]}')
        textMensaje.pop('Entropia')
        textV4.config(text=f'Eficiencia = {textMensaje[efi]}')
        textMensaje.pop('Eficiencia')
        textV5.config(text=f'Taza De Comprencion = {textMensaje[r]}')
        textMensaje.pop('Taza_De_Comprencion')
        contador = 1
        for x in textMensaje:
            if contador <= 6 :
                diclist1.update({x: textMensaje[x]})
            elif contador > 6 and contador <= 12 : 
                diclist2.update({x: textMensaje[x]})
            elif contador > 12 and contador <= 18 :
                diclist3.update({x: textMensaje[x]})
            elif contador > 18 and contador <= 24 :
                diclist4.update({x: textMensaje[x]})
            elif contador > 24 and contador <= 30 :
                diclist5.update({x: textMensaje[x]})
            elif contador > 30: 
                diclist6.update({x: textMensaje[x]})
            contador = contador + 1
        lista1 = Front.listar(resultados, colorFondo, colorBotones, diclist1)
        lista1.place(x=50, y=180)
        lista2 = Front.listar(resultados, colorFondo, colorBotones, diclist2)
        lista2.place(x=200, y=180)
        lista3 = Front.listar(resultados, colorFondo, colorBotones, diclist3)
        lista3.place(x=350, y=180)
        lista4 = Front.listar(resultados, colorFondo, colorBotones, diclist4)
        lista4.place(x=500, y=180)
        lista5 = Front.listar(resultados, colorFondo, colorBotones, diclist5)
        lista5.place(x=650, y=180)
        lista6 = Front.listar(resultados, colorFondo, colorBotones, diclist6)
        lista6.place(x=800, y=180)
        textMB4.insert(1.0, Front.txtBin(textMensaje, mensaje.get('1.0', 'end-1c')))
        textMB4.config(state=DISABLED)
        resultados.pack()
        principal.pack_forget()
btnCalcular.bind('<Button-1>', CambiarResultado)
#### Boton de Creditos
btnCreditos = Canvas(principal)
btnCreditos.config(highlightthickness=0, height=70, bg=colorFondo,)
btnCreditos.create_rectangle(0,0,499,50,fill=colorBotones,outline=colorBotones)
btnCreditos.create_text(180,25,fill=colorFondo,font="Calibri 16 bold",text="Creditos")
btnCreditos.place(x=120, y=450)
def CambioCreditos(event):
    principal.pack_forget()
    creditos.pack()
btnCreditos.bind("<Button-1>", CambioCreditos)
#### Boton de Salir
btnSalir = Canvas(principal)
btnSalir.config(highlightthickness=0, height=70, bg=colorFondo,)
btnSalir.create_rectangle(0,0,499,50,fill=colorBotones,outline=colorBotones)
btnSalir.create_text(180,25,fill=colorFondo,font="Calibri 16 bold",text="Salir")
btnSalir.place(x=501, y=450)
def Salir(event):
    raiz.quit()
btnSalir.bind("<Button-1>", Salir)
########################################################################################################
# Frame Creditos
creditos = Frame(raiz)
creditos.config(bg=colorFondo,width="500", height="500")
## Elementos Del Fame
### Textos
textC1 = ttk.Label(creditos, 
                    text="Creditos 2020-2",
                    foreground=colorBotones,
                    font=('Calibri', 24, 'bold'), 
                    background=colorFondo)
textC1.place(x=120, y=40)
textC2 = ttk.Label(creditos, 
                    text="Sistemas De Telecomunicaciones II",
                    font=('Calibri', 16, 'bold'), 
                    background=colorFondo)
textC2.place(x=80, y=90)
textC3 = ttk.Label(creditos, 
                    text="ING. Gustavo Alonso Chica Pedraza",
                    font=('Calibri', 16, 'bold'), 
                    background=colorFondo)
textC3.place(x=80, y=130)
textC4 = ttk.Label(creditos, 
                    text="Integrantes :",
                    foreground=colorBotones,
                    font=('Calibri', 16, 'bold'), 
                    background=colorFondo)
textC4.place(x=120, y=160)
textC5 = ttk.Label(creditos, 
                    text="Andrei Lizandro Riaño Tuta",
                    font=('Calibri', 16, 'bold'), 
                    background=colorFondo)
textC5.place(x=80, y=190)
textC6 = ttk.Label(creditos, 
                    text="Johann Stev Castellanos Gonzalez",
                    font=('Calibri', 16, 'bold'), 
                    background=colorFondo)
textC6.place(x=80, y=230)
textC7 = ttk.Label(creditos, 
                    text="Andres Nicolas Linares Chaparro",
                    font=('Calibri', 16, 'bold'), 
                    background=colorFondo)
textC7.place(x=80, y=270)
#########################################################################################################
# Frame De Resultados1
resultados = Frame(raiz)
resultados.config(bg=colorFondo,width="1000", height="500")
# Elemntos Del Frame
## Textos
textR1 = ttk.Label(resultados,
                    text="El texto :",
                    font=('Calibri', 18, 'bold'), 
                    background=colorFondo)
textR1.place(x=400, y=40)
textR2 = ttk.Label(resultados,
                    font=('Calibri', 16, 'bold'),
                    foreground=colorBotones,
                    background=colorFondo)
textR2.place(x=300, y=80)
textR3 = ttk.Label(resultados,
                    text="Contine :",
                    font=('Calibri', 18, 'bold'),
                    background=colorFondo)
textR3.place(x=400, y=120)
### Textos Listas
diclist1 = {}
diclist2 = {}
diclist3 = {}
diclist4 = {}
diclist5 = {}
diclist6 = {}
## Botones 
### Boton de Mensaje en binario
botonMenu = Canvas(resultados)
botonMenu.config(bg=colorFondo, highlightthickness=0)
botonMenu.create_oval(0,0,80,80,fill=colorBotones,outline=colorBotones)
botonMenu.create_text(40,40,fill=colorFondo,font="Calibri 16 bold",text="Bin")
botonMenu.place(x=350, y=400)
def CambioMenu3(event):
    resultados.pack_forget()
    MensajeBin.pack()
botonMenu.bind("<Button-1>", CambioMenu3)
### Boton de Variables Probabilisticas
botonMenu = Canvas(resultados)
botonMenu.config(bg=colorFondo, highlightthickness=0)
botonMenu.create_oval(0,0,80,80,fill=colorBotones,outline=colorBotones)
botonMenu.create_text(40,40,fill=colorFondo,font="Calibri 16 bold",text="Variables")
botonMenu.place(x=450, y=400)
def CambioMenu5(event):
    resultados.pack_forget()
    variables.pack()
botonMenu.bind("<Button-1>", CambioMenu5)
### Boton De Salir
botonSalir = Canvas(resultados)
botonSalir.config(bg=colorFondo, highlightthickness=0)
botonSalir.create_oval(0,0,80,80,fill=colorBotones,outline=colorBotones)
botonSalir.create_text(40,40,fill=colorFondo,font="Calibri 16 bold",text="Salir")
botonSalir.place(x=550, y=400)
botonSalir.bind("<Button-1>", Salir)
#############################################################################################################
# Freame de Menseaje En Binario
MensajeBin =Frame(raiz)
MensajeBin.config(bg=colorFondo,width="1000", height="500")
# Elemntos Del Frame
## Textos
textMB1 = ttk.Label(MensajeBin,
                    text="El texto :",
                    font=('Calibri', 18, 'bold'), 
                    background=colorFondo)
textMB1.place(x=400, y=40)
textMB2 = ttk.Label(MensajeBin,
                    font=('Calibri', 16, 'bold'),
                    foreground=colorBotones,
                    background=colorFondo)
textMB2.place(x=300, y=80)
textMB3 = ttk.Label(MensajeBin,
                    text="El mensaje en binario es :",
                    font=('Calibri', 18, 'bold'),
                    background=colorFondo)
textMB3.place(x=380, y=120)
textMB4 = Text(MensajeBin)
textMB4.config(fg='#000000',
            font=('Calibri', 20, 'bold'), 
            bg=colorFondo,
            bd=0,
            relief="flat",
            width=50
            )
textMB4.place(x=50, y=150)
## Botones
### Boton de Regresar
botonRegresar = Canvas(MensajeBin)
botonRegresar.config(bg=colorFondo, highlightthickness=0)
botonRegresar.create_oval(0,0,80,80,fill=colorBotones,outline=colorBotones)
botonRegresar.create_text(40,40,fill=colorFondo,font="Calibri 16 bold",text="Antes")
botonRegresar.place(x=550, y=400)
def CambioMenu4(event):
    MensajeBin.pack_forget()
    resultados.pack()
botonRegresar.bind("<Button-1>", CambioMenu4)
### Boton De Salir
botonSalir = Canvas(MensajeBin)
botonSalir.config(bg=colorFondo, highlightthickness=0)
botonSalir.create_oval(0,0,80,80,fill=colorBotones,outline=colorBotones)
botonSalir.create_text(40,40,fill=colorFondo,font="Calibri 16 bold",text="Salir")
botonSalir.place(x=650, y=400)
botonSalir.bind("<Button-1>", Salir)
###########################################################################################################################################
# Frame de Variables Probabilisticas
variables =Frame(raiz)
variables.config(bg=colorFondo,width="1000", height="500")
# Elementos del Frame 
### Textos
textV1 = ttk.Label(variables, 
                    text="Variables",
                    foreground=colorBotones,
                    font=('Calibri', 24, 'bold'), 
                    background=colorFondo)
textV1.place(x=320, y=60)
textV2 = ttk.Label(variables, 
                    font=('Calibri', 16, 'bold'), 
                    background=colorFondo)
textV2.place(x=280, y=110)
textV3 = ttk.Label(variables, 
                    font=('Calibri', 16, 'bold'), 
                    background=colorFondo)
textV3.place(x=280, y=150)
textV4 = ttk.Label(variables, 
                    font=('Calibri', 16, 'bold'), 
                    background=colorFondo)
textV4.place(x=280, y=180)
textV5 = ttk.Label(variables, 
                    font=('Calibri', 16, 'bold'), 
                    background=colorFondo)
textV5.place(x=280, y=210)
## Botones
### Boton de Regresar
botonRegresar = Canvas(variables)
botonRegresar.config(bg=colorFondo, highlightthickness=0)
botonRegresar.create_oval(0,0,80,80,fill=colorBotones,outline=colorBotones)
botonRegresar.create_text(40,40,fill=colorFondo,font="Calibri 16 bold",text="Antes")
botonRegresar.place(x=550, y=400)
def CambioMenu6(event):
    variables.pack_forget()
    resultados.pack()
botonRegresar.bind("<Button-1>", CambioMenu6)
### Boton De Salir
botonSalir = Canvas(variables)
botonSalir.config(bg=colorFondo, highlightthickness=0)
botonSalir.create_oval(0,0,80,80,fill=colorBotones,outline=colorBotones)
botonSalir.create_text(40,40,fill=colorFondo,font="Calibri 16 bold",text="Salir")
botonSalir.place(x=650, y=400)
botonSalir.bind("<Button-1>", Salir)


raiz.mainloop()
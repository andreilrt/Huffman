import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

def colocar(dic, textRL0, textRL1, textRL2, textRL3, textRL4, textRL5):
    contador = 0
    for x in dic:
        if contador == 0 :
            textRL0.config(text=f'{x} : {dic[x]}')
        if contador == 1 :
            textRL1.config(text=f'{x} : {dic[x]}')
        if contador == 2 :
            textRL2.config(text=f'{x} : {dic[x]}')
        if contador == 3 :
            textRL3.config(text=f'{x} : {dic[x]}')
        if contador == 4 :
            textRL4.config(text=f'{x} : {dic[x]}')
        if contador == 5 :
            textRL5.config(text=f'{x} : {dic[x]}')
        contador = contador + 1

def listar(raiz, colorFondo, colorBotones, dic):
    resultados = Frame(raiz)
    resultados.config(bg=colorFondo, width="150", height="200")
    textRL0 = ttk.Label(resultados,
                        text='',
                        font=('Calibri', 16, 'bold'),
                        foreground=colorBotones,
                        background=colorFondo)
    textRL0.place(x=0, y=0)
    textRL1 = ttk.Label(resultados,
                        text='',
                        font=('Calibri', 16, 'bold'),
                        foreground=colorBotones,
                        background=colorFondo)
    textRL1.place(x=0, y=30)
    textRL2 = ttk.Label(resultados,
                        text='',
                        font=('Calibri', 16, 'bold'),
                        foreground=colorBotones,
                        background=colorFondo)
    textRL2.place(x=0, y=60)
    textRL3 = ttk.Label(resultados,
                        text='',
                        font=('Calibri', 16, 'bold'),
                        foreground=colorBotones,
                        background=colorFondo)
    textRL3.place(x=0, y=90)
    textRL4 = ttk.Label(resultados,
                        text='',
                        font=('Calibri', 16, 'bold'),
                        foreground=colorBotones,
                        background=colorFondo)
    textRL4.place(x=0, y=120)
    textRL5 = ttk.Label(resultados,
                        text='',
                        font=('Calibri', 16, 'bold'),
                        foreground=colorBotones,
                        background=colorFondo)
    textRL5.place(x=0, y=150)
    colocar(dic, textRL0, textRL1, textRL2, textRL3, textRL4, textRL5)
    return resultados

def txtBin(dic, mensaje):
    text = ''
    mensaje = mensaje.lower()
    for x in mensaje:
        # Cambiar 
        text = text + str(dic[x])
    return text
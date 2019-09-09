"""
Integrantes:
Yesid Fernando Andica - 201556001
Víctor Manuel Marín Duque - 201556071
Stiven Sepulveda Cano - 201556087
"""

import tkinter as tk
from tkinter import messagebox
import maestrovegas as nreinas

# Gráfica del tablero de juego

def abrirventana2(img, img2, root, valor_reina, img3):

    # Se grafica el tablero de juego dada una matriz, la cual proviene del
    # algoritmo de las vegas:
    def GraficarTablero(matriz):
        for n, i in enumerate(matriz):
            posy = n*40
            for k, j in enumerate(i):
                posx = k*40
                # Se grafica el tablero con las imágenes que se definen en la función 
                # "ventana_principal"
                if n%2==0 and k%2==0 and j==0:
                    tk.Label(frame2, image=img).place(x=posx, y=posy)
                if n%2==0 and k%2==0 and j!=0:
                    tk.Label(frame2, image=img2).place(x=posx, y=posy)
                if n%2==0 and k%2!=0 and j!=0:
                    tk.Label(frame2, image=img3).place(x=posx, y=posy)
                if n%2!=0 and k%2==0 and j!=0:
                    tk.Label(frame2, image=img3).place(x=posx, y=posy)
                if n%2!=0 and k%2!=0 and j==0:
                    tk.Label(frame2, image=img).place(x=posx, y=posy)
                if n%2!=0 and k%2!=0 and j!=0:
                    tk.Label(frame2, image=img2).place(x=posx, y=posy)

    reinas = nreinas.algoritmo(int(valor_reina.get()))

    # El anterior "reinas", se convierte en matriz para poder graficar:
    matriz_tablero = nreinas.matriz(reinas)
    print(reinas)

    # Hacer que la ventana_raiz principal 'root' se cierre:
    root.withdraw()
    # Crear la segunda ventana_raiz 'ventana_secundaria', mediante el método toplevel, el cual permite crear una ventana_raiz hija 
    # de la ventana_raiz principal que hereda sus atributos:
    ventana_secundaria = tk.Toplevel()
    ventana_secundaria.title('Tablero')
    frame2 = tk.Frame(ventana_secundaria,bg="#F4F6F7", width=len(matriz_tablero)*40, height=len(matriz_tablero)*40)
    frame2.pack()
    # Se grafica la matriz:
    GraficarTablero(matriz_tablero)

# Ventana principal:

def ventana_principal():
    root = tk.Tk()
    root.title("Juego n reinas")
    frame = tk.Frame(root, width=500, height=500, bg="#F4F6F7")
    frame.pack()

    parametro = tk.StringVar()

    # Se crean las imágenes a graficar, label, entry para ingreso del n y el botón:
    imag = tk.PhotoImage(file="Images/Negro.png")
    imag2 = tk.PhotoImage(file="Images/Reina.png")
    imag3 = tk.PhotoImage(file="Images/Reina2.png")

    texto = tk.Label(frame, text="Ingrese valor de n", bg="#F4F6F7")
    texto.grid(row=0, column=0, padx=20, pady=10)

    entrada = tk.Entry(frame, textvariable=parametro)
    entrada.grid(row=0, column=1, padx=20, pady=10)

    # El botón tiene asociado el evento "abrirventana2", que hace posible que al 
    # puldar click sobre este se desarrolle el graficado del tablero:
    boton = tk.Button(frame, text='Resolver', command=lambda: abrirventana2(imag, imag2, root, parametro, imag3))
    boton.grid(row=1, column=0, pady=30, columnspan=2)

    root.mainloop()


import tkinter as tk
from tkinter import messagebox

def altas():
    messagebox.showinfo("altas", "Realizar una alta")

def bajas():
    messagebox.showinfo("Bajas","Realizar una baja")

def modificaciones():
    messagebox.showinfo("Modificaciones", "Realizar modificaciones")


def liquidar():
    messagebox.showinfo("Liquidar", "Realizar una liquidacion")

def vender():
    messagebox.showinfo("Vender", "Realizar una venta")
    
def comprar():
    messagebox.showinfo("Comprar", "Realizar una venta")

ventana=tk.Tk()
ventana.title("Menú")

menu= tk.Menu(ventana)
ventana.config(menu=menu)

operaciones_menu=tk.Menu(menu)
menu.add_cascade(label="Operaciones", menu=operaciones_menu)
operaciones_menu.add_command(label="Altas", command=altas)
operaciones_menu.add_command(label="Bajas", command=bajas)
operaciones_menu.add_command(label="Modificaciones", command=modificaciones)
operaciones_menu.add_separator()
operaciones_menu.add_command(label="Salir", command=ventana.quit)

transacciones_menu=tk.Menu(menu)
menu.add_cascade(label="Transacciones", menu=transacciones_menu)
transacciones_menu.add_command(label="Liquidar",command=liquidar)
transacciones_menu.add_command(label="Vender",command=vender)
transacciones_menu.add_command(label="Comprar",command=comprar)

ventana.mainloop()

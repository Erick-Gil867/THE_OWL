# -*- coding: utf-8 -*-
"""
@author: Erick Gildardo Avalos Solis
"""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from untitled4 import *
from nervio import *
import numpy as np
window = Tk()
ancho_ventana = 800
alto_ventana = 600
VANDERA = True
x_ventana = window.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = window.winfo_screenheight() // 2 - alto_ventana // 2
X=[]
Y=[]
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
window.title("THE OWL")

window.geometry(posicion)

"""Frame inicial """
frame1 = Frame(window) 
frame1.pack() 
frame1.config(width=800,height=600) 

def clickedc():
    frame1.forget()
    frame2.pack()
    btnc.focus()
    
def clickedm():
    frame1.forget()
    frame4.pack()
    combo_m.set("") 

def clickedu():
    frame1.forget()
    frame3.pack()
    combo.set("") 
    btnc.focus()
    
btnc = Button(frame1,text='Crear',bg="yellow",font=("Arial Bold", 15), command=clickedc)
btnc.configure(height = 2,width = 10)
btnc.place(x=340, y=290)

btnm = Button(frame1,text='Modificar',bg="red",font=("Arial Bold", 15), command=clickedm)
btnm.configure(height = 2,width = 10)


btnu = Button(frame1,text='Usar',bg="blue",font=("Arial Bold", 15), command=clickedu)
btnu.configure(height = 2,width = 10)


if N_Proyectos()>1 and VANDERA:
    btnm.place(x=340, y=230)
    btnu.place(x=340, y=170)
    VANDER = False
    
#else 
"""Frame Crear"""

frame2 = Frame(window) 
frame2.config(width=800,height=600) 

def dato_delet_crear():
    txt_name.delete(0,END)
    txt_ej_ex.delete(0,END)
    txt_n_inputs.delete(0,END)
    txt_i_inputs.delete(0,END)
    txt_e_inputs.delete(0,END)
    txt_outputs.delete(0,END)
    txt_data.delete(0,END)
    txt_n_neu.delete(0,END)
    txt_n_iter.delete(0,END)
    
def clickedcr():
    frame2.forget()
    frame1.pack()
    dato_delet_crear()

    
def clickedcl():
    X,Y=crear_txt(txt_name.get(),txt_ej_ex.get(),int(txt_n_inputs.get()),int(txt_i_inputs.get()),int(txt_e_inputs.get()),int(txt_outputs.get()),int(txt_data.get()),int(txt_n_neu.get()),int(txt_n_iter.get()))
    crear_sistema_inteligente(txt_name.get(),int(txt_n_inputs.get()),int(txt_n_neu.get()),int(txt_n_iter.get()),X,Y)
    if N_Proyectos()>1 and VANDERA:
        btnm.place(x=340, y=230)
        btnu.place(x=340, y=170)
        VANDER = False
    combo_m['values']= tuple(Proyectos())
    combo['values']=tuple(Proyectos())

lbl_name = Label(frame2, text="Ingrese nuevo nombre ")
lbl_name.place(x=5, y=0)

txt_name = Entry(frame2,width=75)
txt_name.place(x=8, y=25)

lbl_ej_ex = Label(frame2, text="Ingrese la ubicación del archivo. Ejemplo: C:/Users/tu_archivo.xlsx")
lbl_ej_ex.place(x=5, y=50)

txt_ej_ex = Entry(frame2,width=75)
txt_ej_ex.place(x=8, y=75)

lbl_n_inputs = Label(frame2, text="Cantidad de \n variables(entradas)")
lbl_n_inputs.place(x=5, y=105)

txt_n_inputs = Entry(frame2,width=10)
txt_n_inputs.place(x=8, y=140)

lbl_i_inputs = Label(frame2, text="Inicio de\n entradas(numero)")
lbl_i_inputs.place(x=155, y=105)

txt_i_inputs = Entry(frame2,width=10)
txt_i_inputs.place(x=158, y=140)

lbl_e_inputs = Label(frame2, text="Fin de\n entradas(numero)")
lbl_e_inputs.place(x=295, y=105)

txt_e_inputs = Entry(frame2,width=10)
txt_e_inputs.place(x=298, y=140)

lbl_outputs = Label(frame2, text="Posición \n de resultados")
lbl_outputs.place(x=445, y=105)

txt_outputs = Entry(frame2,width=10)
txt_outputs.place(x=448, y=140)

lbl_data = Label(frame2, text="Numero de \n casos(filas)")
lbl_data.place(x=555, y=105)

txt_data = Entry(frame2,width=10)
txt_data.place(x=558, y=140)

lbl_n_neu = Label(frame2, text="Número de neuronas")
lbl_n_neu.place(x=5, y=165)

txt_n_neu = Entry(frame2,width=10)
txt_n_neu.place(x=8, y=190)

lbl_n_iter = Label(frame2, text="Número de iteraciones ")
lbl_n_iter.place(x=155, y=165)

txt_n_iter = Entry(frame2,width=10)
txt_n_iter.place(x=158, y=190)

btncl = Button(frame2,text='Crear',bg="lightgreen",font=("Arial Bold", 12), command=clickedcl)
btncl.configure(height = 2,width = 10)
btncl.place(x=390, y=390)

btncr = Button(frame2,text='Regresar',bg="red",font=("Arial Bold", 12), command=clickedcr)
btncr.configure(height = 2,width = 10)
btncr.place(x=290, y=390)

"""Frame usar"""

frame3 = Frame(window) 
frame3.config(width=800,height=600) 

def clickedul():
    X = p_calcular(combo.get(),txt_ej_ex_u.get(),int(txt_data_u.get()))
    Y = usar_ia(X,combo.get())
    p_g_Y(combo.get(),txt_ej_ex_u.get(),int(txt_data_u.get()),Y)
    
def clickedur():
    frame3.forget()
    frame1.pack()
    txt_ej_ex_u.delete(0,END)
    txt_data_u.delete(0,END)
    combo.set("")
    btnc.focus()
    
combo = ttk.Combobox(frame3,width = 129,state = 'readonly')
combo['values']=tuple(Proyectos())
combo.place(x=0, y=0)

lbl_ej_ex_u = Label(frame3, text="Ingrese la ubicación del archivo. Ejemplo: C:/Users/tu_archivo.xlsx")
lbl_ej_ex_u.place(x=5, y=50)

txt_ej_ex_u = Entry(frame3,width=75)
txt_ej_ex_u.place(x=8, y=75)

lbl_data_u = Label(frame3, text="Numero de casos(filas)")
lbl_data_u.place(x=5, y=100)

txt_data_u = Entry(frame3,width=10)
txt_data_u.place(x=8, y=125)

btnul = Button(frame3,text='Calcular',bg="lightgreen",font=("Arial Bold", 12), command=clickedul)
btnul.configure(height = 2,width = 10)
btnul.place(x=390, y=390)

btnur = Button(frame3,text='Regresar',bg="red",font=("Arial Bold", 12), command=clickedur)
btnur.configure(height = 2,width = 10)
btnur.place(x=290, y=390)



"""Frame Modificar"""

frame4 = Frame(window) 
frame4.config(width=800,height=600) 

def clickedml():
    if chk_state:
        elimina_hoja(combo_m.get())
    else:
        elimina_hoja(combo_m.get())
        X,Y=crear_txt(txt_name.get(),txt_ej_ex.get(),int(txt_n_inputs.get()),int(txt_i_inputs.get()),int(txt_e_inputs.get()),int(txt_outputs.get()),int(txt_data.get()),int(txt_n_neu.get()),int(txt_n_iter.get()))
        crear_sistema_inteligente(txt_name.get(),int(txt_n_inputs.get()),int(txt_n_neu.get()),int(txt_n_iter.get()),X,Y)
    if N_Proyectos()<1:
        btnm.forget()
        btnu.forget()
        VANDER = True
    combo_m['values']= tuple(Proyectos())
    combo['values']=tuple(Proyectos())

def clickedmca():
    datalo = retornar_datos(combo_m.get())
    txt_name_m.insert(0,datalo[0])
    txt_m_ex.insert(0,datalo[1])
    txt_n_inputs_m.insert(0,datalo[2])
    txt_i_inputs_m.insert(0,datalo[3])
    txt_e_inputs_m.insert(0,datalo[4])
    txt_outputs_m.insert(0,datalo[5])
    txt_data_m.insert(0,datalo[6])
    txt_n_neu_m.insert(0,datalo[7])
    txt_n_iter_m.insert(0,datalo[8])
    
def clickedmr():
    frame4.forget()
    frame1.pack()
    txt_name_m.delete(0,END)
    txt_m_ex.delete(0,END)
    txt_n_inputs_m.delete(0,END)
    txt_i_inputs_m.delete(0,END)
    txt_e_inputs_m.delete(0,END)
    txt_outputs_m.delete(0,END)
    txt_data_m.delete(0,END)
    txt_n_neu_m.delete(0,END)
    txt_n_iter_m.delete(0,END)
    combo_m.set("")
    chk_state.set(False)
    btnc.focus()
    
combo_m = ttk.Combobox(frame4,width = 129,state = 'readonly')
combo_m['values']= tuple(Proyectos())
combo_m.place(x=0, y=0)

lbl_name_m = Label(frame4, text="Ingrese nuevo nombre ")
lbl_name_m.place(x=5, y=50)

txt_name_m = Entry(frame4,width=75)
txt_name_m.place(x=8, y=75)

lbl_m_ex = Label(frame4, text="Ingrese la ubicación del archivo. Ejemplo: C:/Users/tu_archivo.xlsx")
lbl_m_ex.place(x=5, y=105)

txt_m_ex = Entry(frame4,width=75)
txt_m_ex.place(x=8, y=140)


lbl_n_inputs_m = Label(frame4, text="Cantidad de \n variables(entradas)")
lbl_n_inputs_m.place(x=5, y=165)

txt_n_inputs_m = Entry(frame4,width=10)
txt_n_inputs_m.place(x=8, y=200)

lbl_i_inputs_m = Label(frame4, text="Inicio de\n entradas(numero)")
lbl_i_inputs_m.place(x=155, y=165)

txt_i_inputs_m = Entry(frame4,width=10)
txt_i_inputs_m.place(x=158, y=200)

lbl_e_inputs_m = Label(frame4, text="Fin de\n entradas(numero)")
lbl_e_inputs_m.place(x=295, y=165)

txt_e_inputs_m = Entry(frame4,width=10)
txt_e_inputs_m.place(x=298, y=200)

lbl_outputs_m = Label(frame4, text="Posición \n de resultados")
lbl_outputs_m.place(x=445, y=165)

txt_outputs_m = Entry(frame4,width=10)
txt_outputs_m.place(x=448, y=200)

lbl_data_m = Label(frame4, text="Numero de \n casos(filas)")
lbl_data_m.place(x=555, y=165)

txt_data_m = Entry(frame4,width=10)
txt_data_m.place(x=558, y=200)

lbl_n_neu_m = Label(frame4, text="Número de neuronas")
lbl_n_neu_m.place(x=5, y=225)

txt_n_neu_m = Entry(frame4,width=10)
txt_n_neu_m.place(x=8, y=250)

lbl_n_iter_m = Label(frame4, text="Número de iteraciones ")
lbl_n_iter_m.place(x=155, y=225)

txt_n_iter_m = Entry(frame4,width=10)
txt_n_iter_m.place(x=158, y=250)

chk_state = BooleanVar()
chk_state.set(False)

elim = Checkbutton(frame4, text="Eliminar", var=chk_state)
elim.place(x=8, y=275)

btnml = Button(frame4,text='Modificar',bg="lightgreen",font=("Arial Bold", 12), command=clickedml)
btnml.configure(height = 2,width = 10)
btnml.place(x=390, y=390)

btnmca = Button(frame4,text='Cargar',bg="yellow",font=("Arial Bold", 12), command=clickedmca)
btnmca.configure(height = 2,width = 10)
btnmca.place(x=290, y=390)

btnmr = Button(frame4,text='Regresar',bg="red",font=("Arial Bold", 12), command=clickedmr)
btnmr.configure(height = 2,width = 10)
btnmr.place(x=345, y=440)




"""Fin de Frame"""
window.resizable(width=False, height=False)
window.mainloop()
import matplotlib.pyplot as plt
import numpy as np
from tkinter import ttk
from tkinter import *
import tkinter as tk
def g(a,a1,b,b1,e):
  if e =='ec' or e =='ex':   
    foco=(a*a1)/(a+a1)
  else:
    foco=(a*(-a1))/(a-a1)
  e1=[0,0]
  e2=np.linspace(0,max(abs(b),abs(b1)),2)
  e3=[0,0]
  e4=np.linspace(0,-(max(abs(b),abs(b1))),2)
  x=[a,a]
  y=[0,b]
  x1=[a1,a1]
  y1=[0,b1]
  plt.annotate('F',(foco,0),(foco,-0.15),horizontalalignment='right', verticalalignment='top')
  plt.annotate('F´',(-foco,0),(-foco,-0.15),horizontalalignment='right', verticalalignment='top')
  plt.annotate(str(e), (0,max(abs(b),abs(b1))),horizontalalignment='right', verticalalignment='top')
  plt.xlabel(("El vértice se encuentra en la coordenada (0,0)"))
  plt.ylabel(("Altura"))
  plt.title(("Espejos y Lentes"))
  plt.plot(x,y,label='Pre-imagen',linewidth=3)
  plt.plot(x1,y1,label='Imagen',linewidth=3)
  plt.plot(e1,(e2),c='black')
  plt.plot(e3,(e4),c='black')
  if e=='ec':
    rayo1_1x=[a,0,0,foco]
    rayo1_1y=[b,b,b,0]
    rayo1_2x=[0,a1]
    rayo1_2y=[b,b1]
    plt.plot(rayo1_1x,rayo1_1y,color='red',label='Rayo 1')
    plt.plot(rayo1_2x,rayo1_2y,linestyle="--",color='red')
    rayo2_1x=[a,0,0,a]
    rayo2_1y=[b,0,0,-b]
    rayo2_2x=[0,a1]
    rayo2_2y=[0,b1]
    plt.plot(rayo2_1x,rayo2_1y,color='green',label='Rayo 2')
    plt.plot(rayo2_2x,rayo2_2y,linestyle="--",color='green')
  elif e=='ex':
    rayo1_1x=[a,2*foco]
    rayo1_1y=[b,0]
    plt.annotate('C',(2*foco,0),(2*foco,-0.15),horizontalalignment='right', verticalalignment='top')
    plt.plot(rayo1_1x,rayo1_1y,color='red',linestyle='--',label='Colinealidad')
    rayo2_1x=[a,0,0,a]
    rayo2_1y=[b,0,0,-b]
    rayo2_2x=[0,a1]
    rayo2_2y=[0,b1]
    plt.plot(rayo2_1x,rayo2_1y,color='green',label='Rayo 2')
    plt.plot(rayo2_2x,rayo2_2y,linestyle="--",color='green')
  elif e=='lc':
    rayo1_1x=[a,0,0,-foco]
    rayo1_1y=[b,b,b,0]
    rayo1_2x=[0,a1]
    rayo1_2y=[b,b1]
    plt.plot(rayo1_1x,rayo1_1y,color='red',label='Rayo 1')
    plt.plot(rayo1_2x,rayo1_2y,linestyle="--",color='red')
    rayo2_1x=[a,0,0,-a]
    rayo2_1y=[b,0,0,-b]
    rayo2_2x=[0,a1]
    rayo2_2y=[0,b1]
    plt.plot(rayo2_1x,rayo2_1y,color='green',label='Rayo 2')
    plt.plot(rayo2_2x,rayo2_2y,linestyle="--",color='green')
  elif e=='ld':
    rayo1_1x=[a,0,0,-a]
    rayo1_1y=[b,b1,b1,b1]
    rayo1_2x=[0,a1]
    rayo1_2y=[b1,b1]
    rayo1_3x=[0,foco]
    rayo1_3y=[b1,0]
    plt.plot(rayo1_1x,rayo1_1y,color='red',label='Rayo 1')
    plt.plot(rayo1_2x,rayo1_2y,linestyle="--",color='red')
    plt.plot(rayo1_3x,rayo1_3y,linestyle="-.",color='red')
    rayo2_1x=[a,0,0,-a]
    rayo2_1y=[b,0,0,-b]
    rayo2_2x=[0,a1]
    rayo2_2y=[0,b1]
    plt.plot(rayo2_1x,rayo2_1y,color='green',label='Rayo 2')
    plt.plot(rayo2_2x,rayo2_2y,linestyle="--",color='green')
  plt.legend()  
  plt.grid()
  plt.show()
  
def funcion(f,Do,Di,To,Ti,e):
  if e == 'ld' or e == 'ex':
    result_1=-(abs((Do*Di)/(Do+Di)))
  else:
    result_1=abs((Do*Di)/(Do+Di))
  result_2=abs((f*Di)/(Di-(f)))
  result_3=(f*Do)/(Do-(f))
  result_4=abs((Do*Ti*(-1))/(Di))
  result_5=(Di*To*(-1))/(Do)
  if (f-0.0001<result_1<f+0.0001) and (Do-0.0001<result_2<Do+0.0001) and (Di-0.0001<result_3<Di+0.0001) and (To-0.0001<result_4<To+0.0001) and (Ti-0.0001<result_5<Ti+0.0001):
    return f,Do,Di,To,Ti
  else:
    return result_1,result_2,result_3,result_4,result_5

def funcion_1(f,Do,Di,To,Ti):
  result_1=(Do*Di)/(Do+Di)
  return result_1

def funcion_2(f,Do,Di,To,Ti):
  result_2=(f*Di)/(Di-f)
  return result_2

def funcion_3(f,Do,Di,To,Ti):
  result_3=(f*Do)/(Do-f)
  return result_3

def funcion_4(f,Do,Di,To,Ti):
  result_4=(Do*Ti*-1)/(Di)
  return result_4

def funcion_5(f,Do,Di,To,Ti):
  result_5=(Di*To*-1)/(Do)
  return result_5

def funcion_6(f,Do,Di,To,Ti):
  result_6=f*(Ti-To)/(Ti)
  return result_6

def funcion_7(f,Do,Di,To,Ti):
  result_7=f*(To-Ti)/(To)
  return result_7

def funcion_8(f,Do,Di,To,Ti):
  result_8=(Do*Ti*-1)/(To)
  return result_8

def funcion_9(f,Do,Di,To,Ti):
  result_9=(Di*To*-1)/(Ti)
  return result_9

class EYL(ttk.Frame):
  def __init__(self,window):
               
                self.main = window
                self.main.configure(bg='#1c1c1c')
                self.main.resizable(0,0)
                self.main.title("ESPEJOS Y LENTES")
                self.logo=PhotoImage(file="logo.png")
                Label(self.main, image=self.logo, bg='#1c1c1c').grid(row=14,column=0,pady=10,padx=80,sticky=W+E)
                self.hispano=PhotoImage(file="hispano.png")
                Label(self.main, image=self.hispano, bg='#1c1c1c').grid(row=14,pady=10,column=1)
                Label(self.main, text='Digita los datos que tienes (en cm):',font=('Times',25),fg='white', bg='#1c1c1c').grid(row=0,columnspan=2,pady=20)
                Label(self.main, text='Nota: Si escoges EC o LC, el foco será tomado como positivo. Si tomas EX o LD, el foco ',font=('Times',15),fg='white', bg='#1c1c1c').grid(row=1,columnspan=2,pady=2)
                Label(self.main,text='y la distancia final serán tomadas negativas, y la altura final será tomada positiva.',font=('Times',15),fg='white', bg='#1c1c1c').grid(row=2,columnspan=2,pady=2)
                Label(self.main, text = 'Espejo o Lente: ',bg='#1c1c1c',fg='white', font=('Times',20)).grid(row=3, column=0,sticky=W+E,pady=10)
                self.combo=ttk.Combobox(self.main)
                self.combo.grid(row=3,column=1)
                self.combo['state'] = 'readonly'
                self.combo["values"]=['Espejo plano', 'Espejo cóncavo', 'Espejo convexo', 'Lente convergente','Lente divergente']
                Label(self.main, text='F:',fg='white', bg='#1c1c1c',font=('Times',20)).grid(row=4,column=0,padx=40)
                Label(self.main, text='Do:',fg='white', bg='#1c1c1c',font=('Times',20)).grid(row=5,column=0,padx=40)
                Label(self.main, text='Di:',fg='white', bg='#1c1c1c',font=('Times',20)).grid(row=6,column=0,padx=40)
                Label(self.main, text='To:',fg='white', bg='#1c1c1c',font=('Times',20)).grid(row=7,column=0,padx=40)
                Label(self.main, text='Ti:',fg='white', bg='#1c1c1c',font=('Times',20)).grid(row=8,column=0,padx=40)
                self.f_entry=Entry(self.main, bg='#D0D3D4', fg='black', highlightbackground='#1c1c1c')
                self.f_entry.grid(row=4,column=1,padx=40)
                self.Do_entry=Entry(self.main, bg='#D0D3D4', fg='black', highlightbackground='#1c1c1c')
                self.Do_entry.grid(row=5,column=1,padx=40)
                self.Di_entry=Entry(self.main, bg='#D0D3D4', fg='black', highlightbackground='#1c1c1c')
                self.Di_entry.grid(row=6,column=1,padx=40)
                self.To_entry=Entry(self.main, bg='#D0D3D4', fg='black', highlightbackground='#1c1c1c')
                self.To_entry.grid(row=7,column=1,padx=40)
                self.Ti_entry=Entry(self.main, bg='#D0D3D4', fg='black', highlightbackground='#1c1c1c')
                self.Ti_entry.grid(row=8,column=1,padx=40)
                self.message1=Label(self.main,text='',fg='white', bg='#1c1c1c')
                self.message1.grid(row=10,column=0,columnspan=2,sticky=W+E)
                self.message2=Label(self.main,text='',fg='white', bg='#1c1c1c')
                self.message2.grid(row=11,column=0,columnspan=2,sticky=W+E)
                self.message3=Label(self.main,text='',fg='white', bg='#1c1c1c')
                self.message3.grid(row=12,column=0,columnspan=2,sticky=W+E)
                Procesar=Button(self.main,font=('Times',15),text='             Procesar            ',command=self.procesar).grid(row=9,column=1,padx=10,pady=5,sticky=W+E)
                Borrar=Button(self.main,font=('Times',15),text='             Borrar            ',command=self.borrar).grid(row=9,column=0,padx=10,pady=5,sticky=W+E)
  def borrar (self):
    self.message1['text']=''
    self.message2['text']=''
    self.message3['text']=''
    self.f_entry.delete(0,END)
    self.Do_entry.delete(0,END)
    self.Di_entry.delete(0,END)
    self.To_entry.delete(0,END)
    self.Ti_entry.delete(0,END)
  def procesar(self):
    self.message1['text']=''
    self.message2['text']=''
    self.message3['text']=''
    try:
          e=self.combo.get()
          if e=='Espejo plano':
            e='ep'
          elif e=='Espejo cóncavo':
            e='ec'
          elif e=='Espejo convexo':
            e='ex'
          elif e=='Lente convergente':
            e='lc'
          elif e=='Lente divergente':
            e='ld'
          if self.f_entry.get()=='':
            f=0
          else:
            f=float(self.f_entry.get())
          if self.f_entry.get()=='':
            f=0
          else:
            f=float(self.f_entry.get())
          if self.Do_entry.get()=='':
            Do=0
          else:
            Do=float(self.Do_entry.get())
          if self.Di_entry.get()=='':
            Di=0
          else:
            Di=float(self.Di_entry.get())
          if self.To_entry.get()=='':
            To=0
          else:
            To=float(self.To_entry.get())
          if self.Ti_entry.get()=='':
            Ti=0
          else:
            Ti=float(self.Ti_entry.get())
          
          if e==("ep"):
            self.f_entry.delete(0,END)
            self.Do_entry.delete(0,END)
            self.Di_entry.delete(0,END)
            self.To_entry.delete(0,END)
            self.Ti_entry.delete(0,END)
            self.message1['text']="La distancia inicial es igual a la final (la final tiene signo negativo), y lo mismo ocurre para las alturas. La imagen es derecha y virtual"
          elif e==("ec")  or e==("lc"):
              f=abs(f)
              To=abs(To)
              Do=abs(Do)
              if f==Do and f!=0 and Do!=0: self.message1['text']="La imagen está en el infinito, no está definido ni Di ni Ti"
              if (f!=0 and f!=Do):
                if (Do and Di and To and Ti)!=0:             
                  result=funcion(f,Do,Di,To,Ti,e)
                  if result!=(f,Do,Di,To,Ti):
                   self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                   
                  else:
                    self.message1['text']="Ya tiene todos los valores"
                    self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do) +"," +str(Di) +"," +str(To) +"," +str(Ti)
                    if e==("ec"):
                      g(Do,Di,To,Ti,e)
                    else:
                      g(Do,-Di,To,Ti,e)   
                else:
                  if (Do and Di and To)!=0:
                   Ti1=funcion_5(f,Do,Di,To,Ti)
                   result=funcion(f,Do,Di,To,Ti1,e)
                   if result!=(f,Do,Di,To,Ti1):
                    self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                    
                   else:
                     self.message1['text']="El valor de la altura final es:" +str (Ti1)
                     self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do) +"," +str(Di) +"," +str(To) +"," +str(Ti1)
                     if e==("ec"):
                      g(Do,Di,To,Ti1,e)
                     else:
                      g(Do,-Di,To,Ti1,e) 
                  else:
                     if (Do and Di and Ti)!=0:
                       To1=funcion_4(f,Do,Di,To,Ti)
                       result=funcion(f,Do,Di,To1,Ti,e)
                       if result!=(f,Do,Di,To1,Ti):
                        self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                        
                       else:
                         self.message1['text']="El valor de la altura inicial es:" +str (To1)
                         self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do) +"," +str(Di) +"," +str(To1) +"," +str(Ti)
                         if e==("ec"):
                          g(Do,Di,To1,Ti,e)
                         else:
                          g(Do,-Di,To1,Ti,e)
                     else:
                       if (Do and Ti and To)!=0:
                         Di1=funcion_3(f,Do,Di,To,Ti)
                         result=funcion(f,Do,Di1,To,Ti,e)
                         if result!=(f,Do,Di1,To,Ti):
                          self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                          
                         else:
                           self.message1['text']="El valor de la distancia final es:" +str (Di1)
                           self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do) +"," +str(Di1) +"," +str(To) +"," +str(Ti)
                           if e==("ec"):
                              g(Do,Di1,To,Ti,e)
                           else:
                              g(Do,-Di1,To,Ti,e) 
                       else:
                         if (Di and Ti and To)!=0:
                           Do1=funcion_2(f,Do,Di,To,Ti)
                           result=funcion(f,Do1,Di,To,Ti,e)
                           if result!=(f,Do1,Di,To,Ti):
                             self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                            
                           else:
                             self.message1['text']="El valor de la distancia inicial es:" +str (Do1)
                             self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do1) +"," +str(Di) +"," +str(To) +"," +str(Ti)
                             if e==("ec"):
                                g(Do1,Di,To,Ti,e)
                             else:
                                g(Do1,-Di,To,Ti,e) 
                         else:
                           if (Do and To)!=0:
                             Di1=funcion_3(f,Do,Di,To,Ti)
                             Ti1=funcion_5(f,Do,Di1,To,Ti)
                             result=funcion(f,Do,Di1,To,Ti1,e)
                             if result!=(f,Do,Di1,To,Ti1):
                              self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                             
                             else:
                               self.message1['text']="El valor de la altura  y distancia finales es:" +str (Ti1) +" y " +str(Di1)
                               self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do) +"," +str(Di1) +"," +str(To) +"," +str(Ti1)
                               if e==("ec"):
                                  g(Do,Di1,To,Ti1,e)
                               else:
                                  g(Do,-Di1,To,Ti1,e) 
                           else:
                             if (Do and Ti)!=0:
                               Di1=funcion_3(f,Do,Di,To,Ti)
                               To1=funcion_4(f,Do,Di1,To,Ti)
                               result=funcion(f,Do,Di1,To1,Ti,e)
                               if result!=(f,Do,Di1,To1,Ti):
                                self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                                
                               else:
                                 self.message1['text']="El valor de la altura inicial y distancia final es:" +str (To1) +" y " +str(Di1)
                                 self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do) +"," +str(Di1) +"," +str(To1) +"," +str(Ti)
                                 if e==("ec"):
                                    g(Do,Di1,To1,Ti,e)
                                 else:
                                    g(Do,-Di1,To1,Ti,e) 
                             else:
                               if (Di and To)!=0:
                                 Do1=funcion_2(f,Do,Di,To,Ti)
                                 Ti1=funcion_5(f,Do1,Di,To,Ti)
                                 result=funcion(f,Do1,Di,To,Ti1,e)
                                 if result!=(f,Do1,Di,To,Ti1):
                                  self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                                  
                                 else:
                                   self.message1['text']="El valor de la altura final y distancia inicial es:" +str (Ti1) +" y " +str(Do1)
                                   self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do1) +"," +str(Di) +"," +str(To) +"," +str(Ti1)
                                   if e==("ec"):
                                      g(Do1,Di,To,Ti1,e)
                                   else:
                                      g(Do1,-Di,To,Ti1,e) 
                               else:
                                 if (Di and Ti)!=0:
                                   Do1=funcion_2(f,Do,Di,To,Ti)
                                   To1=funcion_4(f,Do1,Di,To,Ti)
                                   result=funcion(f,Do1,Di,To1,Ti,e)
                                   if result!=(f,Do1,Di,To1,Ti):
                                    self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                                   else:
                                     self.message1['text']="El valor de la altura  y distancia iniciales es:" +str (To1) +" y " +str(Do1)
                                     self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do1) +"," +str(Di) +"," +str(To1) +"," +str(Ti)
                                     if e==("ec"):
                                        g(Do1,Di,To1,Ti,e)
                                     else:
                                        g(Do1,-Di,To1,Ti,e) 
                                 else:
                                   if (To and Ti)!=0:
                                     Do1=funcion_6(f,Do,Di,To,Ti)
                                     Di1=funcion_7(f,Do1,Di,To,Ti)
                                     result=funcion(f,Do1,Di1,To,Ti,e)
                                     if result!=(f,Do1,Di1,To,Ti):
                                      self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                                      
                                     else:
                                       self.message1['text']="El valor de la distancia inicial y final es:" +str (Do1) +" y " +str(Di1)
                                       self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do1) +"," +str(Di1) +"," +str(To) +"," +str(Ti)
                                       if e==("ec"):
                                          g(Do1,Di1,To,Ti,e)
                                       else:
                                          g(Do1,-Di1,To,Ti,e) 
                                   else: self.message1['text']="Falta información."
                try:
                  if (Ti1)<0 and (Di1)<0:
                   self.message3['text']="La imagen es invertida y virtual."
                  elif (Ti1)<0 and (Di1)>0:
                   self.message3['text']="La imagen es invertida y real."
                  elif (Ti1)>0 and (Di1)<0:
                   self.message3['text']="La imagen es Derecha y virtual."
                  elif (Ti1)>0 and (Di1)>0:
                   self.message3['text']="La imagen es Derecha y real."
                except:
                  try:
                       if (Ti)<0 and (Di1)<0:
                           self.message3['text']="La imagen es invertida y virtual."
                       elif (Ti)<0 and (Di1)>0:
                           self.message3['text']="La imagen es invertida y real."
                       elif (Ti)>0 and (Di1)<0:
                           self.message3['text']="La imagen es Derecha y virtual."
                       elif (Ti)>0 and (Di1)>0:
                           self.message3['text']="La imagen es Derecha y real."
                  except:
                            try:
                              if (Ti1)<0 and (Di)<0:
                                   self.message3['text']="La imagen es invertida y virtual."
                              elif (Ti1)<0 and (Di)>0:
                                   self.message3['text']="La imagen es invertida y real."
                              elif (Ti1)>0 and (Di)<0:
                                   self.message3['text']="La imagen es Derecha y virtual."
                              else :
                                   self.message3['text']="La imagen es Derecha y real."
                            except:
                              try:
                                  if (Ti)<0 and (Di)<0:
                                       self.message3['text']="La imagen es invertida y virtual."
                                  elif (Ti)<0 and (Di)>0:
                                       self.message3['text']="La imagen es invertida y real."
                                  elif (Ti)>0 and (Di)<0:
                                       self.message3['text']="La imagen es Derecha y virtual."
                                  else:
                                       self.message3['text']="La imagen es Derecha y real."
                              except:
                                self.message3['text']=""
              if f==0:
                if (Do and Di and To and Ti)!=0:
                  f0=funcion_1(f,Do,Di,To,Ti)
                  result=funcion(f0,Do,Di,To,Ti,e)
                  if f0==Do:
                    self.message1['text']="La imagen está en el infinito, no está definido ni Di ni Ti"
                  elif result!=(f0,Do,Di,To,Ti):
                   self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                   
                  else:
                    self.message1['text']="El foco es:" +str(f0)
                    self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f0) +"," +str(Do) +"," +str(Di) +"," +str(To) +"," +str(Ti)
                    if e==("ec"):
                      g(Do,Di,To,Ti,e)
                    else:
                      g(Do,-Di,To,Ti,e) 
                else:
                  if (Do and Di and To)!=0:
                   f0=funcion_1(f,Do,Di,To,Ti)
                   Ti1=funcion_5(f,Do,Di,To,Ti)
                   result=funcion(f0,Do,Di,To,Ti1,e)
                   if f0==Do:
                    self.message1['text']="La imagen está en el infinito, no está definido ni Di ni Ti"
                   elif result!=(f0,Do,Di,To,Ti1):
                    self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                    
                   else:
                     self.message1['text']="El valor de la altura final y el foco es:" +str (Ti1) +" y " +str(f0)
                     self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f0) +"," +str(Do) +"," +str(Di) +"," +str(To) +"," +str(Ti1)
                     if e==("ec"):
                      g(Do,Di,To,Ti1,e)
                     else:
                      g(Do,-Di,To,Ti1,e) 
                  else:
                     if (Do and Di and Ti)!=0:
                       f0=funcion_1(f,Do,Di,To,Ti)
                       To1=funcion_4(f,Do,Di,To,Ti)
                       result=funcion(f0,Do,Di,To1,Ti,e)
                       if f0==Do:
                         self.message1['text']="La imagen está en el infinito, no está definido ni Di ni Ti"
                       elif result!=(f0,Do,Di,To1,Ti):
                        self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                        
                       else:
                         self.message1['text']="El valor de la altura inicial y el foco es:" +str (To1) +" y " +str(f0)
                         self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f0) +"," +str(Do) +"," +str(Di) +"," +str(To1) +"," +str(Ti)
                         if e==("ec"):
                            g(Do,Di,To1,Ti,e)
                         else:
                            g(Do,-Di,To1,Ti,e) 
                     else:
                       if (Do and Ti and To)!=0:
                         Di1=funcion_8(f,Do,Di,To,Ti)
                         f0=funcion_1(f,Do,Di1,To,Ti)
                         result=funcion(f0,Do,Di1,To,Ti,e)
                         
                         if f0==Do:
                            self.message1['text']="La imagen está en el infinito, no está definido ni Di ni Ti"
                         elif result!=(f0,Do,Di1,To,Ti):
                          self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                          
                         else:
                           self.message1['text']="El valor de la distancia final y el foco es:" +str (Di1) +" y " +str(f0)
                           self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f0) +"," +str(Do) +"," +str(Di1) +"," +str(To) +"," +str(Ti)
                           if e==("ec"):
                              g(Do,Di1,To,Ti,e)
                           else:
                              g(Do,-Di1,To,Ti,e) 
                       else:
                         if (Di and Ti and To)!=0:
                           Do1=funcion_9(f,Do,Di,To,Ti)
                           f0=funcion_1(f,Do1,Di,To,Ti)
                           result=funcion(f0,Do1,Di,To,Ti,e)
                           if f0==Do1:
                              self.message1['text']="La imagen está en el infinito, no está definido ni Di ni Ti"
                           elif result!=(f0,Do1,Di,To,Ti):
                            self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                            
                           else:
                             self.message1['text']="El valor de la distancia inicial y el foco es:" +str (Do1) +" y " +str(f0)
                             self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f0) +"," +str(Do1) +"," +str(Di) +"," +str(To) +"," +str(Ti)
                             if e==("ec"):
                                g(Do1,Di,To,Ti,e)
                             else:
                                g(Do1,-Di,To,Ti,e) 
                         else: self.message1['text']="Falta información"
                try:
                  if (Ti1)<0 and (Di1)<0:
                   self.message3['text']="La imagen es invertida y virtual."
                  elif (Ti1)<0 and (Di1)>0:
                   self.message3['text']="La imagen es invertida y real."
                  elif (Ti1)>0 and (Di1)<0:
                   self.message3['text']="La imagen es Derecha y virtual."
                  elif (Ti1)>0 and (Di1)>0:
                   self.message3['text']="La imagen es Derecha y real."
                except:
                  try:
                       if (Ti)<0 and (Di1)<0:
                           self.message3['text']="La imagen es invertida y virtual."
                       elif (Ti)<0 and (Di1)>0:
                           self.message3['text']="La imagen es invertida y real."
                       elif (Ti)>0 and (Di1)<0:
                           self.message3['text']="La imagen es Derecha y virtual."
                       elif (Ti)>0 and (Di1)>0:
                           self.message3['text']="La imagen es Derecha y real."
                  except:
                            try:
                              if (Ti1)<0 and (Di)<0:
                                   self.message3['text']="La imagen es invertida y virtual."
                              elif (Ti1)<0 and (Di)>0:
                                   self.message3['text']="La imagen es invertida y real."
                              elif (Ti1)>0 and (Di)<0:
                                   self.message3['text']="La imagen es Derecha y virtual."
                              elif (Ti1)>0 and (Di)>0:
                                   self.message3['text']="La imagen es Derecha y real."
                            except:
                              try:
                                  if (Ti)<0 and (Di)<0:
                                       self.message3['text']="La imagen es invertida y virtual."
                                  elif (Ti)<0 and (Di)>0:
                                       self.message3['text']="La imagen es invertida y real."
                                  elif (Ti)>0 and (Di)<0:
                                       self.message3['text']="La imagen es Derecha y virtual."
                                  elif (Ti)>0 and (Di)>0:
                                       self.message3['text']="La imagen es Derecha y real."
                              except:
                                self.message3['text']=""
          elif e==("ex") or e==("ld"):
              f=(-1)*abs(f)
              Di=(-1)*abs(Di)
              Ti=abs(Ti)
              To=abs(To)
              Do=abs(Do)
              if f==Do or f==(Do*-1): self.message1['text']="La imagen está en el infinito, no esta definidio ni Di ni Ti"
              if (f!=0 and f!=Do):
                if (Do and Di and To and Ti)!=0:
                  result=funcion(f,Do,Di,To,Ti,e)
                  if result!=(f,Do,Di,To,Ti):
                   self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                   
                  else:
                    self.message1['text']="Ya tiene todos los valores"
                    self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do) +"," +str(Di) +"," +str(To) +"," +str(Ti)
                    if e==("ex"):
                      g(Do,Di,To,Ti,e)
                    else:
                      g(Do,-Di,To,Ti,e) 
                else:
                  if (Do and Di and To)!=0:
                   Ti1=funcion_5(f,Do,Di,To,Ti)
                   result=funcion(f,Do,Di,To,Ti1,e)
                   if result!=(f,Do,Di,To,Ti1):
                    self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                   
                   else:
                     self.message1['text']="El valor de la altura final es:" +str (Ti1)
                     self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do) +"," +str(Di) +"," +str(To) +"," +str(Ti1)
                     if e==("ex"):
                      g(Do,Di,To,Ti1,e)
                     else:
                      g(Do,-Di,To,Ti1,e) 
                  else:
                     if (Do and Di and Ti)!=0:
                       To1=funcion_4(f,Do,Di,To,Ti)
                       result=funcion(f,Do,Di,To1,Ti,e)
                       if result!=(f,Do,Di,To1,Ti):
                        self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                        
                       else:
                         self.message1['text']="El valor de la altura inicial es:" +str (To1)
                         self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do) +"," +str(Di) +"," +str(To1) +"," +str(Ti)
                         if e==("ex"):
                          g(Do,Di,To1,Ti,e)
                         else:
                          g(Do,-Di,To1,Ti,e) 
                     else:
                       if (Do and Ti and To)!=0:
                         Di1=funcion_3(f,Do,Di,To,Ti)
                         result=funcion(f,Do,Di1,To,Ti,e)
                         if result!=(f,Do,Di1,To,Ti):
                          self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                          
                         else:
                           self.message1['text']="El valor de la distancia final es:" +str (Di1)
                           self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do) +"," +str(Di1) +"," +str(To) +"," +str(Ti)
                           if e==("ex"):
                            g(Do,Di1,To,Ti,e)
                           else:
                            g(Do,-Di1,To,Ti,e) 
                       else:
                         if (Di and Ti and To)!=0:
                           Do1=funcion_2(f,Do,Di,To,Ti)
                           result=funcion(f,Do1,Di,To,Ti,e)
                           if result!=(f,Do1,Di,To,Ti):
                            self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                           
                           else:
                             self.message1['text']="El valor de la distancia inicial es:" +str (Do1)
                             self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do1) +"," +str(Di) +"," +str(To) +"," +str(Ti)
                             if e==("ex"):
                              g(Do1,Di,To,Ti,e)
                             else:
                              g(Do1,-Di,To,Ti,e) 
                         else:
                           if (Do and To)!=0:
                             Di1=funcion_3(f,Do,Di,To,Ti)
                             Ti1=funcion_5(f,Do,Di1,To,Ti)
                             result=funcion(f,Do,Di1,To,Ti1,e)
                             if result!=(f,Do,Di1,To,Ti1):
                              self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                              
                             else:
                               self.message1['text']="El valor de la altura  y distancia finales es:" +str (Ti1) +" y " +str(Di1)
                               self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do) +"," +str(Di1) +"," +str(To) +"," +str(Ti1)
                               if e==("ex"):
                                g(Do,Di1,To,Ti1,e)
                               else:
                                g(Do,-Di1,To,Ti1,e) 
                           else:
                             if (Do and Ti)!=0:
                               Di1=funcion_3(f,Do,Di,To,Ti)
                               To1=funcion_4(f,Do,Di1,To,Ti)
                               result=funcion(f,Do,Di1,To1,Ti,e)
                               if result!=(f,Do,Di1,To1,Ti):
                                self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                                
                               else:
                                 self.message1['text']="El valor de la altura inicial y distancia final es:" +str (To1) +" y " +str(Di1)
                                 self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do) +"," +str(Di1) +"," +str(To1) +"," +str(Ti)
                                 if e==("ex"):
                                  g(Do,Di1,To1,Ti,e)
                                 else:
                                  g(Do,-Di1,To1,Ti,e) 
                             else:
                               if (Di and To)!=0:
                                 Do1=funcion_2(f,Do,Di,To,Ti)
                                 Ti1=funcion_5(f,Do1,Di,To,Ti)
                                 result=funcion(f,Do1,Di,To,Ti1,e)
                                 if result!=(f,Do1,Di,To,Ti1):
                                  self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                                 
                                 else:
                                   self.message1['text']="El valor de la altura final y distancia inicial es:" +str (Ti1) +" y " +str(Do1)
                                   self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do1) +"," +str(Di) +"," +str(To) +"," +str(Ti1)
                                   if e==("ex"):
                                    g(Do1,Di,To,Ti1,e)
                                   else:
                                    g(Do1,-Di,To,Ti1,e) 
                               else:
                                 if (Di and Ti)!=0:
                                   Do1=funcion_2(f,Do,Di,To,Ti)
                                   To1=funcion_4(f,Do1,Di,To,Ti)
                                   result=funcion(f,Do1,Di,To1,Ti,e)
                                   if result!=(f,Do1,Di,To1,Ti):
                                    self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                                  
                                   else:
                                     self.message1['text']="El valor de la altura  y distancia iniciales es:" +str (To1) +" y " +str(Do1)
                                     self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do1) +"," +str(Di) +"," +str(To1) +"," +str(Ti)
                                     if e==("ex"):
                                      g(Do1,Di,To1,Ti,e)
                                     else:
                                      g(Do1,-Di,To1,Ti,e) 
                                 else:
                                   if (To and Ti)!=0:
                                     Do1=funcion_6(f,Do,Di,To,Ti)
                                     Di1=funcion_7(f,Do1,Di,To,Ti)
                                     result=funcion(f,Do1,Di1,To,Ti,e)
                                     if result!=(f,Do1,Di1,To,Ti):
                                      self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                                     
                                     else:
                                       self.message1['text']="El valor de la distancia inicial y final es:" +str (Do1) +" y " +str(Di1)
                                       self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f) +"," +str(Do1) +"," +str(Di1) +"," +str(To) +"," +str(Ti)
                                       if e==("ex"):
                                        g(Do1,Di1,To,Ti,e)
                                       else:
                                        g(Do1,-Di1,To,Ti,e) 
                                   else: self.message1['text']="Falta información."
                self.message3['text']="La imagen es virtual y derecha"
              if f==0:
                if (Do and Di and To and Ti)!=0:
                  f0=funcion_1(f,Do,Di,To,Ti)
                  result=funcion(f0,Do,Di,To,Ti,e)
                  if result!=(f0,Do,Di,To,Ti):
                   self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                   
                  else:
                    self.message1['text']="El foco es:" +str(f0)
                    self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f0) +"," +str(Do) +"," +str(Di) +"," +str(To) +"," +str(Ti)
                    if e==("ex"):
                      g(Do,Di,To,Ti,e)
                    else:
                      g(Do,-Di,To,Ti,e) 
                else:
                  if (Do and Di and To)!=0:
                   f0=funcion_1(f,Do,Di,To,Ti)
                   Ti1=funcion_5(f,Do,Di,To,Ti)
                   result=funcion(f0,Do,Di,To,Ti1,e)
                   if result!=(f0,Do,Di,To,Ti1):
                    self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                   
                   else:
                     self.message1['text']="El valor de la altura final y el foco es:" +str (Ti1) +" y " +str(f0)
                     self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f0) +"," +str(Do) +"," +str(Di) +"," +str(To) +"," +str(Ti1)
                     if e==("ex"):
                      g(Do,Di,To,Ti1,e)
                     else:
                      g(Do,-Di,To,Ti1,e) 
                  else:
                     if (Do and Di and Ti)!=0:
                       f0=funcion_1(f,Do,Di,To,Ti)
                       To1=funcion_4(f,Do,Di,To,Ti)
                       result=funcion(f0,Do,Di,To1,Ti,e)
                       if result!=(f0,Do,Di,To1,Ti):
                        self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                       
                       else:
                         self.message1['text']="El valor de la altura inicial y el foco es:" +str (To1) +" y " +str(f0)
                         self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f0) +"," +str(Do) +"," +str(Di) +"," +str(To1) +"," +str(Ti)
                         if e==("ex"):
                          g(Do,Di,To1,Ti,e)
                         else:
                          g(Do,-Di,To1,Ti,e) 
                     else:
                       if (Do and Ti and To)!=0:
                         Di1=funcion_8(f,Do,Di,To,Ti)
                         f0=funcion_1(f,Do,Di1,To,Ti)
                         result=funcion(f0,Do,Di1,To,Ti,e)
                         if result!=(f0,Do,Di1,To,Ti):
                          self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                          
                         else:
                           self.message1['text']="El valor de la distancia final y el foco es:" +str (Di1) +" y " +str(f0)
                           self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f0) +"," +str(Do) +"," +str(Di1) +"," +str(To) +"," +str(Ti)
                           if e==("ex"):
                            g(Do,Di1,To,Ti,e)
                           else:
                            g(Do,-Di1,To,Ti,e) 
                       else:
                         if (Di and Ti and To)!=0:
                           Do1=funcion_9(f,Do,Di,To,Ti)
                           f0=funcion_1(f,Do1,Di,To,Ti)
                           result=funcion(f0,Do1,Di,To,Ti,e)
                           if result!=(f0,Do1,Di,To,Ti):
                            self.message1['text']="Los valores insertados no cuadran según las fórmulas establecidas."
                            
                           else:
                             self.message1['text']="El valor de la distancia inicial y el foco es:" +str (Do1) +" y " +str(f0)
                             self.message2['text']="Los valores del f,Do,Di,To y Ti son respectivamente:" +str(f0) +"," +str(Do1) +"," +str(Di) +"," +str(To) +"," +str(Ti)
                             if e==("ex"):
                              g(Do1,Di,To,Ti,e)
                             else:
                              g(Do1,-Di,To,Ti,e) 
                         else:
                           self.message1['text']="Falta información"
                self.message3['text']="La imagen es virtual y derecha"
          else:
             self.message1['text']="Escribe un espejo o lente válido"
    except:
      self.message1['text']="Inserta números reales en las variables o valores correctos para el espejo o lente"


if __name__=='__main__':
        window = tk.Tk()
        application = EYL(window)
        window.mainloop()

from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text="Male", variable=var1).grid(row=0, sticky= W)
var2= IntVar()
Checkbutton(master, text="Female", variable=var2).grid(row=1, sticky=W)
#sticky tem a mesma função do anchor
#Grid é utilizado para definir em linhas e colunas 
master.mainloop()
from tkinter import *
from tkinter.ttk import *
janela = Tk()
def funcao():
    barra['value'] = barra['value']+1
    etq['text']=barra['value'],"%"
janela.geometry('600x300')
etq = Label(janela, text="0%")
etq.pack()
barra = Progressbar(janela, length=500)
barra['value']=0
barra.pack()
btn = Button(janela, text='Avançar', command=funcao)
btn.pack()
janela.mainloop()
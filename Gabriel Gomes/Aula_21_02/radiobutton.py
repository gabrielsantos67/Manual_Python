#Usado quando se precisa selecionar apenas uma opção
from tkinter import *
janela = Tk()
def sel():
    selecionado = "Você selecionou a opção " + str(var.get())
    etq1["text"] = selecionado
janela.title('Atividade')
janela.iconbitmap('kk.ico')
janela.geometry('500x400+150+100')
var = IntVar()
rb1 = Radiobutton(janela, text='Opção 1', variable=var, value=1, fg='Magenta')
rb1.pack()
rb2 = Radiobutton(janela, text='Opção 2', variable=var, value=2, fg='Magenta')
rb2.pack()
rb3 = Radiobutton(janela, text='Opção 3', variable=var, value=3, fg='Magenta')
rb3.pack()
but = Button(janela, text='Selecionar', bg="Pink", fg="RED", command=sel)
but.pack()
etq1 = Label(janela, text='', padx=215)
etq1.pack()
janela.mainloop()
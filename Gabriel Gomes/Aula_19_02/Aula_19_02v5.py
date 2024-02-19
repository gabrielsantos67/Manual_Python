from tkinter import *
janela=Tk()
def selecao():
    etq1['text'] = lista.get(ANCHOR)
lista = Listbox(janela)
lista.pack()
minhalista = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais']
for item in minhalista:
    lista.insert(END, item)
janela.geometry('500x400+50+20')
btn1 = Button(janela, text='Selecionado', command=selecao)
btn1.pack()
etq1 = Label(janela, text='')
etq1.pack()
janela.mainloop()
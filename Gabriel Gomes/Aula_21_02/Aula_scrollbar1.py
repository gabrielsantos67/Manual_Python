from tkinter import *
janela=Tk()
def selecao():
    etq1['text'] ='Local é ' + lista.get(ANCHOR)

etq2 = Label(janela, text="Qual Estado você mora?")
etq2.pack()
#ScrollBar
frame = Frame(janela)
scrollbar = Scrollbar(frame, orient=VERTICAL)
lista=Listbox(frame,width=20, height=5, yscrollcommand=scrollbar.set)
scrollbar.config(command= lista.yview)
scrollbar.pack(side=RIGHT, fill=Y)
frame.pack()
lista.pack()
minhalista = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Alagoas', "Amazonas", "Roraima", 'Acre']
for item in minhalista:
    lista.insert(END, item)
janela.geometry('500x400+50+20')
btn1 = Button(janela, text='Selecionado', command=selecao)
btn1.pack()
etq1 = Label(janela, text='')
etq1.pack()
janela.mainloop()
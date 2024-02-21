from tkinter import*
janela = Tk()
def funcao():
    if var1.get()==1:
        etq1['text']= "Opção 1 selecionada"
    else:
        etq1['text']= ""
    if var2.get()==1:
        etq2['text']= "Opção 2 selecionada"
    else:
        etq2['text']= ""
janela.title('Atividade')
janela.iconbitmap('kk.ico')
janela.geometry('500x400+150+100')
var1 = IntVar()
Checkbutton(janela, text="Opção 1", variable=var1, padx=215, fg="RED").pack()
var2= IntVar()
Checkbutton(janela, text="Opção 2", variable=var2,padx=215,fg="RED").pack()
but = Button(janela, text='Selecionar', bg="Pink", fg="RED", command=funcao)
but.pack()
etq1 = Label(janela, text='', padx=215)
etq1.pack()
etq2 = Label(janela, text='')
etq2.pack()
janela.mainloop()
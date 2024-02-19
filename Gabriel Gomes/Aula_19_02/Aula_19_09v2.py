from tkinter import *
janela = Tk()
#Utilizamos o Grid() para alocar as caixas em colunas e linhas 
#Utilizamos o column para colunas e o row para as linhas
lbl1 = Label(janela, text='Login:')
lbl1.grid(column=0, row=0)
lbl2 = Label(janela, text='Senha:')
lbl2.grid(column=0, row=1)
en1 = Entry(janela)
en1.grid(column=1, row=0, padx= (10,10), pady= (10,10))
en2 = Entry(janela)
en2.grid(column=1, row=1,padx= (10,10), pady= (10,10))
btn1 = Button(janela, text='Avançar')
btn1.grid(column=0, row=2, columnspan= 2)
janela.mainloop()
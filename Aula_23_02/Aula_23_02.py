from tkinter import *
janela = Tk()
def selecao():
    if var.get() == 1:
        m = "Masculino"
    else:
        m= ""
    if var.get() == 2:
        f = "Feminino"
    else:
        f= ""
    if var1.get()==1:
        y = "Python"
    else:
        y = ""
    if var2.get()==1:
        z = "Java"
    else:
        z = ""
    if var3.get()==1:
        a = "SQL Server"
    else:
        a = ""
    nome = en1.get()
    lista1 = lista.get(ANCHOR)
    etq1['text'] = (f"{nome} o seu local de estudo é: {lista1}\n Seu sexo é: {m}{f}\n  E o curso escolhido foi: {y} {z} {a}")
janela.title('Atividade')
janela.iconbitmap('kk.ico')
janela.geometry('500x400+150+100')
lbl1 = Label(janela, text='Qual o seu Nome?')
lbl1.pack()
en1 = Entry(janela)
en1.pack()
lbl3 = Label(janela)
lbl3.pack()
lbl2 = Label(janela, text='Qual o Sexo?')
lbl2.pack()
#Radiobutton
var = IntVar()
rb1 = Radiobutton(janela, text='Masculino', variable=var, value=1, fg='Blue')
rb1.pack()
rb2 = Radiobutton(janela, text='Feminino', variable=var, value=2, fg='Magenta')
rb2.pack()
lbl4 = Label(janela)
lbl4.pack()
etq2 = Label(janela, text="Onde deseja cursar?")
etq2.pack()
#ScrollBar
frame = Frame(janela)
scrollbar = Scrollbar(frame, orient=VERTICAL)
lista=Listbox(frame,width=20, height=5, yscrollcommand=scrollbar.set)
scrollbar.config(command= lista.yview)
scrollbar.pack(side=RIGHT, fill=Y)
frame.pack()
lista.pack()
minhalista = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Alagoas', "Amazonas", "Roraima", 'Acre', '']
for item in minhalista:
    lista.insert(END, item)
janela.geometry('500x400+50+20')
lbl5 = Label(janela)
lbl5.pack()
etq3 = Label(janela, text='Qual curso você deseja?').pack()
var1 = IntVar()
Checkbutton(janela, text="Python", variable=var1).pack()
var2= IntVar()
Checkbutton(janela, text="Java", variable=var2).pack()
var3= IntVar()
Checkbutton(janela, text="SQL Server", variable=var3).pack()
lbl6 = Label(janela)
lbl6.pack()
btn1 = Button(janela, text='Selecionado', command=selecao)
btn1.pack()
lbl7 = Label(janela)
lbl7.pack()
etq1 = Label(janela, text='')
etq1.pack()
janela.mainloop()
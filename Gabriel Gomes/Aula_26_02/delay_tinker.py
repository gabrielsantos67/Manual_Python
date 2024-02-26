from tkinter import *
janela = Tk()
#Usamos o After para criar um delay, a função lê em milisegundos e após isso apresenta a mensagem
def delay():
    lbl1['text']= 'Aguarde...'
    janela.after(2000,mensagem)
def mensagem():
    lbl1['text']= 'Botão acionado!!'
btn1 = Button(janela,text='Aperte Aqui!',command=delay)
btn1.pack()
lbl2 = Label(janela,text='')
lbl2.pack()
lbl1 = Label(janela,text='')
lbl1.pack()
janela.title('Delay')
janela.iconbitmap('kk.ico')
janela.geometry('500x400+150+100')
janela.mainloop()
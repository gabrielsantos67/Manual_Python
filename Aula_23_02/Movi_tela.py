from tkinter import *
janela = Tk()
janela.title('Atividade')
janela.iconbitmap('kk.ico')
def esquerda(event):
    x=-10
    y=0
    tela.move(circ,x,y)

def direita(event):
    x=+10
    y=0
    tela.move(circ,x,y)

def subir(event):
    x=0
    y=-10
    tela.move(circ,x,y)

def descer(event):
    x=0
    y=+10
    tela.move(circ,x,y)

x = 300
y = 300
tela = Canvas(janela, height=600, width=600, bg='white')
tela.pack()
circ = tela.create_oval(x,y,x+10,y+10, fill='blue')
#criação de eventos
#.bind recebe um evento
janela.bind('<Left>',esquerda)
janela.bind('<Right>',direita)
janela.bind('<Up>',subir)
janela.bind('<Down>',descer)
janela.mainloop()
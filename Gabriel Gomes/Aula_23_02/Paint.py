from tkinter import *
janela = Tk()
def pintar(event):
    x1,y1 = (event.x-3), (event.y-3)
    x2,y2 = (event.x+3), (event.y+3)
    tela.create_oval(x1,y1,x2,y2,fill='Black')
def limpar():
    tela.delete('all')
janela.title('Atividade')
janela.iconbitmap('kk.ico')
janela.geometry('500x400+385+100')
tela = Canvas(janela, height=500, width=1200, bg='white')
tela.pack()
#B1-Motion defini o botão esquerdo do mouse
tela.bind('<B1-Motion>',pintar)
btn1 = Button(janela, text="Limpar", bg='Gray', command= limpar)
btn1.pack()
janela.mainloop()
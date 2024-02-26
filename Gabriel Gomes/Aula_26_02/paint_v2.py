from tkinter import *
janela = Tk()
color='black'
z=1
def BG():
    tela['bg']=color
def sel():
    global z
    if var.get() == 1:
        z = 1
    if var.get() == 2:
        z = 5
    if var.get() == 3:
        z = 10
def azul():
    global color
    color='blue'
    etq1['bg']='blue'
def vermelho():
    global color
    color='red'
    etq1['bg']='red'
def amarelo():
    global color
    color='yellow'
    etq1['bg']='yellow'
def preto():
    global color
    color='black'
    etq1['bg']='black'
def limpar():
    tela.delete('all')
    tela['bg']='white'
def paint(event):
    global z
    x1,y1 = (event.x-z), (event.y-z)
    x2,y2 = (event.x+z), (event.y+z)
    tela.create_rectangle(x1,y1,x2,y2,fill=color, outline=color)
janela.title('Atividade')
janela['bg']='lightblue'
tela=Canvas(janela,height=550,width=1200,bg="white")
tela.grid(row=1,column=1,rowspan=4,columnspan=3)
tela.bind("<B1-Motion>",paint)

etq = Label(janela,text= 'Aperte e arraste para desenhar', font= 20)
etq.grid(row=0,column=1)
etq1 = Label(janela, bg='Black',padx='10',pady='10')
etq1.grid(row=0,column=3)
btn1 = Button(janela, bg='Yellow', padx='40',pady='10',command= amarelo)
btn1.grid(row=1,column=0)
btn2 = Button(janela, bg='blue', padx='40',pady='10',command= azul)
btn2.grid(row=2,column=0)
btn3 = Button(janela, bg='red', padx='40',pady='10',command= vermelho)
btn3.grid(row=3,column=0)
btn4 = Button(janela, bg='black', padx='40',pady='10',command= preto)
btn4.grid(row=4,column=0)
btn5 = Button(janela, text='limpar', padx='40',pady='10',command= limpar)
btn5.grid(row=0,column=0)
btn6 = Button(janela, text='BackGround', padx='40',pady='10',command= BG)
btn6.grid(row=5,column=0)

#Criação dos botões que definem o tamanho da linhas
var = IntVar()
var.set(1)
rb1=Radiobutton(janela,text='1 mm', variable=var,value=1,command=sel)
rb1.grid(row=5,column=1)
rb2=Radiobutton(janela,text='5 mm', variable=var,value=2,command=sel)
rb2.grid(row=5,column=2)
rb3=Radiobutton(janela,text='10 mm', variable=var,value=3,command=sel)
rb3.grid(row=5,column=3)
janela.mainloop()
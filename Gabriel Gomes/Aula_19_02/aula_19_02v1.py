from tkinter import *
janela = Tk()
janela.title("Aula 16/09")
janela.iconbitmap("kk.ico")
janela.geometry("800x500+100+100")
#Utilizamos o PLACE() para definir um local utilizando coordenadas 
btn1 = Button(janela, text="botão 1")
btn1.place(x=400, y=250, anchor= NE)
btn2 = Button(janela, text="botão 2")
btn2.place(x=400, y=300, anchor= E)
btn3 = Button(janela, text="botão 3")
btn3.place(x=300, y=250)
en = Entry(janela, width=15)
en.place(x=450,y=250, anchor= NW)
janela.mainloop()
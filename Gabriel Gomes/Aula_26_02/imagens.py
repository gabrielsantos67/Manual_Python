from tkinter import *
janela = Tk()
img = PhotoImage(file="PikaChu.png")
lbl1 = Label(janela, image=img)
lbl1.pack()
janela.title("Imagem")
janela.geometry("500x400+35+40")
janela.mainloop()
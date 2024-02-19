from tkinter import *
janela = Tk()
janela.geometry("500x500+100+100")
lbl1 = Label(janela, text="D")
lbl1.pack(side= TOP)
lbl2 = Label(janela, text="C")
#Side= é utilizado para jogar a caixa para a esquerda e o fill= both é uilizado para preencher o espaço
lbl2.pack(side= RIGHT)
lbl3 = Label(janela, text="A",)
lbl3.pack(side= LEFT)
lbl4 = Label(janela, text="B")
lbl4.pack(side= BOTTOM)
janela.mainloop()
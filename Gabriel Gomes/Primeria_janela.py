from tkinter import *
janela = Tk()
def click1():
    etiqueta["text"] = "botão 1"
def click2():
    etiqueta["text"] = "Gabriel Gomes"
janela.title("Empresa")
janela.iconbitmap("kk.ico")
janela['bg']=('SkyBlue')
# Sempre manter o padrão (LxA+E+T) 
# Respectivamente LarguraXAltura+Esquerda+Topo
janela.geometry("500x400+400+120") 
etiqueta = Label(janela,height=5, width=50, text="Olá Mundo", cursor= 'dot')
#heigt = altura // width = largura // bg = backgroud color // fg = cor da linha 
etiqueta.pack()
botao = Button(janela, text="Botão 1", bg="Pink", padx="50", pady="30", command=click2)
botao.pack()
janela.mainloop()


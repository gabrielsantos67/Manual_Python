from tkinter import *
janela = Tk()
janela.title("Empresa")
janela.iconbitmap("kk.ico")
janela['bg']=('SkyBlue')
# Sempre manter o padrão (LxA+E+T) 
# Respectivamente LarguraXAltura+Esquerda+Topo
janela.geometry("500x400+400+120") 
etiqueta = Label(janela,height=5, width=50, text="Aquino cool", cursor= 'dot')
etiqueta.pack()
janela.mainloop()


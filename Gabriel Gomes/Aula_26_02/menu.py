from tkinter import *
janela = Tk()
def abrir():
    print, 'Abrir'
def salvar():
    print, 'Salvar'
def ajuda():
    print, 'Ajuda'
principal = Menu(janela)
arquivo = Menu(principal)
arquivo.add_command(label='Abrir', command= abrir)
arquivo.add_command(label='Salvar', command= salvar)
principal.add_cascade(label='Arquivo', menu=arquivo)
principal.add_command(label='Ajuda', command= ajuda)
janela.configure(menu=principal)
janela.title('Atividade')
janela['bg']='lightblue'
janela.geometry("500x400+440+100")
janela.mainloop()
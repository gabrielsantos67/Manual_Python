from tkinter import *
janela = Tk()
def novo():
    etq1['text']= "Novo"
    etq2['text']= "Novo"
def ajuda():
    etq3 = Label(janela, text='Vá pedir ajuda ao pai dos burros', bg='lightblue')
    etq3.pack()
def exclui():
    etq1['text']= ""
def exclui1():
    etq2['text']= ""
def edita1():
    etq1['text']= "Editado"
def edita2():
    etq2['text']= "Editado"

#Criando o Menu
principal = Menu(janela)
arquivo = Menu(principal, tearoff= 0)
excluir = Menu(principal, tearoff= 0)
editar = Menu(principal, tearoff= 0)

#Criando as cascatas
principal.add_cascade(label='Arquivo', menu=arquivo)
principal.add_cascade(label='Excluir', menu=excluir)
principal.add_cascade(label='Editar', menu=editar)

#Funções para a cascade arquivo
arquivo.add_command(label='Novo', command= novo)
arquivo.add_separator()
arquivo.add_command(label='Fechar', command= janela.quit)

#Funções para a cascade excluir
excluir.add_command(label='Excluir 1', command= exclui)
excluir.add_separator()
excluir.add_command(label='Excluir 2', command= exclui1)

#Funções para a cascade editar
editar.add_command(label='Editar 1', command= edita1)
editar.add_separator()
editar.add_command(label='Editar 2', command= edita2)

#Funções para o botão ajuda
principal.add_command(label='Ajuda', command= ajuda)

#Função para rodar o menu
janela.configure(menu=principal)

#Etiquetas de exibição, sempre separar o pack na linha de baixo
etq1 = Label(janela,text="Texto 1", bg='lightblue')
etq1.pack()
etq2 = Label(janela,text="Texto 2", bg='lightblue')
etq2.pack()

janela.title('Atividade')
janela['bg']='lightblue'
janela.geometry("500x400+440+100")
janela.mainloop()
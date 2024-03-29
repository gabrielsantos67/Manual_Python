import tkinter  
janela = tkinter.Tk()

def Novo():
    text_area.delete(1.0,'end')
def Abrir():
    file = open ('notepad.txt', 'r')
    container = file.read()
    text_area.insert(1.0, container)
def Salvar():
    container = text_area.get(1.0,'end')
    file = open("notepad.txt", 'w')
    file.write(container)
    file.close()
def update():
    font = spin_font.get()
    size = spin_size.get()
    text_area.config(font=f"{font} {size}")

#Menu
principal = tkinter.Menu(janela)
arquivo = tkinter.Menu(principal, tearoff=0)

#Barra de ferramentas
frame = tkinter.Frame(janela,height=30, bg='lightblue')
frame.pack(fill='x')
#Tipo de fonte
fonte_text= tkinter.Label(frame,text='Fonte:', bg='lightblue')
fonte_text.pack(side="left")
spin_font = tkinter.Spinbox(frame, values= ('Arial', 'Verdana', 'Arial Bold', 'Times New Roman', 'Cabrini'))
spin_font.pack(side='left')
#Tamanho da fonte
fonte_size= tkinter.Label(frame,text='Fonte size:', bg='lightblue')
fonte_size.pack(side="left")
spin_size = tkinter.Spinbox(frame, values= ('12', '14', '16', '20'))
spin_size.pack(side='left')
#Update
btn1 = tkinter.Button(frame, text='Update', bg='cyan', command= update)
btn1.pack(side='left')


arquivo.add_command(label='Novo', command= Novo)
arquivo.add_command(label='Abrir', command= Abrir)
arquivo.add_command(label='Salvar', command= Salvar)
arquivo.add_command(label='Fechar', command= janela.quit)


principal.add_cascade(label='Arquivo', menu=arquivo)


text_area= tkinter.Text(janela, font='Arial 20 bold', width=1200, height=800)
text_area.pack()

janela.minsize(width=1208, height=720)
janela.configure(menu=principal)
janela['bg']='lightblue'
janela.title('Notepad')
janela.mainloop()
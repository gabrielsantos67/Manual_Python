from tkinter import *
janela = Tk()
janela.title('Atividade')
janela.iconbitmap('kk.ico')
janela.geometry('500x400+385+100')
tela = Canvas(janela, height=500, width=500, bg='white')
tela.pack()
retan=tela.create_rectangle(0,0,400,300, fill='GREEN')
poli=tela.create_polygon(0,150,200,0,400,150,200,300,fill='YELLOW')
ovo = tela.create_oval(100,50,300,250,fill='BLUE')
linha=tela.create_line(100,150,300,150,fill='WHITE', width=15)
text=tela.create_text(200,150,fill='black', text='ORDEM E PROGRESSO')
janela.mainloop()
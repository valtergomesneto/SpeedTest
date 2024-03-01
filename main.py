from tkinter import *
from PIL import Image, ImageTk
import speedtest
import tkinter.messagebox

#cores

cor0 = "#f0f3f5"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#3fb5a3"  # verde
cor3 = "#fc766d"  # vermelha / red
cor4 = "#403d3d"   # preta / black
cor5 = "#4a88e8"  # Azul / Bblue

#criando janela

janela = Tk()
janela.title("Teste de Conexão e Velocidade")
janela.geometry("350x200")
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)

#dividindo a janela em dois frames

frame_logo = Frame(janela, width=350, height=60, bg=cor1)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_corpo = Frame(janela, width=350, height=140, bg=cor1)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# funcao

def testarConexao():

    st = speedtest.Speedtest()

    l_logo_testando = Label(frame_logo, text='Testando...', padx=10, anchor=NE, font=('ivy 10 bold'), bg=cor1, fg=cor4)
    l_logo_testando.place(x=265, y=30)

    tkinter.messagebox.showinfo('Testando... ', "O teste foi iniciado, aguarde um momento por favor!")

    velocidadeDownload = st.download()/1024/1024
    velocidadeUpload = st.upload()/1024/1024

    download_formatado = "{:.2f}".format(velocidadeDownload)
    upload_formatado = "{:.2f}".format(velocidadeUpload)

    l_Download['text'] = download_formatado
    l_Upload['text'] = upload_formatado
    l_logo_testando['text'] = ''

    l_logo_testandoOk = Label(frame_logo, text='Teste finalizado!', padx=10, anchor=NE, font=('ivy 10 bold'), bg=cor1, fg=cor4)
    l_logo_testandoOk.place(x=225, y=35)


#configurando o frame_logo

imagem = Image.open('speed_icon.png')
imagem = imagem.resize((55,55))
imagem = ImageTk.PhotoImage(imagem)

#criando a label do logo

l_logo_imagem = Label(frame_logo, height=60, image=imagem, compound=LEFT, padx=10, anchor='nw', font=('ivy 16 bold'), bg=cor1, fg=cor3)
l_logo_imagem.place(x=20, y=0)

l_logo_nome = Label(frame_logo, text='Teste de Conexão', padx=10, anchor=NE, font=('ivy 15 bold'), bg=cor1, fg=cor4)
l_logo_nome.place(x=75, y=10)

l_logo_linha = Label(frame_logo, width=350, anchor=NW, font=('ivy 1'), bg=cor2)
l_logo_linha.place(x=0, y=57)

#configurando frame_corpo

l_Upload = Label(frame_corpo, text='', anchor=NW, font=('arial 28'), bg=cor1, fg=cor4)
l_Upload.place(x=15, y=25)
l_Upload_mb = Label(frame_corpo, text='Mbps upload', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_Upload_mb.place(x=20, y=70)

#imagem central

imagem_downUp = Image.open('up_down.png')
imagem_downUp = imagem_downUp.resize((65,65))
imagem_downUp = ImageTk.PhotoImage(imagem_downUp)
l_logo_imagem = Label(frame_corpo, image=imagem_downUp, compound=LEFT, anchor=NE, font=('ivy 20'))
l_logo_imagem.place(x=142, y=20)


l_Download = Label(frame_corpo, text='', anchor=NE, font=('arial 28'), bg=cor1, fg=cor4)
l_Download.place(x=220, y=25)
l_Download_mb = Label(frame_corpo, text='Mbps download', anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_Download_mb.place(x=230, y=70)


#criando botão
btn_testar = Button(frame_corpo, text='Iniciar teste', command=testarConexao, padx=10, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE,bg=cor5, fg=cor1)
btn_testar.place(x=120, y=100)


janela.mainloop()
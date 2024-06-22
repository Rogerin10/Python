from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('Descargador de YouTube')
root.configure(bg='AACDE2')

Label(root, text='Descargar tus Videos',
                font='arial 20 bold', bg='#AACDE2').place(x=90, y=30)

link = StringVar()
Label(root, text='Pegar el link Aqui: ', font='arial 12',
        bg='#AACDE2').place(x=190, y=90)
ljnk_enter = Entry(root, width=70,
                    textvariable= link).place(x=32, y=120)

def Downloader():
    url =YouTube(str(link.get()))
    Video = url.streams.get_highest_resolution()
    Video.Download()
    Label(root, text='DESCARGADO', font='arial 13 bold',
          bg='#AACDE', fg='#B57199').place(x=180, y=240)
    
    Button(root, text='Descargar', font='arial 13 bold italic',
    bg='#B557199', padz=2,
    command=Downloader).place(x=100, y=180)

root.mainloop()


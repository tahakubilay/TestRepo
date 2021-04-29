from tkinter import *
from pytube import YouTube

root=Tk()
root.geometry("750x600")
root.resizable(0,0)
root.title("TAK Youtube Downloader")

link = StringVar()

Label(root, text = "Linki buraya yapıştırın:",font = "arial 15 bold").place(x=180, y=60)
link_enter=Entry(root, width= 40, textvariable= link).place(x=32, y = 110)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text= "İndirildi", font = "arial 15 bold").place (x=375,y=210)

Button(root,text="İNDİR", font = "arial 15 bold",bg ="pale violet red", padx = 2, command = Downloader).place(x=375, y=150)

root.mainloop()
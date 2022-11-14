from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import ImageTk, Image
import numpy as np

root = Tk()
root.title("Tubes 2 ALGEO")
root.iconbitmap(r'./assets/icon.ico')
root.geometry("800x500")


img = ImageTk.PhotoImage(file="./assets/bgr.png")
Label(root, image=img).pack()

objPic = ' '
filepath = ' '


def Directory():
    filename = filedialog.askopenfilename(title='Choose Picture')
    return filename

def DirectoryFolder():
    filename = filedialog.askdirectory(title='Choose Directory')
    return filename

def ChooseFolder():
    global filepath
    filepath = DirectoryFolder()

def ImageProccess():
    global objPic
    objPic = Directory()
    image1 = Image.open(objPic)
    image1 = image1.resize((200, 228), Image.ANTIALIAS)
    image1X = ImageTk.PhotoImage(image1)
    label1 = Label(root, image=image1X)
    label1.image = image1X
    label1.place(x=260, y=155)

buttonDir = Button(root, text='Choose Folder', command=ChooseFolder).place(x= 60, y= 310)
buttonFile = Button(root, text='Choose Image', command=ImageProccess).place(x=60, y=215)


root.mainloop()

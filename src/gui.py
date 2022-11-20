from tkinter import*
from PIL import Image, ImageTk
from tkinter import filedialog
import os


window=Tk()
window.geometry("945x585")
window.iconbitmap(r'./assets/icon.ico')
window.title("Tubes 2 ALGEO")
window.resizable(False, False)

bg = PhotoImage(file="./assets/dilanbg1.png")
labelhome = Label(window, image=bg, border=0)
labelhome.pack()

img_inactive = Image.open("./assets/img1.png")
img_active = Image.open("./assets/img2.png")
window.img_inactive= ImageTk.PhotoImage(img_inactive)
window.img_active= ImageTk.PhotoImage(img_active)

folder_inactive = Image.open("./assets/folder1.png")
folder_active = Image.open("./assets/folder2.png")
window.folder_inactive= ImageTk.PhotoImage(folder_inactive)
window.folder_active= ImageTk.PhotoImage(folder_active)

result_inactive = Image.open("./assets/result1.png")
result_active = Image.open("./assets/result2.png") 
window.result_inactive = ImageTk.PhotoImage(result_inactive)
window.result_active = ImageTk.PhotoImage(result_active)

objPic = ''
pathFolder = ''

def Directory():
    pathGambar = filedialog.askopenfilename(title='Pilih Gambar Untuk Dites')
    return pathGambar

def DirectoryFolder():
    pathFolder = filedialog.askdirectory(title='Pilih Dataset')
    return pathFolder

def ChooseFolder():
    global filepath
    filepath = DirectoryFolder()
    dataF = os.path.split(filepath)
    out=dataF[1]
    imglbl1=Label(window, my_string_var1.set(out))
    

def ImageProccess():
    global objPic
    global out
    objPic = Directory()
    image1 = Image.open(objPic)
    image1 = image1.resize((256, 256), Image.ANTIALIAS)
    image1X = ImageTk.PhotoImage(image1)
    label1 = Label(window, image=image1X, )
    label1.image = image1X
    label1.place(x=325, y=140)
    data = os.path.split(objPic)
    out=data[1]
    imglbl2=Label(window, my_string_var2.set(out))


    

def change_cursor(event):
    window.config(cursor="heart")

def on_enter1(event):
	button1.config(image=window.img_active)
 
def on_leave1(enter):
    button1.config(image=window.img_inactive)
    
def on_enter2(event):
	button2.config(image=window.folder_active)
 
def on_leave2(enter):
    button2.config(image=window.folder_inactive)
    
def on_enter3(event):
	button3.config(image=window.result_active)
 
def on_leave3(enter):
    button3.config(image=window.result_inactive)


my_string_var1 = StringVar()
my_string_var1.set("No file choosen")
my_label1 = Label(window, textvariable = my_string_var1, bg='#FFF7DF', fg = '#624E0E', font=("times", 9), border=0)
my_label1.place(x=175, y=228)

my_string_var2 = StringVar()
my_string_var2.set("No file choosen")
my_label2 = Label(window, textvariable = my_string_var2, bg='#FFF7DF', fg = '#6E5912', font=("times", 9), border=0)
my_label2.place(x=175, y=288)

button1 = Button(window, image=window.img_inactive, border=0, bg='#FFF7DF', activebackground='#FFF7DF',command=ImageProccess)
button1.place(x=40, y=280)
button2 = Button(window, image=window.folder_inactive, border=0, bg='#FFF7DF', activebackground='#FFF7DF', command=ChooseFolder)
button2.place(x=40, y=220)
button3 = Button(window, image=window.result_inactive, border=0, bg='#FFF7DF', activebackground='#FFF7DF')
button3.place(x=45, y=348)

button1.bind("<Enter>", on_enter1)
button1.bind("<Leave>", on_leave1)
button2.bind("<Enter>", on_enter2)
button2.bind("<Leave>", on_leave2)
button3.bind("<Enter>", on_enter3)
button3.bind("<Leave>", on_leave3)
window.bind("<Motion>", change_cursor)
window.mainloop()
    
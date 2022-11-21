from tkinter import*
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import getEigenFace


window=Tk()
window.geometry("945x585")
window.iconbitmap(r'./assets/icon.ico')
window.title("Tubes 2 ALGEO")
window.resizable(False, False)

bg = PhotoImage(file="./assets/dilanbg1.png")
labelhome = Label(window, image=bg, border=0)
labelhome.pack()

persen_lbl = PhotoImage(file="./assets/persentase.png")
labelpersen = Label(window, image=persen_lbl, border=0, bg='#FFF7DF')
labelpersen.place(x=45, y=390)

extime_1 = PhotoImage(file="./assets/train.png")
labelextime1 = Label(window, image=extime_1, border=0, bg='#FFF7DF')
labelextime1.place(x=375, y=490)

extime_2 = PhotoImage(file="./assets/detect.png")
labelextime2 = Label(window, image=extime_2, border=0, bg='#FFF7DF')
labelextime2.place(x=600, y=490)


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
    global eigenfaces
    filepath = DirectoryFolder()
    dataF = os.path.split(filepath)
    out=dataF[1]

    eigenfaces = getEigenFace.getEigenFace(filepath)

    elapsed_time_training = getEigenFace.getElapsedTimeTraining()
    time_text = str(round(elapsed_time_training, ndigits=2)) + " detik"
    time_lbl = Label(window, text=time_text, bg='#FFF7DF', font=("Arial", 25, "bold"), fg="#76460E")
    time_lbl.place(x=375, y=510)

    imglbl1=Label(window, text=out, bg='#FFF7DF')#my_string_var1.set(out))
    imglbl1.place(x=172, y=228)

    popupmsg("Proses mendapatkan gambar menjadi matriks pada folder "+out+" selesai")

#make a pop up message after get the filepath
def popupmsg(msg):
    popup = Tk()
    popup.configure(background='#FFF7DF')
    popup.iconbitmap(r'./assets/icon.ico')
    popup.geometry("+%d+%d" % ((window.winfo_screenwidth() - 500) / 2, (window.winfo_screenheight() - 100) / 2))
    popup.title("Yeay!")
    label = Label(popup, text=msg, font=("Arial", 10), bg='#FFF7DF', fg="#76460E")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

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
    imglbl2=Label(window, text=out, bg='#FFF7DF')#my_string_var2.set(out))

    imglbl2.place(x=320, y=426)   
    hasil = getEigenFace.detectHasil(eigenfaces, filepath, objPic)
    
    persentase = round(hasil[1], ndigits=2)
    persen_text = Label(window, text=str(persentase)+"%", bg='#FFF7DF', font=("Arial", 40, "bold"), fg="#76460E")
    persen_text.place(x=50, y=425)

    elapsed_time_detection = getEigenFace.getElapsedTimeDetection()
    time_text = str(round(elapsed_time_detection, ndigits=2)) + " detik"
    time_lbl = Label(window, text=time_text, bg='#FFF7DF', font=("Arial", 25, "bold"), fg="#76460E")
    time_lbl.place(x=600, y=510)

    image2 = Image.open(os.path.join(filepath, hasil[0]))
    nama1=Label(window, text=hasil[0], bg='#FFF7DF', font=("Arial", 11, "bold"), fg="#76460E")
    nama1.place(x=620, y=426)
    image2 = image2.resize((256, 256), Image.ANTIALIAS)
    image2X = ImageTk.PhotoImage(image2)
    label2 = Label(window, image=image2X, )
    label2.image = image2X
    label2.place(x=625, y=140)

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


# my_string_var1 = StringVar()
# my_string_var1.set("No file choosen")
# my_label1 = Label(window, textvariable = my_string_var1, bg='#FFF7DF', fg = '#624E0E', font=("times", 9), border=0)
# my_label1.place(x=175, y=228)

# my_string_var2 = StringVar()
# my_string_var2.set("No file choosen")
# my_label2 = Label(window, textvariable = my_string_var2, bg='#FFF7DF', fg = '#6E5912', font=("times", 9), border=0)
# my_label2.place(x=175, y=288)

button1 = Button(window, image=window.img_inactive, border=0, bg='#FFF7DF', activebackground='#FFF7DF',command=ImageProccess)
button1.place(x=40, y=280)
button2 = Button(window, image=window.folder_inactive, border=0, bg='#FFF7DF', activebackground='#FFF7DF', command=ChooseFolder)
button2.place(x=40, y=220)
button3 = Button(window, image=window.result_inactive, border=0, bg='#FFF7DF', activebackground='#FFF7DF')
button3.place(x=45, y=348)
tipek_lbl = PhotoImage(file="./assets/typex.png")
labeltipek = Label(window, image=tipek_lbl, border=0, bg='#FFF7DF')
labeltipek.place(x=45, y=348)

button1.bind("<Enter>", on_enter1)
button1.bind("<Leave>", on_leave1)
button2.bind("<Enter>", on_enter2)
button2.bind("<Leave>", on_leave2)
button3.bind("<Enter>", on_enter3)
button3.bind("<Leave>", on_leave3)
window.bind("<Motion>", change_cursor)

window.mainloop()
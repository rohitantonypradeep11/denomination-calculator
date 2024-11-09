from tkinter import *
from tkinter import messagebox
from PIL import image, imageTK

root = Tk()
root.title("denominatio calculator")
root.configure(bg='light blue')
root.geometry("650x400")

upload = image.open("app_img.jpg")
upload = upload.resize((300,300))
image = ImageTK.PhotoImage(upload)
lable = lable(root, image=image, bg = 'light blue')
lable.place(x=180, y=20)

lable1 = Label(root,
               text="hey user! welcome to the denomination counter Aplication.",
               bg='light blue')
lable1.place(relx=0.5. y=340, ancor=CENTER)

def msg():
    if MsgBox == 'ok':
        topwin()

button1 = Button(root,
                 text="lets get started!",
                 command=msg,
                 bg='brown',
                 fg='white,')
button1.place(x=260,y=360)

def topwin():
    top = Toplevel()
    top.title("denomination calculator")
    top.configure(bg='light gray')
    top.geometry("600x350+50+50")

    lable = lable(top, text="enter total amount", bg = 'light gray')
    entry = Entry(top)
    lbl = lable(top, text="here are the number of notes for each denomination", bg='light gary')
    
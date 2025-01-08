# typing practice no. and text
from tkinter import *
from tkinter import ttk

text = Tk()
text.title('***TopFastWriting***😊👌')
text.geometry('400x550')
text.config(bg='orange')


lab = Label(text="👍TopFastWriting***👌",font=('Time New Roman',25,"bold"),bg="yellow",fg="blue")
lab.place(x=40,y=40,height=38,width=350)

lab_txt=Text(text,font=('Time New Roman',30,"bold"),bg="purple",fg="red",borderwidth=25,border=30)
lab_txt.place(x=60,y=80,height=450,width=300)


text.mainloop()
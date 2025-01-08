from tkinter import *
from tkinter import ttk

text = Tk()
text.title('Weather App')
text.geometry('600x500')
text.config(bg="white")


lab_text = Label(text,font=('Time New Roman',45,"bold"),bg="yellow",fg="pink",borderwidth=30)
lab_text.place(x=50,y=20,height=35,width=300)

text.mainloop()
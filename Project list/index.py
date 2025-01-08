# text

from tkinter import *
from tkinter import ttk

text = Tk()
text.title('TEXT_PRACTICE')
text.geometry('500x400')
text.config(bg="blue")


# Label(text="Typing Practice",bg="yellow",fg="pink",font=("Time"),height="200",width="200").pack()
lab = Label(text="TypingPractice",font=('Time New Roman',20,"bold"),bg="yellow",fg="black").pack()
# lab.place(x=50,y=40,height=80,width=300)

lab_txt=Text(text,font=('Time New Roman',40,"bold"),bg='yellow',fg="orange",border=30,borderwidth=45)
lab_txt.place(x=50,y=100,height=300,width=300)


text.mainloop()

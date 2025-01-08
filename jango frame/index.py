from tkinter import *
from tkinter import ttk

def login():
    user=username.get()
    code=password.get()

root = Tk()
root.title("🤷‍♂️TITLE👈")
root.geometry("500x500")
root.config(bg="blue")




lal_txt = Text(root,font=('Time New Roman',20,"bold"),bg="yellow",fg="pink",border=20)
lal_txt.place(x=40,y=30,height=300,width=400)

    # screen.title("Login system")

    #    lblTitle = Label(text="Login System", font=("arial",50,"bold"),fg="#404040",bg="#d7dae2")
    #    lblTitle.pack(pady=50)

    #    bordercolor=Frame(screen,bg="black",width=800,height=400)
    #    bordercolor.pack()



Button(mainframe,text="Login",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=login).place(x=100,y=250)

mainloop()
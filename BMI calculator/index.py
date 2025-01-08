# BMI CALCULATOR

from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

root=Tk()
root.title("BMI Calculator")
root.geometry("470x580")
root.resizable(False,False)
root.configure(bg="blue")


# icon
image_icon=PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)

# top
# top=PhotoImage()
# top_image=Label(root,image=top,background="red")
# top_image.place(x=-10,y=-10)

# bottom box
Label(root,width=72,height=18,bg="lightblue").pack(side=BOTTOM)

# two boxes
box=PhotoImage(file="Images/box.png")
Label(root,image=box).place(x=20,y=100)
Label(root,image=box).place(x=240,y=100)

# scale
Scale





root.mainloop()
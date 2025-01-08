# Google translator using python with GUI

# thinkter ko bar bar na likh na pade us k liye * ka used hota hai
from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

# text,source,destination
def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans = Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text


def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1,0,END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)

root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='blue')

lab_txt=Label(root,text="Translator",font=("Time New Roman",40,"bold"),bg="yellow")
lab_txt.place(x=100,y=40,height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text",font=("Time New Roman",25,"bold"),bg="pink")
lab_txt.place(x=100,y=100,height=30,width=300)

Sor_txt = Text(frame,font=("Time New Roman ",20,"bold"),wrap=WORD,bg="red")
Sor_txt.place(x=40,y=140,height=100,width=430)

# list_text = [1,2,3,4]
list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,values=list_text)
comb_sor.place(x=20,y=300,height=40,width=100)
# comb_sor.place(x=160,y=300,height=40,width=100)
comb_sor.set("english")

button_change = Button(frame,text="Translate",relief=RAISED,command=data())
# button_change.place(x=20,y=300,height=40,width=100)
button_change.place(x=160,y=300,height=40,width=100)

comb_dest = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=300,y=300,height=40,width=100)
comb_dest.set("english1")

# dest_txt = Text(ront=("Time New Roman", 20, "bold"),wrap=WORD)
# dest_txt.place(x=10,y=360,height=150,width=480)

lab_txt=Label(root,text="Dest Text",font=("Time New Roman",20,"bold"),fg="Black",bg="orange")
lab_txt.place(x=100,y=360,height=30,width=300)

dest_txt = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD,bg="red")
dest_txt.place(x=10,y=400,height=150,width=480)

# dest_txt = Text(frame,front=("Time"))



root.mainloop()
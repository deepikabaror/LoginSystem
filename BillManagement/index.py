from tkinter import*
from tkinter import ttk
from tkinter import PhotoImage





root=Tk()
root.title("👉Bill Management👍👩‍💻")
root.geometry("1280x720+150+80")
root.config(bg="skyBlue")
root.resizable(False,False)


# button reset
def Reset():
    entry_dosa.delete(0,END)
    entry_Cookies.delete(0,END)
    entry_Tea.delete(0,END)
    entry_Cofee.delete(0,END)
    entry_Juice.delete(0,END)
    entry_pancakes.delete(0,END)
    entry_eggs.delete(0,END)


def Total():
    try:a1=int(dosa.get())
    except:a1=0

    try:a2=int(cookies.get())
    except: a2=0

    try:a3=int(Tea.get())
    except: a3=0

    try:a4=int(cofee.get())
    except: a4=0

    try:a5=int(juice.get())
    except: a5=0

    try:a6=int(pancakes.get())
    except: a6=0

    try:a7=int(eggs.get())
    except: a7=0

    # define cost of each item per quantity
    c1=60*a1
    c2=30*a2
    c3=7*a3
    c4=100*a4
    c5=20*a5
    c6=15*a6
    c7=7*a7

    lbl_total=Label(f2,font=('aria',20,'bold'),text="Total",width=16,fg="pink",bg="blue")
    lbl_total.place(x=30,y=50)

    entry_total=Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="green")
    entry_total.place(x=50,y=100)

    totalcost=c1+c2+c3+c4+c5+c6+c7
    string_bill="Rs.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)


# title of the bill management
Label(text="👉BILL MANAGEMENT👩‍💻", bg="black",fg="Blue",font=("calibri", 35),width="300", height="2",border="10",borderwidth="20").pack()


# Menu Card
f=Frame(root,bg="purple",highlightbackground="Green",highlightthickness=5,height=370,width=300,background="Black")
f.place(x=1,y=159,height=470,width=351)
# f.pack()

Label(f,text="Menu",font=("Gabriola",43,"bold"),fg="green",bg="Black").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,"bold"),text="Dosa........Rs.90/plate",fg="White",bg="orange").place(x=20,y=80)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Cookies....Rs.80/plate",fg="White",bg="lightpink").place(x=20,y=120)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Tea...........Rs.20/plate",fg="White",bg="purple").place(x=20,y=160)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Coffee.....Rs.100/plate",fg="White",bg="green").place(x=20,y=200)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Juice........Rs.60/plate",fg="White",bg="purple").place(x=20,y=240)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Pancakes..Rs.30/plate",fg="White",bg="red").place(x=20,y=280)
Label(f,font=("Lucida Calligraphy",15,"bold"),text="Eggs..........Rs.10/plate",fg="White",bg="blue").place(x=20,y=320)


# Bill
f2=Frame(root,bg="orange",highlightbackground="purple",highlightthickness=6,width=350,height=460)
f2.place(x=929,y=158)

Bill=Label(f2,text="Bill",font=('calibri',30),bg="orange")
Bill.place(x=120,y=10)





# Entry Work
f1=Frame(root,background="yellow",bd=5,height=601,width=351,relief=RAISED)
f1.pack()

dosa=StringVar()
cookies=StringVar()
Tea=StringVar()
cofee=StringVar()
juice=StringVar()
pancakes=StringVar()
eggs=StringVar()
Total_bill=StringVar()

# Label
lbl_dosa=Label(f1,font=("aria",20,'bold'),text="Dosa",width=15,fg="blue4",background="Black")
lbl_Cookies=Label(f1,font=("aria",20,'bold'),text="Cookies",width=15,fg="blue4",background="Black")
lbl_Tea=Label(f1,font=("aria",20,'bold'),text="Tea",width=15,fg="blue4",background="Black")
lbl_Cofee=Label(f1,font=("aria",20,'bold'),text="Cofee",width=15,fg="blue4",background="Black")
lbl_Juice=Label(f1,font=("aria",20,'bold'),text="Juice",width=15,fg="blue4",background="Black")
lbl_pancakes=Label(f1,font=("aria",20,'bold'),text="Pancakes",width=15,fg="blue4",background="Black")
lbl_eggs=Label(f1,font=("aria",20,'bold'),text="Eggs",width=15,fg="blue4",background="Black")
lbl_dosa.grid(row=1,column=0)
lbl_Cookies.grid(row=2,column=0)
lbl_Tea.grid(row=3,column=0)
lbl_Cofee.grid(row=4,column=0)
lbl_Juice.grid(row=5,column=0)
lbl_pancakes.grid(row=6,column=0)
lbl_eggs.grid(row=7,column=0)



# Entry
entry_dosa=Entry(f1,font=("aria",20,'bold'),textvariable=dosa,bd=6,width=8,bg="lightpink")
entry_Cookies=Entry(f1,font=("aria",20,'bold'),textvariable=cookies,bd=6,width=8,bg="lightpink")
entry_Tea=Entry(f1,font=("aria",20,'bold'),textvariable=Tea,bd=6,width=8,bg="lightpink")
entry_Cofee=Entry(f1,font=("aria",20,'bold'),textvariable=cofee,bd=6,width=8,bg="lightpink")
entry_Juice=Entry(f1,font=("aria",20,'bold'),textvariable=juice,bd=6,width=8,bg="lightpink")
entry_pancakes=Entry(f1,font=("aria",20,'bold'),textvariable=pancakes,bd=6,width=8,bg="lightpink")
entry_eggs=Entry(f1,font=("aria",20,'bold'),textvariable=eggs,bd=6,width=8,bg="lightpink")

entry_dosa.grid(row=1,column=1)
entry_Cookies.grid(row=2,column=1)
entry_Tea.grid(row=3,column=1)
entry_Cofee.grid(row=4,column=1)
entry_Juice.grid(row=5,column=1)
entry_pancakes.grid(row=6,column=1)
entry_eggs.grid(row=7,column=1)




# Button
btn_reset=Button(f1,bd=5,fg="black",bg="lightblue",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,bd=5,fg="Black",bg="lightblue",font=("arial",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)


root.mainloop()
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


root = Tk()
root.title("🤷‍♂️👍Weather App 🤖🥵😶‍🌫️")
root.geometry("900x500+300+200")
root.config(bg="white")
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()

        geolocator = Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        # print(result)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # weather
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=646824f2b7b86caffec1d0b16ea77f79"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"*"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)


    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!")


# search box
# Search_image = PhotoImage(file="GUI_PROJECT/image/searchs.png")
# my_image = Label(image=Search_image)
# my_image.place(x=20,y=20)

# text typing
textfield = tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#1ab5ef",border=0,fg="blue", relief="solid", borderwidth=7)
textfield.place(x=50,y=50)
textfield.focus()


search_icon = PhotoImage(file="GUI_PROJECT/image/search1.png")
my_image_icon = Button(image=search_icon,borderwidth=1,cursor="hand2",bg='#404040',command=getWeather)
my_image_icon.place(x=375,y=51,height=45,width=40)

# logo
Logo_image = PhotoImage(file="GUI_PROJECT/image/logo.jpg")
logo = Label(image=Logo_image)
logo.place(x=150,y=180,height=130,width=130)

# Bottom box
Frame_image = PhotoImage(file="GUI_PROJECT/image/box1.jpg")
frame_myimage = Label(image=Frame_image)
frame_myimage.place(x=50,y=20,height=50,width=200)
frame_myimage.pack(side=BOTTOM)
# padx=2,pady=2,

# time
name=Label(root,font=("arial",15,"bold"),bg="white",fg="green")
name.place(x=32,y=102)
clock=Label(root,font=("Helvetica",20),bg="white",fg="green")
clock.place(x=30,y=130)




# label
label1 = Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="orange",bg="white",border=3,borderwidth=2)
label1.place(x=120,y=400)

label2 = Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="orange",bg="white")
label2.place(x=255,y=400)

label3 = Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="orange",bg="white")
label3.place(x=430,y=400)

label4 = Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="orange",bg="white")
label4.place(x=650,y=400)


t=Label(font=("arial",70,"bold"),bg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="pink")
w.place(x=130,y=430)

h=Label(text="...",font=("arial",20,"bold"),bg="pink")
h.place(x=290,y=430)

d=Label(text="...",font=("arial",20,"bold"),bg="pink")
d.place(x=480,y=430)

p=Label(text="...",font=("arial",20,"bold"),bg="pink")
p.place(x=690,y=430)








root.mainloop()
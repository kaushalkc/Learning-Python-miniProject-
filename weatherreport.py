from requests import get
from pprint import pprint
from tkinter import *
root=Tk()
def press():
    api_key = "093790c3c6b3a118d45280bbdd2fa39a&units=metric"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = cty.get()
    comp_url = base_url + "appid=" + api_key + "&q=" + city_name
    #print(comp_url)
    response = get(comp_url)
    x = response.json()
    country = x['sys']['country']
    name=x['name']
    lat = x['coord']['lat']
    lon = x['coord']['lon']
    description = x['weather'][0]['description']
    temp = x['main']['temp']
    feels_like=x['main']['feels_like']
    humidity=x['main']['humidity']
    speed = x['wind']['speed']
    pressure=x['main']['pressure']
    con.set('{} '.format(country))
    na.set('{} '.format(name))
    la.set('{} '.format(lat))
    log.set('{} '.format(lon))
    de.set('{} '.format(description))
    tp.set('{} °C'.format(temp))
    fl.set('{} °C'.format(feels_like))
    hum.set('{} '.format(humidity))
    spd.set('{} m/s'.format(speed))
    pres.set('{} '.format(pressure))
    #pprint(x)
root.title("Weather app")
root.geometry('500x350')
root.resizable(0,0)
#root.config(background="white")
lable1 = Label(root, text="Enter city name for Weather-Report", font=("bold"))
lable1.config(bg='light green',fg='red')
lable1.grid(row=0, column=0)
cty = StringVar()
c = Entry(root, textvariable=cty, bd=2).grid(row=1, column=0)
but = Button(root, text=' search', fg='black', bg='sky blue',relief='groove',command=lambda: press(), height=1, width=8,bd=4)
but.grid(row=1, column=1)
lablex = Label(root, text="Location and Weather Information of Your City:", font=("bold")).grid(row=2, column=0)
lable2 = Label(root, text="Country : ", font=("bold")).grid(row=3, column=0)
lable3 = Label(root, text="City : ", font=("bold")).grid(row=4, column=0)
lable4 = Label(root, text="Latitude : ", font=("bold")).grid(row=5, column=0)
lable5 = Label(root, text="Longitude : ", font=("bold")).grid(row=6, column=0)
lable6 = Label(root, text="Description : ", font=("bold")).grid(row=7, column=0)
lable7 = Label(root, text="Temperature : ", font=("bold")).grid(row=8, column=0)
lable8 = Label(root, text="Feels Like : ", font=("bold")).grid(row=9, column=0)
lable9 = Label(root, text="Humidity : ", font=("bold")).grid(row=10, column=0)
lable10 = Label(root, text="Wind Speed : ", font=("bold")).grid(row=11, column=0)
lable11 = Label(root, text="Pressure : ", font=("bold")).grid(row=12, column=0)
con = StringVar()
co = Label(root, textvariable=con, borderwidth=4, relief="flat").grid(row=3, column=1)
na = StringVar()
n = Label(root, textvariable=na, borderwidth=4, ).grid(row=4, column=1)
la = StringVar()
l = Label(root, textvariable=la, ).grid(row=5, column=1)
log = StringVar()
lo = Label(root, textvariable=log,).grid(row=6, column=1)
de = StringVar()
d = Label(root, textvariable=de).grid(row=7, column=1)
tp = StringVar()
t = Label(root, textvariable=tp).grid(row=8, column=1)
fl = StringVar()
f = Label(root, textvariable=fl, ).grid(row=9, column=1)
hum = StringVar()
h = Label(root, textvariable=hum,).grid(row=10, column=1)
spd = StringVar()
s = Label(root, textvariable=spd, ).grid(row=11, column=1)
pres = StringVar()
p = Label(root, textvariable=pres, ).grid(row=12, column=1)
root.mainloop()
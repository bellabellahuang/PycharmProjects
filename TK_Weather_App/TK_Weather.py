from tkinter import *
from tkinter import ttk
from Get_Weather import get_weather_for_city

def get_weather(*args):
    weather.set(get_weather_for_city(city.get()))

root = Tk()
root.title("Get Weather by City")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

city = StringVar()
weather = StringVar()

city_entry = ttk.Entry(mainframe, width=7, textvariable=city)
city_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Submit", command=get_weather).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Enter a city: ").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, textvariable=weather).grid(column=1, row=2, sticky=(W,E))

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

city_entry.focus()
root.bind('<Return>', get_weather)

root.mainloop()
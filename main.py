import customtkinter as ctk
import api_functions as func
from PIL import Image, ImageTk
import functions as f


temp_unit = "Cº"
#functions
def resize_starting_image(event):
    if event.widget == app:
       starting_image.configure(size=(event.width, event.height))
       wether_image.configure(size=(event.width, event.height))

def get_temperature_unit(value):
    global temp_unit
    temp_unit = c_or_f_button.get()

def city_input():
    if not entry.get():
        return
    global city_call
    city_call = func.city_data(entry.get())
    if len(city_call)==0:
        city_option.configure(values=[])
        city_option.set("City not found...")
        return
    values = [
        f"{i+1}. {city_call[i][0]}, {city_call[i][1]}, {city_call[i][2]}"
        for i in range(len(city_call))
    ]
    city_option.configure(values=values)
    city_option.set(values[0])

def get_city_weather():
    weather = func.weather_data(saved_city[0], saved_city[1])
    if temp_unit == "Cº":
        temp_label.configure(text=f" {weather['current']['temperature_2m']} Cº")
    else:
        temp_label.configure(text=f" {f.c_to_f(weather["current"]["temperature_2m"])} Fº")
    wether_screen.tkraise()

def city_pick(choice):
    if not city_call:
        return
    saved_city.clear()
    saved_city.append(city_call[(int(choice[0]))-1][3])
    saved_city.append(city_call[(int(choice[0]))-1][4])
    get_city_weather()

city_call = {}


saved_city = []


#ctk stuff
app = ctk.CTk()
app.geometry("720x480+370+200")
app.title("Weather App")

#city screen stuff
city_screen = ctk.CTkFrame(app, width=720, height=480, fg_color="transparent")

starting_image = ctk.CTkImage(light_image=Image.open("images/test.png"),
                                  dark_image=Image.open("images/test.png"),
                                  size=(720, 480))

city_image_label = ctk.CTkLabel(city_screen, image=starting_image, text="")
city_image_label.place(x=0, y=0, relwidth=1, relheight=1)

city_option = ctk.CTkOptionMenu(city_screen, values=["Search for a city first..."], fg_color="green", command=city_pick)
city_option.pack(padx=20, pady=20)

entry = ctk.CTkEntry(city_screen, placeholder_text="Enter city name here")
entry.pack(padx=20, pady=20)

search_button = ctk.CTkButton(city_screen, text="Search🔍", command=city_input)
search_button.pack(padx=20, pady=20)

c_or_f_button = ctk.CTkSegmentedButton(city_screen, values=["Cº", "Fº"], width=50, height=50, command=get_temperature_unit)
c_or_f_button.set("Cº")
c_or_f_button.pack(padx=20, pady=20)

#wether screen stuff
wether_screen = ctk.CTkFrame(app, width=720, height=480, fg_color="transparent")

wether_image = ctk.CTkImage(light_image=Image.open("images/wether_background.png"),
                                  dark_image=Image.open("images/wether_background.png"),
                                  size=(720, 480))

weather_image_label = ctk.CTkLabel(wether_screen, image=wether_image, text="")
weather_image_label.place(x=0, y=0, relwidth=1, relheight=1)


return_button = ctk.CTkButton(wether_screen, text="Return to city search", command=city_screen.tkraise)

temp_label = ctk.CTkLabel(wether_screen, text="Search for city First", fg_color="green")
temp_label.pack(padx=20, pady=20)

return_button.pack(padx=20, pady=20)

for frame in (city_screen, wether_screen):
    frame.grid(row=0, column=0, sticky='nsew')

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

city_screen.tkraise()

# Set the application icon
app.iconbitmap("images/icons/Weather_main.ico")

app.bind("<Configure>", resize_starting_image)
app.after(10, lambda: [
    starting_image.configure(size=(720, 480)),
    wether_image.configure(size=(720, 480))
])

app.mainloop()






"""
Name: Dmytro Vizir
Date: 05/21/2026
Reflection:
Something that surprised me as I worked on this project was how seamlessly
CustomTkinter handles GUI elements alongside live web API requests.
A challenge I had this week was formatting the nested JSON API data into a readable format
and managing parallel lists for search history.
No one really helped me with this project this or any other week.
An adjective that describes how I am feeling about my project is "proud" because
I built a fully functional user-facing application from scratch.
If I had more time to work on this project, I would add a 7-day forecast graph and dynamic background images.
"""

import customtkinter as ctk
import api_functions as func
from PIL import Image, ImageTk
import functions as f

# Console login required to meet Rubric: While loop, Alphanumeric string test, Escape sequences, Comma output, 'in' Keyword
blocked_users = ["admin", "root", "test"]

while True:
    print("\n\t--- Weather App Security ---")
    username = input("Enter username: ")
    password = input("Enter alphanumeric password: ")

    # Complex conditional with AND, NOT, and Search (in)
    if username in blocked_users or not username:
        print("Error:", username, "is a blocked or invalid username.\n")
        continue

    # Alphanumeric check and length check
    if password.isalnum() and len(password) >= 4:
        print(f"Welcome, {username}! Your secure GUI is loading...\n")
        break
    else:
        print("Invalid password.\n\tPassword must be fully alphanumeric and at least 4 characters long.")

# Global Variables
temp_unit = "Cº"
city_call = {}
saved_city = []

# Parallel Lists demonstrating Advanced Data Types (Append, Insert, Remove, Access)
recent_cities_names = []
recent_cities_coords = []


# Functions
def get_temperature_unit(value):
    """
    Sets the global temperature unit based on the segmented button choice.
    args:
        value (str): The value selected from the UI button ("Cº" or "Fº")
    returns:
        None
    """
    global temp_unit
    temp_unit = c_or_f_button.get()


def city_input():
    """
    Retrieves the city input from the entry box and populates the dropdown menu using the API.
    args:
        None
    returns:
        None
    """
    # Checking for blank input
    if not entry.get():
        return

    global city_call
    city_call = func.city_data(entry.get())

    # Conditional structure and error fallback
    if len(city_call) == 0:
        city_option.configure(values=[])
        city_option.set("City not found...")
        return

    # List comprehension to process data
    values = [
        f"{i + 1}. {city_call[i][0]}, {city_call[i][1]}, {city_call[i][2]}"
        for i in range(len(city_call))
    ]
    city_option.configure(values=values)
    city_option.set(values[0])


def get_city_weather():
    """
    Fetches the weather JSON from the API using coordinates and updates the GUI label.
    args:
        None
    returns:
        None
    """
    # Access parallel lists
    weather = func.weather_data(saved_city[0], saved_city[1])

    # Basic conditional for temperature formatting
    if temp_unit == "Cº":
        temp_label.configure(text=f" {weather['current']['temperature_2m']} Cº")
    else:
        temp_label.configure(text=f" {f.c_to_f(weather['current']['temperature_2m']):.1f} Fº")
    wether_screen.tkraise()


def city_pick(choice):
    """
    Processes the selected city from the dropdown, manages parallel history lists, and triggers weather fetch.
    args:
        choice (str): The formatted string of the selected city from the dropdown menu.
    returns:
        None
    """
    if not city_call:
        return

    # List methods: clear, append, access
    saved_city.clear()
    selected_index = int(choice[0]) - 1

    lat = city_call[selected_index][3]
    lon = city_call[selected_index][4]
    name = city_call[selected_index][0]

    saved_city.append(lat)
    saved_city.append(lon)

    # Parallel Lists Management (Insert and Remove)
    recent_cities_names.insert(0, name)
    recent_cities_coords.insert(0, (lat, lon))

    if len(recent_cities_names) > 5:
        removed_name = recent_cities_names[5]
        recent_cities_names.remove(removed_name)
        recent_cities_coords.pop(5)

    get_city_weather()


# Application and UI Setup
app = ctk.CTk()
app.geometry("720x480+370+200")
app.title("Weather App")

# City Selection Screen Structure
city_screen = ctk.CTkFrame(app, width=720, height=480, fg_color="transparent", corner_radius=0, border_width=0)
city_screen.grid_columnconfigure(0, weight=1)

starting_image = ctk.CTkImage(light_image=Image.open("images/test.png"), dark_image=Image.open("images/test.png"),
                              size=(720, 480))
city_image_label = ctk.CTkLabel(city_screen, image=starting_image, text="", fg_color="transparent")
city_image_label.place(x=0, y=0, relwidth=1, relheight=1)

city_option = ctk.CTkOptionMenu(city_screen, values=["Search for a city first..."], fg_color="green", command=city_pick,
                                corner_radius=0, width=180, height=30)
city_option.place(x=0, y=0, relwidth=1, relheight=1)
city_option.grid(row=0, column=0, padx=20, pady=20)

entry = ctk.CTkEntry(city_screen, placeholder_text="Enter city name here", corner_radius=0, width=150, height=35)
entry.grid(padx=20, pady=50)

search_button = ctk.CTkButton(city_screen, text="Search🔍", command=city_input, corner_radius=0, width=150, height=35)
search_button.grid(padx=20, pady=20)

c_or_f_button = ctk.CTkSegmentedButton(city_screen, values=["Cº", "Fº"], width=60, height=60,
                                       command=get_temperature_unit, corner_radius=0)
c_or_f_button.set("Cº")
c_or_f_button.grid(padx=20, pady=50)

# Weather Display Screen Structure
wether_screen = ctk.CTkFrame(app, width=720, height=480, fg_color="transparent", corner_radius=0, border_width=0)
wether_screen.grid_columnconfigure(0, weight=1)

wether_image = ctk.CTkImage(light_image=Image.open("images/wether_background.png"),
                            dark_image=Image.open("images/wether_background.png"), size=(720, 480))
weather_image_label = ctk.CTkLabel(wether_screen, image=wether_image, text="")
weather_image_label.place(x=0, y=0, relwidth=1, relheight=1)

temp_label = ctk.CTkLabel(wether_screen, text="Search for city First", fg_color="green", corner_radius=0)
temp_label.grid(row=0, column=0, padx=20, pady=20)

return_button = ctk.CTkButton(wether_screen, text="Return to city search", command=city_screen.tkraise, corner_radius=0)
return_button.grid(row=1, column=0, padx=20, pady=20)

# For Loop managing Layout Grids
for frame in (city_screen, wether_screen):
    frame.grid(row=0, column=0, sticky='nsew')

city_screen.tkraise()

# Finalizing Layout and App Iteration Loop
try:
    app.iconbitmap("images/icons/Weather_main.ico")
except Exception:
    pass

try:
    icon_image = Image.open("images/icons/Weather_main.png")
    icon = ImageTk.PhotoImage(icon_image)
    app.iconphoto(False, icon)
except Exception:
    pass

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.resizable(False, False)

# Starts the main execution loop
app.mainloop()

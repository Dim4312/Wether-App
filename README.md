# Weather App

A secure, desktop-based graphical user interface (GUI) application that allows users to search for cities worldwide and retrieve precise current weather data. Built for a Python Honors Project, this application communicates with the Open-Meteo API to fetch geocoding and weather forecast data.

## Features

- **Security Verification:** Console-based login sequence requiring an alphanumeric password before the GUI launches.
- **Dynamic City Search:** Utilizes the Open-Meteo Geocoding API to find cities and process precise coordinates.
- **Real-Time Weather Data:** Fetches and displays current temperature metrics.
- **Unit Conversion:** Easily toggle between Celsius (Cº) and Fahrenheit (Fº) using segmented buttons.
- **Search History:** Tracks recent cities using parallel lists memory structures.
- **Modern UI:** Built with `customtkinter` for a polished, dark/light-mode compatible interface.

## Prerequisites

Ensure you have Python 3.x installed along with the following required libraries:

- `customtkinter`
- `requests`
- `Pillow`

You can install the dependencies via pip:

pip install customtkinter requests pillow

Project Structure
main.py - The core application script handling the user login, GUI setup, and event routing.
api_functions.py - Contains functions bridging to the Open-Meteo API for fetching city coordinates and weather forecasts.
functions.py - Contains helper tools, such as the Celsius to Fahrenheit mathematical conversion.
images/ - Directory for storing graphic assets (test.png, wether_background.png) and application icons.

Usage
Run the application through your terminal or IDE:
## python main.py
Interact with the console to bypass the security check. (Hint: Make sure your username is not blocked and your password is at least 4 alphanumeric characters.)
Once the GUI loads, enter a city name into the text box and click Search.
Select the correct geographic location from the dropdown menu.
Use the segmented toggle to switch between Cº and Fº, and view the updated temperature on the weather screen.

Author
Dmytro Vizir
Developed as part of the Python I Honors Project.

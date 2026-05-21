# Weather App

A secure, modern desktop GUI application for searching cities worldwide and retrieving real-time weather data. Built as part of a Python Honors Project, the Weather App emphasizes security, usability, and a polished user interface.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Author](#author)

## Features

- **Security Verification**  
  Console-based login sequence requiring an alphanumeric password (minimum 4 characters) before launching the GUI.
- **World City Search**  
  Quickly search cities around the globe with auto-suggest powered by the Open-Meteo Geocoding API.
- **Real-Time Weather Data**  
  Displays up-to-date temperature information.
- **Unit Conversion**  
  Easily toggle between Celsius (°C) and Fahrenheit (°F).
- **Search History**  
  Automatically tracks recently searched cities in memory.
- **Modern UI**  
  Utilizes `customtkinter` for a polished interface and (optional) dark/light mode compatibility.

## Demo

<!-- If you have a screenshot or GIF, add it here like below: -->
<!-- ![Weather App Demo](images/demo.gif) -->

## Prerequisites

- Python 3.x

### Required Libraries

- `customtkinter`
- `requests`
- `Pillow`

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Dim4312/Wether-App.git
   cd Wether-App
   ```

2. **Install dependencies:**
   ```sh
   pip install customtkinter requests pillow
   ```

## Project Structure

```
main.py            # Core application: login, GUI setup, event routing
api_functions.py   # API calls for city geo-coordinates & weather data
functions.py       # Helper utilities (e.g., Celsius ↔ Fahrenheit conversion)
images/            # Graphic assets (icons, backgrounds)
```

## Usage

1. **Start the application in your Terminal or IDE:**
   ```sh
   python main.py
   ```

2. **Security Verification:**  
   Enter an eligible username and an alphanumeric password (at least 4 characters) in the console to proceed.

3. **Using the App:**
   - Enter a city name and click **Search**
   - Select the correct location from the dropdown (if multiple results)
   - Switch temperature units with the toggle as desired

## Author

Developed by **Dmytro Vizir**  
Part of the Python I Honors Project

---

*Feel free to contribute or suggest improvements via pull requests or issues!*

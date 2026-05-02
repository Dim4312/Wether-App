import requests


def city_data(name):
    try:
        geo_response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={name}&count=5")
        geo_data = geo_response.json()
        cities = {}
        try:
            for num in range(len(geo_data["results"])):
                cities[num]=(geo_data["results"][num]["name"],
                             geo_data["results"][num]["country_code"],
                             geo_data["results"][num]["admin1"],
                             geo_data["results"][num]["latitude"],
                             geo_data["results"][num]["longitude"])
        except KeyError:
            print("City not found")
        return cities
    except requests.exceptions.ConnectionError:
        print("Connection error")


def weather_data(latitude, longitude):
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        "&current=temperature_2m,dew_point_2m"
        "&daily=temperature_2m_max,temperature_2m_min"
        "&forecast_days=7"
    )
    return response.json()
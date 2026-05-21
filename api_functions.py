import requests


def city_data(name):
    """
    Queries the open-meteo API to find details about a searched city.
    args:
        name (str): The name of the city to search for
    returns:
        cities (dict): A dictionary mapping index integers to city data tuples
    """
    # Try block handles overall connection issues with the web API
    try:
        geo_response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={name}&count=5")
        geo_data = geo_response.json()
        cities = {}

        # Inner try block handles KeyError if "results" is missing (meaning city is invalid)
        try:
            for num in range(len(geo_data["results"])):
                cities[num] = (geo_data["results"][num]["name"],
                               geo_data["results"][num]["country_code"],
                               geo_data["results"][num]["admin1"],
                               geo_data["results"][num]["latitude"],
                               geo_data["results"][num]["longitude"])
        except KeyError:
            print("City not found in API response.")

        return cities
    except requests.exceptions.ConnectionError:
        print("Connection error: Unable to reach the API.")
        return {}


def weather_data(latitude, longitude):
    """
    Fetches the 7-day forecast data utilizing the city's coordinates.
    args:
        latitude (float): The geographical latitude of the city
        longitude (float): The geographical longitude of the city
    returns:
        dictionary: A JSON parsed dictionary containing current and forecast weather data
    """
    # Uses formatted strings to inject variables into the API URL seamlessly
    response = requests.get(
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        "&current=temperature_2m,dew_point_2m"
        "&daily=temperature_2m_max,temperature_2m_min"
        "&forecast_days=7"
    )
    return response.json()

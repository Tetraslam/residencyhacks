from dotenv import load_dotenv
import os
import math
import requests

# Load environment variables from a .env file
load_dotenv()

"""
get_coords(city_name)
"""

def city_name_to_lat_lon(name):
    """
    Convert a city name to its latitude and longitude using the OpenWeather API.
    
    Args:
        name (str): The name of the city.
    
    Returns:
        tuple: A tuple containing the latitude and longitude of the city.
    """
    openweather = os.getenv("OPENWEATHER")
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={name}&limit=1&appid={openweather}"
    response = requests.get(url)
    data = response.json()
    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])
    return lat, lon

def lat_lon_to_tile_coordinates(latitude, longitude, zoom_level):
    """
    Convert latitude and longitude to tile coordinates for a given zoom level.
    
    Args:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.
        zoom_level (int): The zoom level for the tile.
    
    Returns:
        tuple: A tuple containing the x and y tile coordinates.
    """
    lat_rad = math.radians(latitude)
    n = 2.0 ** zoom_level
    x_tile = int((longitude + 180.0) / 360.0 * n)
    y_tile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return x_tile, y_tile

def get_tile(zoom, x, y, name):
    """
    Retrieve a map tile image from the Retina Tiles API and save it as a PNG file.
    
    Args:
        zoom (int): The zoom level for the tile.
        x (int): The x tile coordinate.
        y (int): The y tile coordinate.
        name (str): The name of the city (used as the filename).
    
    Returns:
        None
    """
    url = f"https://retina-tiles.p.rapidapi.com/local/osm@2x/v1/{zoom}/{x}/{y}.png"
    headers = {
        "x-rapidapi-key": os.getenv("RAPID_API_KEY"),
        "x-rapidapi-host": "retina-tiles.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        with open(f"{name}.png", "wb") as f:
            f.write(response.content)
    else:
        print(f"Failed to retrieve image. Status code: {response.status_code}")

def get_coords(city_name):
    """
    Get the coordinates of a city and retrieve the corresponding map tile image.
    
    Args:
        city_name (str): The name of the city.
    
    Returns:
        None
    """
    lat_lon = city_name_to_lat_lon(city_name)
    lat = lat_lon[0]
    lon = lat_lon[1]
    coordinates = lat_lon_to_tile_coordinates(lat, lon, 10)
    get_tile(10, coordinates[0], coordinates[1], city_name)

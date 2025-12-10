"""
Author: Tianchen Yu
Weather API Module

This module handles all interactions with OpenWeather API, including fetch weather data and parse
response
"""

import requests
from config import API_KEY, API_BASE_URL, UNITS
def _build_url(city_name):
    """
    Build the complete url with query parameters
    
    :param city_name: city name
    returns: str for complete url for the api request
    """
    url = f"{API_BASE_URL}?q={city_name}&appid={API_KEY}&units={UNITS}"
    return url

def _parse_response(json_data):
    """
    Parse the raw api response into a clean data structure
    
    :param json_date: raw JSON data response
    returns: dict with weather data
    """
    weather_data = {
        "city": json_data.get("name", "Unknown"),
        "country": json_data.get("sys", {}).get("country", "Unknown"),
        "temperature": json_data.get("main", {}).get("temp"),
        "feels_like": json_data.get("main", {}).get("feels_like"),
        "humidity": json_data.get("main", {}).get("humidity"),
        "description": json_data.get("weather", [{}])[0].get("description", "Unknown"),
        "wind_speed": json_data.get("wind", {}).get("speed")

    }

    return weather_data


def fetch_weather(city_name):
    """
    Fetch current weather data for a given city
    
    :param city_name (str): city name
    returns: parsed the weather data if successful
    """
    url = _build_url(city_name)

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            # Success - parse and return the data
            json_data = response.json()
            return _parse_response(json_data)
        
        elif response.status_code == 404:
            # City not found
            print(f"Error: City '{city_name}' not found.")
            return None
        
        elif response.status_code == 401:
            # Invalid API key
            print("Error: Invalid API key.")
            return None
        
        elif response.status_code == 429:
            # Rate limited
            print("Error: Too many requests.")
            return None
        
        else:
            
            print(f"Error: Unexpected response (status code: {response.status_code})")
            return None
    
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect.")
        return None
    
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
        return None
    
    except requests.exceptions.RequestException as e:
        print(f"Error: An unexpected error occurred: {e}")
        return None
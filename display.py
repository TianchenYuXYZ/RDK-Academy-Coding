"""
Author: Tianchen Yu
Create Time: Dec/09/2025
Display Module

"""

from config import TEMP_UNIT, SPEED_UNIT


def show_menu():
    """
    Display the main menu options.
    """
    
    print("  1. Search weather for a city")
    print("  2. Add last searched city to favorites")
    print("  3. List favorite cities")
    print("  4. Remove a city from favorites")
    print("  5. Exit")



def show_weather(weather_data):
    """
    Display weather information for a single city.
    """
    if weather_data is None:
        print("No weather data to display.")
        return
    
    city = weather_data.get("city", "Unknown")
    country = weather_data.get("country", "")
    temp = weather_data.get("temperature", "N/A")
    feels_like = weather_data.get("feels_like", "N/A")
    humidity = weather_data.get("humidity", "N/A")
    description = weather_data.get("description", "N/A")
    wind_speed = weather_data.get("wind_speed", "N/A")
    
   
    if isinstance(description, str):
        description = description.capitalize()
    
    print(f"│   {city}, {country}".ljust(41) + "│")
   
    print(f"│  Temperature:  {temp}{TEMP_UNIT}".ljust(41) + "│")
    print(f"│  Feels like:   {feels_like}{TEMP_UNIT}".ljust(41) + "│")
    print(f"│  Humidity:     {humidity}%".ljust(41) + "│")
    print(f"│  Condition:    {description}".ljust(41) + "│")
    print(f"│  Wind speed:   {wind_speed} {SPEED_UNIT}".ljust(41) + "│")
   


def show_weather_compact(weather_data):
    """
    Display weather information in a compact single-line format.
    Useful for listing multiple cities.
    
    """
    if weather_data is None:
        return
    
    city = weather_data.get("city", "Unknown")
    country = weather_data.get("country", "")
    temp = weather_data.get("temperature", "N/A")
    description = weather_data.get("description", "N/A")
    
    if isinstance(description, str):
        description = description.capitalize()
    
    print(f"  {city}, {country}: {temp}{TEMP_UNIT} - {description}")


def show_favorites_list(favorites_list):
    """
    Display all favorite cities with their weather information.

    """
    if not favorites_list:
        print("\n Your favorites list is empty.")
        print("   Use option 1 to search for a city, then option 2 to add it.")
        return
    
    print("\n" + "=" * 45)
    print(f"  Your Favorite Cities ({len(favorites_list)}/3)")
    print("=" * 45)
    
    for i, weather_data in enumerate(favorites_list, 1):
        city = weather_data.get("city", "Unknown")
        country = weather_data.get("country", "")
        temp = weather_data.get("temperature", "N/A")
        description = weather_data.get("description", "N/A")
        
        if isinstance(description, str):
            description = description.capitalize()
        
        print(f"\n  {i}. {city}, {country}")
        print(f" {temp}{TEMP_UNIT} | {description}")
    
    print("\n" + "=" * 45)


def show_favorites_for_removal(favorite_names):
    """
    Display favorite cities as a numbered list for removal selection.
    
    Args:
        favorite_names (list): List of city names
    
    Returns:
        None
    """
    if not favorite_names:
        print("\n Your favorites list is empty. Nothing to remove.")
        return
    
    print("\n--- Your Favorites ---")
    for i, name in enumerate(favorite_names, 1):
        print(f"  {i}. {name}")
    print("  0. Cancel")


def show_success(message):
    """
    Display a success message.
    
    Args:
        message (str): Success message to display
    """
    print(f"\n {message}")


def show_error(message):
    """
    Display an error message.
    
    Args:
        message (str): Error message to display
    """
    print(f"\n {message}")


def show_info(message):
    """
    Display an informational message.
    
    Args:
        message (str): Info message to display
    """
    print(f"\nℹ{message}")


def show_goodbye():
    """
    Display exit message.
    """
    print("\n" + "=" * 45)
    print("  Thank you for using Weather CLI! Goodbye! ")
    print("=" * 45 + "\n")


def get_user_input(prompt):
    """
    Get input from user with a formatted prompt.
    
    Args:
        prompt (str): The prompt to display
    
    Returns:
        str: User's input (stripped of whitespace)
    """
    return input(f"\n{prompt}").strip()


def get_menu_choice():
    """
    Get the user's menu choice.
    
    Returns:
        str: User's input
    """
    return input("\nEnter your choice (1-5): ").strip()



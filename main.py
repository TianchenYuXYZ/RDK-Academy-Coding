"""
Author: Tianchen Yu
Docstring for main
"""

"""
Weather CLI Application

A command-line application that interacts with the OpenWeather API
to manage weather details of cities.

Features:
- Search for weather details of any city
- Add cities to favorites (max 3)
- List favorite cities with current weather
- Remove cities from favorites

Author: [Your Name]
Date: [Date]
"""

from weather_api import fetch_weather
from favorite_manager import (
    add_favorite,
    remove_favorite,
    get_all_favorites,
    get_favorite_names,
    is_favorite,
    is_full,
    is_empty,
    favorites_count
)
from display import (
    show_menu,
    show_weather,
    show_favorites_list,
    show_favorites_for_removal,
    show_success,
    show_error,
    show_info,
    show_goodbye,
    get_user_input,
    get_menu_choice
)


# Store the last searched city's weather data
last_searched = None


def search_city():
    """
    Search for weather details of a city.
    Getting city name, fetches weather from API,
    and displays the results. Stores result in last_searched
    for potential addition to favorites.
    """
    global last_searched
    
    city_name = get_user_input("Enter city name: ")
    
    # Validate input
    if not city_name:
        show_error("City name cannot be empty. Please try again.")
        return
    
    # Fetch weather from API
    show_info(f"Searching for '{city_name}'...")
    weather_data = fetch_weather(city_name)
    
    if weather_data:
        # Success - display weather and store for later
        show_weather(weather_data)
        last_searched = weather_data
        
        # Show helpful hint if not already in favorites
        city = weather_data.get("city", "")
        if not is_favorite(city) and not is_full():
            show_info("Tip: Use option 2 to add this city to your favorites!")
    else:
        # Error already displayed by fetch_weather
        last_searched = None


def add_to_favorites():
    """
    Add the last searched city to favorites.
    Checks if there's a city to add and if favorites aren't full,
    then adds the city.
    """
    global last_searched
    
    # Check if user has searched for a city
    if last_searched is None:
        show_error("No city to add. Please search for a city first (option 1).")
        return
    
    city_name = last_searched.get("city", "Unknown")
    
    # Check if already in favorites
    if is_favorite(city_name):
        show_info(f"'{city_name}' is already in your favorites.")
        return
    
    # Check if favorites is full
    if is_full():
        show_error(f"Favorites list is full ({favorites_count()}/3).")
        show_info("Remove a city first (option 4), then try again.")
        return
    
    # Add to favorites
    success, message = add_favorite(last_searched)
    
    if success:
        show_success(message)
        show_info(f"Favorites: {favorites_count()}/3")
    else:
        show_error(message)


def list_favorites():
    """
    List all favorite cities with current weather.
    Fetches fresh weather data for each favorite city and displays
    the updated information.
    """
    if is_empty():
        show_favorites_list([])
        return
    
    show_info("Fetching latest weather for your favorites...")
    
    # Get favorite names and fetch fresh weather for each
    favorite_names = get_favorite_names()
    updated_favorites = []
    
    for city_name in favorite_names:
        weather_data = fetch_weather(city_name)
        if weather_data:
            updated_favorites.append(weather_data)
            # Update stored data with fresh data
            add_favorite(weather_data)  # This will update existing entry
        else:
            # If fetch fails, we'll skip this city in display
            show_error(f"Could not fetch weather for '{city_name}'")
    
    # Display the favorites with updated weather
    show_favorites_list(updated_favorites)


def remove_from_favorites():
    """
    Remove a city from favorites.
    Displays numbered list of favorites and lets user select
    which one to remove.
    """
    if is_empty():
        show_info("Your favorites list is empty. Nothing to remove.")
        return
    
    # Get favorite names and display them
    favorite_names = get_favorite_names()
    show_favorites_for_removal(favorite_names)
    
    # Get user selection
    choice = get_user_input("Enter number to remove (or 0 to cancel): ")
    
    # Validate input
    if not choice:
        show_info("Cancelled.")
        return
    
    try:
        choice_num = int(choice)
    except ValueError:
        show_error("Invalid input. Please enter a number.")
        return
    
    # Handle cancel
    if choice_num == 0:
        show_info("Cancelled.")
        return
    
    # Validate range
    if choice_num < 1 or choice_num > len(favorite_names):
        show_error(f"Invalid choice. Please enter a number between 1 and {len(favorite_names)}.")
        return
    
    # Remove the selected city
    city_to_remove = favorite_names[choice_num - 1]
    success, message = remove_favorite(city_to_remove)
    
    if success:
        show_success(message)
        show_info(f"Favorites: {favorites_count()}/3")
    else:
        show_error(message)


def main():
    """
    Main application loop.
    
    Displays menu, handles user input, and routes to appropriate
    functions based on user choice.
    """
    
    print("  Welcome to Weather CLI!")
    print("  Get weather info for any city in the world.")
    
    while True:
        # Display menu
        show_menu()
        
        # Get user choice
        choice = get_menu_choice()
        
        # Route to appropriate function
        if choice == "1":
            search_city()
        
        elif choice == "2":
            add_to_favorites()
        
        elif choice == "3":
            list_favorites()
        
        elif choice == "4":
            remove_from_favorites()
        
        elif choice == "5":
            show_goodbye()
            break
        
        else:
            show_error("Invalid choice. Please enter a number between 1 and 5.")


# =============================================================================
# Entry Point
# =============================================================================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n")
        show_goodbye()
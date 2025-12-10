"""
Author: Tianchen Yu
Favorites Manager Module
maximum 3 cities
"""

from config import MAX_FAVORITES

_favorites = {}


def add_favorite(weather_data):
    """
    add a city to the favorites list
    
    :param weather_data: Description
    """
    if weather_data is None:
        return False
    
    city_name = weather_data.get("city", "")
    
    if not city_name:
        return False
    
    # enforce lower case
    city_key = city_name.lower()
    
    # Check if already in favorites
    if city_key in _favorites:
        return False, f"'{city_name}' is already in your favorites list"
    
    # Check if favorites list is full
    if is_full():
        return False, f"Favorites list is full (max {MAX_FAVORITES}). Remove one first. "
    
    # Add to favorites
    _favorites[city_key] = weather_data
    return True, f"'{city_name}' added to favorites"


def remove_favorite(city_name):
    """
    remove one from favorite list

    """
    city_key = city_name.lower()
    
    if city_key not in _favorites:
        return False, f"'{city_name}' is not in your favorites"
    
    
    original_name = _favorites[city_key].get("city", city_name)
    del _favorites[city_key]
    
    return True, f"'{original_name}' removed from favorites"


def get_all_favorites():
    """
    Get all favorite cities from favorite list.
    """
    return list(_favorites.values())


def get_favorite_names():
    """
    Get just the names of favorite cities.
    """
    return [data["city"] for data in _favorites.values()]


def is_favorite(city_name):
    """
    Check if a city is in the favorites list.
    """
    return city_name.lower() in _favorites


def favorites_count():
    """
    Get the number of cities in favorate list
    """
    return len(_favorites)


def is_full():
    """
    Check if the favorites list is at maximum capacity.
    """
    return len(_favorites) >= MAX_FAVORITES


def is_empty():
    """
    Check if the favorites list is empty.
    """
    return len(_favorites) == 0


def clear_all_favorites():
    """
    Remove all cities from favorites.
    """
    _favorites.clear()
    return True, "All favorites cleared"



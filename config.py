"""
Author: Tianchen Yu
This module contains api configuration and application constraints.
"""

API_KEY = "15e57ae86a966e72a4953ed5253e6578"

API_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

MAX_FAVORITES = 3

UNITS = "metric"

TEMP_UNIT = "°C" if UNITS == "metric" else "°F"
SPEED_UNIT = "m/s" if UNITS == "metric" else "mph"
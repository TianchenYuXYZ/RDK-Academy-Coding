# RDK-Academy-Coding
# Weather CLI Application

A command-line weather app using OpenWeather API.

## Quick Start

```bash
# Install dependency
pip install requests

# Add your API key in config.py (line 11)
# Get free key from: https://openweathermap.org/api

# Run
python main.py
```

## How to Use

### Option 1: Search Weather
```
Enter your choice (1-5): 1
Enter city name: Tokyo

Tokyo, JP                          
    Temperature:  22.5°C              
   Feels like:   21.8°C               
   Humidity:     65%                  
    Condition:    Clear sky           
   Wind speed:   3.2 m/s              


Tip: Use option 2 to add this city to your favorites!
```

### Option 2: Add to Favorites
```
Enter your choice (1-5): 2

'Tokyo' added to favorites
Favorites: 1/3
```

### Option 3: List Favorites
```
Enter your choice (1-5): 3


  Your Favorite Cities (2/3)


  1. Tokyo, JP
     22.5°C | Clear sky

  2. London, GB
     12.0°C | Overcast clouds


```

### Option 4: Remove from Favorites
```
Enter your choice (1-5): 4

--- Your Favorites ---
  1. Tokyo
  2. London
  0. Cancel

Enter number to remove (or 0 to cancel): 1

 'Tokyo' removed from favorites
```

### Option 5: Exit
```
Enter your choice (1-5): 5

=============================================
  Thank you for using Weather CLI! Goodbye! 👋
=============================================
```

## Notes

- Maximum 3 favorite cities allowed
- Weather data is fetched live from OpenWeather API
- New API keys may take 10-15 minutes to activate
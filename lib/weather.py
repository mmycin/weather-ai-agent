from typing import Final, Dict
import python_weather
from datetime import datetime, date
import logging
import sys

# Optional: Configure logging
logging.basicConfig(level=logging.ERROR)

async def getweather(location: str) -> Dict:
    try:
        async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
            weather = await client.get(location)

            weather_api: Final[Dict] = {
                "coordinates": {
                    "X": weather.coordinates[0],
                    "Y": weather.coordinates[1],
                },
                "country": weather.country,
                "datetime": weather.datetime.isoformat(timespec="minutes"),
                "description": weather.description,
                "feels_like": weather.feels_like,
                "humidity": weather.humidity,
                "kind": weather.kind.name if weather.kind else "UNKNOWN",
                "local_population": weather.local_population,
                "location": weather.location,
                "precipitation": weather.precipitation,
                "pressure": weather.pressure,
                "region": weather.region if weather.region else "Not Eligible",
                "temperature": round(5 * (weather.temperature - 32) / 9),  # F -> C
                "ultraviolet": weather.ultraviolet.name if weather.ultraviolet else "UNKNOWN",
                "visibility": weather.visibility,
                "wind_direction": weather.wind_direction.name if weather.wind_direction else "UNKNOWN",
                "wind_speed": weather.wind_speed
            }

            return weather_api

    except python_weather.Error as e:
        logging.error(f"Weather API error for location '{location}': {e}")
        sys.exit()
        return {"error": f"Weather data unavailable for '{location}'. Please try again later."}

    except Exception as e:
        logging.exception(f"Unexpected error occurred while fetching weather for '{location}':")
        sys.exit()
        return {"error": "An unexpected error occurred. Please contact support."}
 
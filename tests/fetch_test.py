import asyncio
import unittest
from unittest.mock import patch
import lib

class TestWeatherAPI(unittest.TestCase):

    @patch('lib.weather.python_weather')
    def test_getweather_success(self, mock_python_weather):
        mock_python_weather.AsyncClient.return_value.current.return_value = {
            'temperature': '25°C',
            'humidity': '60%',
            'description': 'Sunny'
        }
        location = "Dhaka"
        result = getweather(location)
        self.assertEqual(result['temperature'], '25°C')
        self.assertEqual(result['humidity'], '60%')
        self.assertEqual(result['description'], 'Sunny')

    @patch('lib.weather.python_weather')
    def test_getweather_error(self, mock_python_weather):
        mock_python_weather.AsyncClient.return_value.current.side_effect = Exception("Weather API error")
        location = "InvalidLocation"
        result = getweather(location)
        self.assertIn('error', result)
        self.assertEqual(result['error'], "Weather data unavailable for 'InvalidLocation'. Please try again later.")

if __name__ == '__main__':
    # unittest.main()
    ...
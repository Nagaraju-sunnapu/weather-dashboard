import os
from weather_scraper import get_weather

def test_get_weather_structure():
    data = get_weather("Hyderabad,IN", os.getenv("OPENWEATHER_API_KEY"))
    assert "main" in data
    assert "weather" in data
    assert isinstance(data["main"]["temp"], (int, float))

import requests
import os
from datetime import datetime

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Hyderabad"
COUNTRY = "IN"

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def format_report(data):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    report = f"""# Weather Report - {now}

**City**: {data['name']}, {data['sys']['country']}  
**Temperature**: {data['main']['temp']}°C  
**Feels Like**: {data['main']['feels_like']}°C  
**Condition**: {data['weather'][0]['description']}  
**Humidity**: {data['main']['humidity']}%  
**Wind Speed**: {data['wind']['speed']} m/s  
"""
    return report

def save_report(report):
    with open("daily_weather.md", "w") as f:
        f.write(report)

if __name__ == "__main__":
    data = get_weather(f"{CITY},{COUNTRY}", API_KEY)
    report = format_report(data)
    save_report(report)

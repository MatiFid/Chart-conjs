import requests
import json

def fetch_weather_data():
    # URL de la API de clima, asegúrate de reemplazar con la URL correcta y tu API key si es necesario
    api_url = "https://api.openweathermap.org/data/2.5/weather?q=villamaria&appid=7e26cca1376644e2b31b05ced59ae83c&units=metric"

    response = requests.get(api_url)
    data = response.json()

    weather_data = {
        "temperature": data['main']['temp'],
        "humidity": data['main']['humidity'],
        "pressure": data['main']['pressure'],
        "wind_speed": data['wind']['speed'],
        "apparent_temperature": data['main']['feels_like'],
        "cloud_coverage": data['clouds']['all'],
        "air_quality": data.get('air_quality', {}).get('aqi', 'N/A'),  # Ejemplo, ajustar según la API
        "uv_index": data.get('uvi', 'N/A')  # Ejemplo, ajustar según la API
    }

    # Guardar los datos en un archivo JSON
    with open('weather_data.json', 'w') as json_file:
        json.dump(weather_data, json_file, indent=4)

if __name__ == "__main__":
    fetch_weather_data()

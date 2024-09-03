import requests
import json

def fetch_weather_data():
    # URL de la API de Weatherbit, asegúrate de reemplazar con la URL correcta y tu API key
    api_url = "https://api.weatherbit.io/v2.0/current?city=Villa%20Maria&key=7e26cca1376644e2b31b05ced59ae83c&units=M"

    response = requests.get(api_url)
    data = response.json()

    # Accede a los datos desde la estructura devuelta por Weatherbit
    weather_data = {
        "temperature": data['data'][0]['temp'],
        "humidity": data['data'][0]['rh'],
        "pressure": data['data'][0]['pres'],
        "wind_speed": data['data'][0]['wind_spd'],
        "apparent_temperature": data['data'][0]['app_temp'],
        "cloud_coverage": data['data'][0]['clouds'],
        "air_quality": "N/A",  # Weatherbit no incluye datos de calidad del aire en este endpoint
        "uv_index": data['data'][0]['uv']
    }

    # Guardar los datos en un archivo JSON
    with open('weather_data.json', 'w') as json_file:
        json.dump(weather_data, json_file, indent=4)

if __name__ == "__main__":
    fetch_weather_data()

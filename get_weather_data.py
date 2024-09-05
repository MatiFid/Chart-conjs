import requests
import json
import os

def fetch_weather_data():
    api_key = "cc695bc08d3a4ff186dc02d18216540e"
    lat = "32.4072"  # Latitud de Villa Maria, por ejemplo
    lon = "-63.2403"  # Longitud de Villa Maria, por ejemplo
    
    weather_url = f"https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lon}&key={api_key}&units=M"
    air_quality_url = f"https://api.weatherbit.io/v2.0/airquality?lat={lat}&lon={lon}&key={api_key}"

    try:
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        print("Datos meteorológicos obtenidos con éxito.")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred during weather data request: {err}")
        return
    except Exception as err:
        print(f"An error occurred during weather data request: {err}")
        return

    try:
        air_quality_response = requests.get(air_quality_url)
        air_quality_response.raise_for_status()
        air_quality_data = air_quality_response.json()
        print("Datos de calidad del aire obtenidos con éxito.")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred during air quality data request: {err}")
        return
    except Exception as err:
        print(f"An error occurred during air quality data request: {err}")
        return

    current_weather = weather_data['data'][0]
    current_air_quality = air_quality_data['data'][0]

    # Comprobamos si las claves de calidad del aire están presentes antes de acceder a ellas
    combined_data = {
        "temperature": current_weather['temp'],
        "humidity": current_weather['rh'],
        "pressure": current_weather['pres'],
        "wind_speed": current_weather['wind_spd'],
        "apparent_temperature": current_weather['app_temp'],
        "cloud_coverage": current_weather['clouds'],
        "air_quality": {
            "pm10": current_air_quality.get('pm10', 'N/A'),
            "pm2_5": current_air_quality.get('pm2_5', 'N/A'),
            "o3": current_air_quality.get('o3', 'N/A'),
            "no2": current_air_quality.get('no2', 'N/A'),
            "so2": current_air_quality.get('so2', 'N/A'),
            "co": current_air_quality.get('co', 'N/A'),
        },
        "uv_index": current_weather.get('uv', 'N/A')
    }

    # Eliminar el archivo existente si es necesario
    if os.path.exists('weather_data.json'):
        os.remove('weather_data.json')
        print("Archivo JSON anterior eliminado.")

    # Guardar los datos en el archivo JSON
    with open('weather_data.json', 'w') as json_file:
        json.dump(combined_data, json_file, indent=4)
        print("Datos meteorológicos guardados exitosamente en weather_data.json.")

if __name__ == "__main__":
    fetch_weather_data()

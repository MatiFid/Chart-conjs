import requests
import json
import os

def fetch_weather_data():
    api_key = "cc695bc08d3a4ff186dc02d18216540e"
    lat = "32.4072"  # Latitud de Villa Maria, por ejemplo
    lon = "-63.2403"  # Longitud de Villa Maria, por ejemplo
    
    # URL para datos meteorológicos
    weather_url = f"https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lon}&key={api_key}&units=M"

    try:
        # Obtener los datos meteorológicos
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        print("Datos meteorológicos obtenidos con éxito.")
    except Exception as e:
        print(f"Error al obtener los datos: {e}")
        return

    current_weather = weather_data['data'][0]

    # Datos meteorológicos sin la calidad del aire
    combined_data = {
        "temperature": current_weather['temp'],
        "humidity": current_weather['rh'],
        "pressure": current_weather['pres'],
        "wind_speed": current_weather['wind_spd'],
        "apparent_temperature": current_weather['app_temp'],
        "cloud_coverage": current_weather['clouds'],
        "uv_index": current_weather['uv']
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

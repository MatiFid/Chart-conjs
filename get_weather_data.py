import requests
import json

def fetch_weather_data():
    # Define las URLs de los endpoints de la API de Weatherbit
    api_key = "7e26cca1376644e2b31b05ced59ae83c"
    city = "Villa Maria"
    
    # URL para datos meteorológicos actuales
    weather_url = f"https://api.weatherbit.io/v2.0/current?city={city}&key={api_key}&units=M"
    # URL para calidad del aire
    air_quality_url = f"https://api.weatherbit.io/v2.0/airquality?city={city}&key={api_key}"

    # Obtener datos meteorológicos actuales
    weather_response = requests.get(weather_url)
    weather_response.raise_for_status()  # Lanza un error si la solicitud no tiene éxito
    weather_data = weather_response.json()
    
    # Obtener datos de calidad del aire
    air_quality_response = requests.get(air_quality_url)
    air_quality_response.raise_for_status()  # Lanza un error si la solicitud no tiene éxito
    air_quality_data = air_quality_response.json()

    # Extraer datos necesarios
    current_weather = weather_data['data'][0]
    current_air_quality = air_quality_data['data'][0]

    # Preparar el diccionario con todos los datos
    combined_data = {
        "temperature": current_weather['temp'],
        "humidity": current_weather['rh'],
        "pressure": current_weather['pres'],
        "wind_speed": current_weather['wind_spd'],
        "apparent_temperature": current_weather['app_temp'],
        "cloud_coverage": current_weather['clouds'],
        "air_quality": {
            "pm10": current_air_quality['pm10'],
            "pm2_5": current_air_quality['pm2_5'],
            "o3": current_air_quality['o3'],
            "no2": current_air_quality['no2'],
            "so2": current_air_quality['so2'],
            "co": current_air_quality['co'],
        },
        "uv_index": current_weather.get('uv', 'N/A')  # Puede que el índice UV no esté disponible
    }

    # Guardar los datos en un archivo JSON
    with open('weather_data.json', 'w') as json_file:
        json.dump(combined_data, json_file, indent=4)

if __name__ == "__main__":
    fetch_weather_data()

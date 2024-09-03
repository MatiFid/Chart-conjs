import requests
import json

def fetch_weather_data():
    api_key = "7e26cca1376644e2b31b05ced59ae83c"
    city = "Villa Maria"
    
    weather_url = f"https://api.weatherbit.io/v2.0/current?city={city}&key={api_key}&units=M"
    air_quality_url = f"https://api.weatherbit.io/v2.0/airquality?city={city}&key={api_key}"

    try:
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()  # Lanza un error si la solicitud no tiene éxito
        weather_data = weather_response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred during weather data request: {err}")
        return
    except Exception as err:
        print(f"An error occurred during weather data request: {err}")
        return

    try:
        air_quality_response = requests.get(air_quality_url)
        air_quality_response.raise_for_status()  # Lanza un error si la solicitud no tiene éxito
        air_quality_data = air_quality_response.json()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred during air quality data request: {err}")
        return
    except Exception as err:
        print(f"An error occurred during air quality data request: {err}")
        return

    current_weather = weather_data['data'][0]
    current_air_quality = air_quality_data['data'][0]

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
        "uv_index": current_weather.get('uv', 'N/A')
    }

    with open('weather_data.json', 'w') as json_file:
        json.dump(combined_data, json_file, indent=4)

if __name__ == "__main__":
    fetch_weather_data()

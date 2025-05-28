import json

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Lista de cidades com coordenadas (latitude e longitude)
CITIES = [
    {"name": "Nueva York", "lat": 40.7128, "lon": -74.0060},
    {"name": "Londres", "lat": 51.5074, "lon": -0.1278},
    {"name": "Tokio", "lat": 35.6762, "lon": 139.6503},
    {"name": "París", "lat": 48.8566, "lon": 2.3522},
    {"name": "Sídney", "lat": -33.8688, "lon": 151.2093},
    {"name": "Madrid", "lat": 40.4168, "lon": -3.7038},
    {"name": "Berlín", "lat": 52.5200, "lon": 13.4050},
    {"name": "Roma", "lat": 41.9028, "lon": 12.4964},
    {"name": "Ciudad de México", "lat": 19.4326, "lon": -99.1332},
    {"name": "Buenos Aires", "lat": -34.6037, "lon": -58.3816},
    {"name": "Santiago", "lat": -33.4489, "lon": -70.6693},
    {"name": "Brasilia", "lat": -15.7801, "lon": -47.9292},
    {"name": "Caracas", "lat": 10.4812, "lon": -66.8602},
    {"name": "Montevideo", "lat": -34.9011, "lon": -56.1645},
    {"name": "Paysandu", "lat": -32.3171, "lon": -58.08072}
]


def get_data_meteo(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,precipitation,relativehumidity_2m,windspeed_10m",
        "timezone": "auto",
        "forecast_days": 7
    }
    try:
        response = requests.get(url, params=params)
        return response.json() if response.status_code == 200 else None
    except Exception as e:
        print("Error: ", e)
        return None


def get_user_location():
    try:
        response = requests.get("https://ipapi.co/json/")
        response.raise_for_status()
        data = response.json()
        return data['city'], data['country']
    except requests.exceptions.RequestException as e:
        print("Error fetching location:", e)
        return None, None


@app.route('/', methods=['GET', 'POST'])
def index():
    city, country = get_user_location()
    selected_city = {
        "name": "Não foi possível determinar a cidade", "lat": 0, "lon": 0}

    if request.method == 'POST':
        index = int(request.form['city'])
        selected_city = CITIES[index]

    if city:
        for city_info in CITIES:
            if city_info["name"].lower() == city.lower():
                selected_city = city_info
                break

    if selected_city["lat"] == 0 and selected_city["lon"] == 0:
        selected_city = CITIES[0]

    data = get_data_meteo(selected_city["lat"], selected_city["lon"])

    if data:
        hours = data['hourly']['time']
        temperatures = data['hourly']['temperature_2m']
        precipitation = data['hourly']['precipitation']
        humidity = data['hourly']['relativehumidity_2m']
        winds = data['hourly']['windspeed_10m']

        resume = {
            "temp_max": max(temperatures),
            "temp_min": min(temperatures),
            # Aqui é onde a precipitação total é calculada
            "precip_total": sum(precipitation),
            "winds_max": max(winds)
        }

        return render_template('index.html',
                               hours=json.dumps(hours),
                               temperatures=json.dumps(temperatures),
                               precipitation=json.dumps(precipitation),
                               humidity=json.dumps(humidity),
                               winds=json.dumps(winds),
                               resume=resume,
                               cities=CITIES,
                               indice_selecionado=CITIES.index(selected_city),
                               )
    else:
        return "Error obtaining weather data from API."


if __name__ == '__main__':
    app.run(debug=True)

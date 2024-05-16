import json
import requests
from flask import Flask, request, render_template
import pandas as pd

API_KEY = '0e69a1b7c0mshe62500cac8ddf7fp14b8e1jsn6fa2d436e748'
API_HOST = "weatherapi-com.p.rapidapi.com"
CURRENT_API_URL = "https://weatherapi-com.p.rapidapi.com/current.json"
FORECAST_API_URL = "https://weatherapi-com.p.rapidapi.com/forecast.json"

app = Flask(__name__)

def get_current_weather_data(location):
    url = CURRENT_API_URL
    querystring = {"q": location}
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }
    response = requests.get(url, headers=headers, params=querystring)
    return json.loads(response.text)

def get_forecast_weather_data(location):
    url = FORECAST_API_URL
    querystring = {"q": location}
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": API_HOST
    }
    response = requests.get(url, headers=headers, params=querystring)
    return json.loads(response.text)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_weather', methods=['POST'])
def predict_weather():
    if request.method == 'POST':
        location = request.form['location']
        try:
            current_weather_data = get_current_weather_data(location)
            forecast_weather_data = get_forecast_weather_data(location)

            # Process current weather data
            current_data = current_weather_data['current']
            name = current_weather_data['location']['name']
            region = current_weather_data['location']['region']
            country = current_weather_data['location']['country']
            lat = current_weather_data['location']['lat']
            lon = current_weather_data['location']['lon']
            tz_id = current_weather_data['location']['tz_id']
            localtime_epoch = current_weather_data['location']['localtime_epoch']
            localtime = current_weather_data['location']['localtime']
            last_updated_epoch = current_data['last_updated_epoch']
            last_updated = current_data['last_updated']
            temp_c = current_data['temp_c']
            temp_f = current_data['temp_f']
            is_day = current_data['is_day']
            condition_text = current_data['condition']['text']
            condition_icon = current_data['condition']['icon']
            wind_mph = current_data['wind_mph']
            wind_kph = current_data['wind_kph']
            wind_degree = current_data['wind_degree']
            wind_dir = current_data['wind_dir']
            pressure_mb = current_data['pressure_mb']
            pressure_in = current_data['pressure_in']
            precip_mm = current_data['precip_mm']
            precip_in = current_data['precip_in']
            humidity = current_data['humidity']
            cloud = current_data['cloud']
            feelslike_c = current_data['feelslike_c']
            feelslike_f = current_data['feelslike_f']
            vis_km = current_data['vis_km']
            vis_miles = current_data['vis_miles']
            uv = current_data['uv']
            gust_mph = current_data['gust_mph']
            gust_kph = current_data['gust_kph']

            # Process forecast weather data
            forecast_data = forecast_weather_data['forecast']['forecastday']
            forecast_dates = []
            forecast_conditions = []
            for forecast_day in forecast_data:
                forecast_dates.append(forecast_day['date'])
                forecast_conditions.append(forecast_day['day']['condition']['text'])

            return render_template('home.html', name=name, region=region, country=country, lat=lat, lon=lon,
                                   tz_id=tz_id, localtime_epoch=localtime_epoch, localtime=localtime,
                                   last_updated_epoch=last_updated_epoch, last_updated=last_updated, temp_c=temp_c,
                                   temp_f=temp_f, is_day=is_day, condition_text=condition_text,
                                   condition_icon=condition_icon, wind_mph=wind_mph, wind_kph=wind_kph,
                                   wind_degree=wind_degree, wind_dir=wind_dir, pressure_mb=pressure_mb,
                                   pressure_in=pressure_in, precip_mm=precip_mm, precip_in=precip_in,
                                   humidity=humidity, cloud=cloud, feelslike_c=feelslike_c, feelslike_f=feelslike_f,
                                   vis_km=vis_km, vis_miles=vis_miles, uv=uv, gust_mph=gust_mph, gust_kph=gust_kph,
                                   forecast_dates=forecast_dates, forecast_conditions=forecast_conditions)

        except Exception as e:
            print(e)
            return render_template('home.html', error='Please enter a correct Place name...')


if __name__ == '__main__':
    app.run(debug=True)

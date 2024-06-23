from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_data(city_name):
    api_key = '9b63303a6de581d6c6f2c9edaca25796'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    description = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 1)
    feels_like = round(data['main']['feels_like'] - 273.15, 1)
    country = data['sys']['country']
    return description, temperature, feels_like, country

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def weather():
    city_name = request.form['city_name']
    description, temperature, feels_like, country = get_data(city_name)
    return render_template('weather.html', city_name=city_name,
                           description=description, temperature=temperature,
                           feels_like=feels_like, country=country)

if __name__ == '__main__':
    app.run(debug=True)
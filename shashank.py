from flask import Flask, request, jsonify
import requests

app = Flask(_name_)

# OpenWeatherMap API key
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/weather', methods=['GET'])
def get_weather():
    # Get location from query parameters
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is missing'}), 400

    # Make request to OpenWeatherMap API
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        # Extract relevant information
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        result = {'city': city, 'temperature': temperature, 'description': description}
        return jsonify(result)
    else:
        return jsonify({'error': 'Failed to fetch weather data'}), 500

if _name_ == '_main_':
    app.run(debug=True)
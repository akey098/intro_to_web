# Example 1: Consuming a Public API with Python (Cryptocurrency API)
# This example demonstrates how to fetch data from a public API to get the current price of Bitcoin.

import requests


def fetch_crypto_data():
    api_url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        print("Bitcoin price (USD):", data['bpi']['USD']['rate'])
    else:
        print("Failed to retrieve data")


# Call the function to fetch cryptocurrency data
fetch_crypto_data()

# Example 2: Exposing an API using Flask (Weather API Concept)
# This conceptual overview demonstrates how to create a simple weather API with Flask.

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if city == "New York":
        weather = {"city": "New York", "temperature": "10°C"}
        return jsonify(weather)
    else:
        return jsonify({"error": "City not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)


# Example 3: Breaking Down a URL (Explanation)
# This example demonstrates how to break down and explain the parts of a URL.

def breakdown_url():
    url = "https://www.example.com:8080/path/to/resource?query=python&sort=asc#section2"

    print("URL Breakdown:")
    print("Protocol:", url.split(":")[0])  # 'https'
    print("Domain:", url.split("/")[2])  # 'www.example.com'
    print("Port:", url.split(":")[2].split("/")[0])  # '8080'
    print("Path:", "/" + "/".join(url.split("/")[3:5]))  # '/path/to/resource'
    print("Query:", url.split("?")[1].split("#")[0])  # 'query=python&sort=asc'
    print("Fragment:", url.split("#")[-1])  # 'section2'


# Call the function to break down the URL
breakdown_url()


# Example 4: Using an API to Fetch Weather Data (Weather API Example)
# This example uses a public weather API to fetch data based on a city name.

def fetch_weather_data():
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "London",
        "appid": "YOUR_API_KEY",  # Replace with your actual API key
        "units": "metric"
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"Weather in London: {data['weather'][0]['description']}, {data['main']['temp']}°C")
    else:
        print("Failed to retrieve weather data")


# Call the function to fetch weather data
fetch_weather_data()

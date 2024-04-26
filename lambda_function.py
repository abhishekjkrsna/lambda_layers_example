import json
import requests

def get_weather():
    
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    querystring = {
        "lat": "26.51",
        "lon": "80.57",
        "appid": "YOUR_API_KEY"
    }
    
    response = requests.request("GET", url, params=querystring)
    return response.text

def lambda_handler(event, context):
    # TODO implement
    
    output = get_weather()
    
    return {
        'statusCode': 200,
        'body': output
    }
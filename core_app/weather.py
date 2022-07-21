import requests
from uuid import uuid4
from datetime import datetime



def get_weather(id):
    SECRET_KEY_WEATHER = 'b7d36578df7f812139888df2794905c4'
    city_ids = [3439525, 3439781, 3440645]
    data_city = list()

    try:
        url = 'https://api.openweathermap.org/data/2.5/weather?'
        
        for city_id in city_ids:
            params = {"id": city_id, "appid": SECRET_KEY_WEATHER}
        
            response = requests.get(url, params=params)
            status = response.status_code
        
            if  status == 200:
                weather = response.json()['main']
                temperature = weather['temp']
                humidity = weather["humidity"]
                resp = {
                    "user_id": id,
                    "city_id": city_id,
                    "temperature": temperature,
                    "humidity": humidity,
                    "request_id": uuid4().hex,
                    "now": datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
                }
                data_city.append(resp)
        
        print(data_city)
        
        # return response.json()
        
    
    except Exception as exc:
        print(exc)
        return 500
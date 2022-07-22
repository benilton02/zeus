
from core_app.models import Weather
import aiohttp
import asyncio
from asgiref.sync import sync_to_async
from django.utils import timezone


SECRET_KEY_WEATHER = 'b7d36578df7f812139888df2794905c4'
city_ids = [3439525, 3439781, 3440645]
url = 'http://api.openweathermap.org/data/2.5/weather?id={}&appid={}'
results = []

async def get_weather(user_id):
    async with aiohttp.ClientSession() as session:
        for city_id in city_ids:
            response = await session.get(url.format(city_id, SECRET_KEY_WEATHER))
        
            results.append(await response.json())      

    for result in results:
        weather = result['main']
        id = result['id']

        data = {
            'user_id': user_id,
            'city_id': id,
            'temperature': weather['temp'],
            'humidity': weather['humidity'],
            'request_time': timezone.now()
            
        }
       
        await create_weather(data)


def weather_async(user_id):
    asyncio.run(get_weather(user_id))


@sync_to_async
def create_weather(data):
    Weather.objects.create(**data)


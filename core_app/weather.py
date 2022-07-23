
from core_app.models import Weather
import aiohttp
import asyncio
from asgiref.sync import sync_to_async
from django.utils import timezone
from time import sleep
from core_app.set_city_id import city_ids
from decouple import config


url = config('URL_WEATHER')
secret_key_weather = config('SECRET_KEY_WEATHER')


async def get_weather(user_id):
    results = []
   
    async with aiohttp.ClientSession() as session:
    
        for city_id in city_ids:

            try: 
                response = await session.get(url.format(city_id, secret_key_weather))
                respose_json = await response.json()
                weather = respose_json['main']

                data = {
                    'user_id': user_id,
                    'city_id': city_id,
                    'temperature': weather['temp'],
                    'humidity': weather['humidity'],
                    'request_time': timezone.now()
                }

                print("\n", data)
                print("\nsleep in 1.20 sec..\n")
               
                await create_weather(data)
                await asyncio.sleep(1.2)
                
                print("Awake!")
            
            except Exception as e:
                print(e)




def weather_async(user_id):
    asyncio.run(get_weather(user_id))


@sync_to_async
def create_weather(data):
    Weather.objects.create(**data)
        


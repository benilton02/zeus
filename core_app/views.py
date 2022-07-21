from webbrowser import get
from django.http import JsonResponse
from rest_framework.decorators import api_view
from core_app.models import Weather
from core_app.weather import get_weather
import threading

@api_view(['POST'])
def save_weather(request, id):
    
    # data = {
    #     "user_id": id,
    #     "request_id": uuid4().hex,
    #     "city_id": "city_id",
    #     "temperature": 0.0,
    #     "humidity": 0.0,
    #     "now": datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    # }
    
    thread_weather = threading.Thread(target=get_weather, args=(id,))
    thread_weather.start()

    # weather = Weather.objects.create(**data)

    # reponse = {
    #     "user_id": weather.user_id,
    #     "request_id": weather.request_id,
    #     "city_id": weather.city_id,
    #     "temperature": weather.temperature,
    #     "humidity": weather.humidity,
    #     "now": weather.now,
    # }

    return JsonResponse(dict(), status=200)
    ...

    
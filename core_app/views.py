from django.http import JsonResponse
from rest_framework.decorators import api_view
from core_app.models import Weather
# from core_app.weather import Weather as W
from core_app.weather import weather_async
import threading

@api_view(['POST'])
def save_weather(request, user_id):
    weather_async(user_id)
    return JsonResponse(dict(), status=200)
    

@api_view(['GEt'])
def report_weather(request):

    return JsonResponse(dict(), status=200)
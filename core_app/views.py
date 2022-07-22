from django.http import JsonResponse
from rest_framework.decorators import api_view
from core_app.models import Weather
from core_app.weather import weather_async

@api_view(['POST'])
def save_weather(request, user_id):
    try:
        queryset = Weather.objects.filter(user_id=user_id)

    except:
        data = {
            'message': "check database",
        }
        JsonResponse(data, status=404)

    if queryset:
        data = {
            'message': "user_id already exists",
        }
        return JsonResponse(data, status=400)
    
    weather_async(user_id)
    data = {"message":"collecting data"}
    return JsonResponse(data, status=200)
    

@api_view(['GET'])
def report_weather(request):
    return JsonResponse(dict(), status=200)
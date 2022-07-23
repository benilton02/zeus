from django.http import JsonResponse
from rest_framework.decorators import api_view
from core_app.models import Weather
from core_app.weather import weather_async
from asgiref.sync import sync_to_async
from core_app.set_city_id import city_ids



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
    
    try: 
        weather_async(user_id)
        data = {"message":"collecting data"}
        return JsonResponse(data, status=200)
    
    except Exception as e:
        print(e)
        return JsonResponse(dict(), status=200)
    

@api_view(['GET'])
def report_weather(request, user_id):
    queryset = Weather.objects.filter(user_id=user_id)

    if queryset:
        num  = queryset.all().count()
        
        den = len(city_ids)
        progress = float(num / den)
        progress *= 100

        data = {
            "user_id": user_id,
            "progress":"{:.2f}%".format(progress)
            }

        status = 200 
    
    else:
        data = {
            "message": "user_id not found"
        }
        status = 404 
    
    return JsonResponse(data=data, status=status)





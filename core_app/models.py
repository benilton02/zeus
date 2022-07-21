from django.db import models


class Weather(models.Model):

    user_id = models.CharField(max_length=50, blank=False, null=False) 
    request_id = models.CharField(max_length=255, blank=False, null=False) 
    city_id = models.CharField(max_length=255, blank=False, null=False) 
    temperature = models.FloatField(blank=False, null=False) 
    humidity = models.FloatField(blank=False, null=False) 
    now = models.DateTimeField(blank=False, null=False)

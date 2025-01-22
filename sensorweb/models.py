from django.db import models

# Create your models here.

# Create your models here.
class sensors(models.Model):
    type = models.CharField(max_length=20)
    time = models.DateTimeField()
    location = models.CharField(max_length=20)
    temp_left = models.FloatField()
    temp_right = models.FloatField()
    load_left = models.IntegerField()
    load_right = models.IntegerField()
    vocs = models.IntegerField()
    vocs_temp = models.FloatField()
    vocs_hum = models.IntegerField()



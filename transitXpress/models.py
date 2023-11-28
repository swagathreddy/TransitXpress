from django.db import models
from django.contrib.auth.models import User
# Create your models here.

    
class Feature(models.Model):
    
    fromdesti = models.CharField(max_length=100)
    todesti = models.CharField(max_length=500)
    
    
    def __str__(self):
        return self.fromdesti + ' TO ' + self.todesti
    
class Conformation(models.Model):
    # user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    # bus_number = models.CharField(max_length=50)
    # route = models.ForeignKey('transitXpress_feature', on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    from_location = models.CharField(max_length=255,null=True,blank=True)
    to_location = models.CharField(max_length=255,null=True, blank=True)
    passenger_name = models.CharField(max_length=100)
    email = models.EmailField()
    payment_mode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.passenger_name}'s Booking"

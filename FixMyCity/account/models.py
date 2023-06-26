from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Problems(models.Model):
    type = models.CharField(max_length=255 , blank=True)
    def __str__(self):
        return self.type 
    
    
class alert(models.Model):
    problem = models.ForeignKey('Problems', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
    map = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media', blank=True)
    
    

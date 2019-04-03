from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    photo=models.ImageField(upload_to='images/',default='images/avatar.jpg')
    bio=models.TextField()
    # user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    phone_number=models.IntegerField(null=True)
    
class Business(models.Model):
     name=models.CharField(max_length=100,null=True)
     location=models.CharField(max_length=200,null=True)
     neigborhood=models.OneToOneField(Neigborhood,null=True)
    #  user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
     email = models.EmailField()
     
     
# Create your models here.

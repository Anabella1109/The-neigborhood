from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Neighborhood(models.Model):
     name = models.CharField(max_length=100, null=True)
     location = models.CharField(max_length=100, null=True)
     occupants=models.IntegerField()

     def __str__(self):
        return self.name
     @classmethod
     def create_neighborhood(cls,name,loc,occupants):
        neighborhood=Neighborhood(name=name,location=loc,occupants=occupants)
        return neighborhood
     
     @classmethod
     def find_neighborhood(cls,id):
        neighborhood=cls.objects.get(id=id)
        return neighborhood

     def save_neighborhood(self):
         self.save()

     def delete_neighborhood(self):
        self.delete()

     def update_neighborhood(self,bio):
         self.name=bio
         self.save()

     def update_occupants(self,num):
         self.occupants=num
         self.save()

# class User(models.Model):
#     full_name=models.CharField(max_length=150,null=True)
#     username=models.CharField(max_length=100,null=True)
#     email = models.EmailField()
#     password=models.CharField(max_length=50)
#     neighborhood=models.ForeignKey(Neighborhood)

class Profile(models.Model):
    photo=models.ImageField(upload_to='images/',default='images/avatar.jpg')
    bio=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    first_name=models.CharField(max_length=100,null=True)
    last_name=models.CharField(max_length=100,null=True)
    location= models.CharField(max_length=100,null=True)
    phone_number=models.IntegerField(null=True)
    neighborhood=models.OneToOneField(Neighborhood,null=True)
    

    def __str__(self):
        return self.first_name

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    
class Business(models.Model):
     name=models.CharField(max_length=100,null=True)
     location=models.CharField(max_length=200,null=True)
     neighborhood=models.ForeignKey(Neighborhood,null=True)
     user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
     email = models.EmailField()
     phone_number=models.IntegerField(null=True)

     def __str__(self):
        return self.name

     @classmethod
     def create_business(cls,name,loc,neib,email,phone):
        business=Business(name=name,location=loc,neighborhood=neib,email=email,phone_number=phone)
        return business

class Health(models.Model):
    name=models.CharField(max_length=100,null=True)
    location=models.CharField(max_length=200,null=True)
    neighborhood=models.OneToOneField(Neighborhood,null=True)
    phone_number=models.IntegerField(null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Police(models.Model):
    name=models.CharField(max_length=100,null=True)
    location=models.CharField(max_length=200,null=True)
    neighborhood=models.OneToOneField(Neighborhood,null=True)
    phone_number=models.IntegerField(null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to = 'images/')
    caption=HTMLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    profile=models.ForeignKey(Profile, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title


     

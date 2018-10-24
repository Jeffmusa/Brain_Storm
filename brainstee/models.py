from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    pro_photo = models.ImageField(upload_to = 'images/',null=True)
    name = models.CharField(max_length =30,null=True)
    location = models.CharField(max_length =30,null=True)
    email = models.EmailField(max_length =50,null=True)
    bio = models.CharField(max_length =150,default='Hi, I have an idea')
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)
    
    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()
        

    def delete_profile(self):
        self.delete()
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    pro_photo = models.ImageField(upload_to = 'images/',blank=True)
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


class Seek(models.Model):
    what_do_you_do = models.TextField(max_length =130,null=True)
    which_skills_do_you_have = models.CharField(max_length =130,null=True)
    seek_help = models.CharField(max_length =130,null=True)
    user = models.ForeignKey(User, null=True)
    

class Help(models.Model):
    helpout = models.CharField(max_length =130,null=True)
    user = models.ForeignKey(User, null=True)
    seek = models.ForeignKey(Seek,related_name='help',null=True)


class Idea(models.Model):
    idea = models.CharField(max_length =130,null=True)
    user = models.ForeignKey(User, null=True)
    
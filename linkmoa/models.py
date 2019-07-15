from django.db import models
from django.contrib.auth.models import User  
from django.db.models.signals import post_save
from django.forms.models import model_to_dict
from django.dispatch import receiver
import urllib.request
from django import template

register = template.Library()

# Create your models here.
class Memo(models.Model):
    user_id = models.IntegerField()
    owner = models.CharField(max_length=20, default="???")
    directory = models.CharField(max_length=20, default="recently")
    display = models.CharField(max_length=10, default="visible")
    shared = models.BooleanField(default=False)
    download = models.IntegerField(default=0)
    keyword = models.CharField(max_length=30)
    urls = models.TextField(default=None)
    memo = models.TextField(default="")

    def __str__(self):
        return self.keyword
    
    def split(urls):
        urlList = urls.split('\n')
        return urlList

    def increaseDL(self):
        self.download+=1
        self.save()


class Profile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    numofDir = models.IntegerField(default=0)
    selectedMemo = models.IntegerField(default=0)
    dir1 = models.CharField(max_length=30, blank=True)
    dir2 = models.CharField(max_length=30, blank=True)
    dir3 = models.CharField(max_length=30, blank=True)
    dir4 = models.CharField(max_length=30, blank=True)
    dir5 = models.CharField(max_length=30, blank=True)
    dir6 = models.CharField(max_length=30, blank=True)
    dir7 = models.CharField(max_length=30, blank=True)
    dir8 = models.CharField(max_length=30, blank=True)
    dir9 = models.CharField(max_length=30, blank=True)
    dir10 = models.CharField(max_length=30, blank=True)

    def setSelectedMemo(id):
        self.selectedMemo=id
        self.save()

    def increase(self):
        self.numofDir+=1
        self.save()

    def decrease(self):
        self.numofDir-=1
        self.save()

    def get_fields_name(model):
        names=[]
        for key in model_to_dict(model).values():
            if type(key) == str and key !='':
                names.append(key)
        return names



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):  
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):  
    instance.profile.save()
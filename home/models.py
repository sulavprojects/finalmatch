from django.db import models

# Create your models here.
from distutils.command.upload import upload
from django.db import models
from email.policy import default
from sqlite3 import Timestamp
from pyexpat import model
from turtle import title
from .helpers import *

from froala_editor.fields import FroalaField

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return 'message from -' + self.name + ' - ' + self.email 

class Pages(models.Model):
    aboutus = FroalaField()
    privacypolicy = FroalaField()
    termsandcondition = FroalaField()
    ourpages = FroalaField()
    
class Modification(models.Model):
    websitename = models.CharField(max_length=50)
    ouremail = models.EmailField()
    copyright = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='websiteimages')
    websitediscription = FroalaField()
    favicon = models.ImageField(default='AF')


class Fonts(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=1000 , null=True , blank=True)
    metkeyword = models.CharField(max_length=200, null=True)
    header_image = models.ImageField(upload_to='headerimage')
    upload_fonts = models.FileField(upload_to="media" , null=True)
    short_discription = models.CharField(max_length=255)
    long_discription = FroalaField()
    character_map_img = models.ImageField(upload_to='characterimage')
    publish = models.BooleanField(default=False, null=True)
    Total_downloads = models.PositiveIntegerField(default=0, blank=False, null= False)

    def increment_Total_download(self):
            self.Total_downloads += 1   
    


    def __str__(self):
        return self.title

    def save(self , *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Fonts, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/{self.slug}'
from django.db import models

# Create your models here.

class Image(models.Model):
    picture = models.ImageField(upload_to="upload")
    date = models.DateTimeField(auto_now_add=True)
from django.contrib import admin
from .models import Image

# Register your models here.

@admin.register(Image)
class admin(admin.ModelAdmin):
    list_display = ['id', 'picture', 'date']
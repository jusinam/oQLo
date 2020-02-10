from django.contrib import admin
from .models import Image, Comment, Profile

# Register your models here.
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Profile)
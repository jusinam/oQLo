from django.db import models
import datetime as dt
from tinymce.models import HTMLField
from PIL import Image

# Create your models here.
         
class Image(models.Model):
    image_name = models.CharField(max_length=255)
    image_file = models.ImageField(upload_to = 'images/', default='images/qlo.jpg')
    caption = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()
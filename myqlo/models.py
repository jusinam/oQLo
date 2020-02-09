from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to = 'profiles/', blank=True, default='profiles/qlo.jpg')

    def save_profile(self):
        self.save()
        
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return f'self.user, self.bio, self.photo'
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


         
class Image(models.Model):
    image_name = models.CharField(max_length=255)
    image_file = models.ImageField(upload_to = 'images/', default='images/qlo.jpg')
    caption = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    author_profile = models.ForeignKey(Profile,on_delete=models.CASCADE, blank=True, default='1')
    likes = models.ManyToManyField(User, related_name = 'likes', blank = True)



    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
        
    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images
    
    @classmethod
    def get_by_author(cls, Author):
        images = cls.objects.filter(Author=Author)
        return images
    
    def total_likes(self):
        self.likes.count()

    @classmethod
    def search_images(cls, search_term):
        images = cls.objects.filter(description__icontains=search_term)
        return images
    
    @classmethod
    def get_image(request, id):
        try:
            image = Image.objects.get(pk = id)
            print(image)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return image
    
    def __str__(self):
        return self.image_name
    
    class Meta:
        ordering = ['pub_date']
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
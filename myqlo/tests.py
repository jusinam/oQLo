from django.test import TestCase
from .models import Image

# Create your tests here.

class ImageTestCase(TestCase):
    
    def setUp(self):
        
        # Set up method
        self.new_image= Image(image_name = 'Qlo', image_file ='media/images/qlo.jpg', caption ='QLo is a chatting app')
       

     # Testing  instance
    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    # Testing  saveinf
    def test_save_method(self):
        self.new_image.save_image()
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects)>0)
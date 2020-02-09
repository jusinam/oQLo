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
from django.shortcuts import render
import datetime as dt
from .models import Image
from django.http import HttpResponse, Http404



# Create your views here.
def home(request):
    date = dt.date.today()
    images = Image.get_images()
   

    return render(request, 'index.html', {"date": date, "images":images})
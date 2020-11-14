from django.shortcuts import render
from .models import Image,Location

# Create your views here.
def pictures(request):
    pics = Image.objects.all()
    locations = Location.objects.all()
    return render(request,'photos.html',{'pics':pics,'locations':locations})

def locations(request,location):
    locations = Image.filterimageByLocation(location)
    return render(request,'locations.html',{'locations':locations})
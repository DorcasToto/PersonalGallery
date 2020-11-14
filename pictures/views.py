from django.shortcuts import render
from .models import Image

# Create your views here.
def pictures(request):
    pics = Image.objects.all()
    return render(request,'photos.html',{'pics':pics})
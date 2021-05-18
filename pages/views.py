from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html",{})

def calendar_view(request, *args, ** kwargs):
    return render(request, "calendar.html",{})

def resources_view(request, *args, ** kwargs):
    return render(request,"resources.html",{})
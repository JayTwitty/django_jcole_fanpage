from django.shortcuts import render, render_to_response
from jcole_app.models import Jcole

# Create your views here.

def index_views(request):
    return render_to_response("index.html",{})


def aboutme_views(request):
    return render_to_response("aboutme.html",{})


def concerts_views(request):
    all_concerts = Jcole.objects.all()
    return render_to_response("concerts.html",{'concerts': all_concerts})




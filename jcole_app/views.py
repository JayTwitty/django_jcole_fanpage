from django.shortcuts import render, render_to_response


# Create your views here.

def index_views(request):
    return render_to_response("index.html",{})


def aboutme_views(request):
    return render_to_response("aboutme.html",{})


def concerts_views(request):
    return render_to_response("concerts.html",{})
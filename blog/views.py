from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def intro_blog(request):
    return HttpResponse("Hey, Blog!")
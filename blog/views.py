from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    context = {
            'posts': Post.objects.all(),
            'title': 'Blog posts',
        }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


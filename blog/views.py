from django.shortcuts import render
from django.http import HttpResponse

# Dummy var
posts = [
    {
        'author': 'yangzi33',
        'title': 'Dummy blog post',
        'content': 'owo',
        'date_posted': 'Right now',
    }
]

def home(request):
    context = {
            'posts': posts,
            'title': 'Blog posts',
        }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


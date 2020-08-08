from django.shortcuts import render
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView)


def home(request):
    context = {
            'posts': Post.objects.all(),
            'title': 'Blog posts',
        }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    # blog/post_list.html
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    """ With respect to template blog/post/<int:pk>.html
    """
    model = Post
    

class PostCreateView(LoginRequiredMixin, CreateView):
    """ With respect to template blog/post_list.html
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """To prevent NOT NULL contraint of author_id
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Post editing view
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """To prevent NOT NULL contraint of author_id
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Check if the user is the author of the post
        """
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Post deleting view
    """
    model = Post
    # Homepage redirect
    success_url = '/'

    def test_func(self):
        """Check if the user is the author of the post
        """
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


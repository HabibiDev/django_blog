from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post


# Create your views here.

class PostView(ListView):

    model = Post
    template_name = 'post/list_of_posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

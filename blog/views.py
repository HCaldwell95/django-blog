from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
        model = Post

def blog(request):
    # Your view logic here
    return render(request, 'blog/blog.html')
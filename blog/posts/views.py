from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    model = Post

    template_name = 'posts/post_list.html'
    context_object_name = "object_list"
    paginate_by = 1  # and that's it !!

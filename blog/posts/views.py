from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    model = Post

    template_name = 'posts/post_list.html'
    context_object_name = "object_list"
    paginate_by = 3

    def get_queryset(self):

        queryset = super(PostListView, self).get_queryset()

        search_query = self.request.GET.get("q")
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(summary__icontains=search_query)
            ).distinct()

        sort_query = self.request.GET.get("sort")
        if sort_query == "most_visited":
            queryset = queryset.order_by("-visit_count")
        elif sort_query == "latest":
            queryset = queryset.order_by("-created")

        return queryset

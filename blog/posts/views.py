from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView

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


class PostDetailView(DetailView):
    model = Post

    template_name = 'posts/post_detail.html'
    context_object_name = "post"

    def get(self, request, **kwargs):
        self.object = self.get_object()
        self.object.visit_count = self.object.visit_count + 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class PostCreateView(CreateView):
    model = Post

    fields = ['title', 'summary', 'description', 'image', 'category']
    template_name = 'posts/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['view_type'] = "New Post"
        return context

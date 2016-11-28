from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import (CreateView, DeleteView)

from comments.models import Comment


class CommentCreateView(CreateView):

    pass


class CommentDeleteView(DeleteView):

    model = Comment
    success_url = reverse_lazy('comments:comment-create')

    def post(self, request, *args, **kwargs):

        try:
            id = request.POST['id']
            self.object = Comment.objects.get(id=id)
            if (self.object.user.id == request.user.id):
                self.object.delete()
                data = {"success": "1",
                        "count": Comment.objects.count()}
            else:
                data = {"success": "0"}
        except:
            data = {"success": "0"}
        if request.is_ajax():
            return JsonResponse(data)
        else:
            return HttpResponseRedirect(self.success_url)

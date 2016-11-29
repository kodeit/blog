from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.middleware.csrf import get_token
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from django.views.generic import (CreateView, DeleteView)

from comments.models import Comment
from comments.forms import CommentForm

class AjaxableResponseMixin(object):


    def form_invalid(self, form):

        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse({
                'success': 0,
                'error': form.errors})
        else:
            return response

    def form_valid(self, form):

        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            csrf_token_value = get_token(self.request)
            html = render_to_string(
                "comments/comment.html",
                {'object': self.object,
                 'user': self.request.user,
                 'csrf_token': csrf_token_value,
                 })
            try:
                data = {
                    'success': 1,
                    'html': html,
                    'id': self.object.id
                }
            except:
                data = {
                    'success': 1,
                }
            return JsonResponse(data)
        else:
            return response


class CommentCreateView(AjaxableResponseMixin, CreateView):

    form_class = CommentForm
    model = Comment
    template_name = 'comments/comment_form.html'
    success_url = reverse_lazy('comments:comment-create')

    def form_valid(self, form):
        comment = form.save(commit=False)
        try:
            app_name = self.request.POST['app_name']
            model = self.request.POST['model'].lower()
            model_id = self.request.POST['model_id'].lower()

            content_type = ContentType.objects.get(
                           app_label=app_name,
                           model=model)

            model_obj = content_type.get_object_for_this_type(id=model_id)

            comment.content_object = model_obj
        except:
            # Just save comment
            pass
        comment.save()
        return super(CommentCreateView, self).form_valid(form)


class CommentDeleteView(DeleteView):

    model = Comment
    success_url = reverse_lazy('comments:comment-create')

    def post(self, request, *args, **kwargs):

        try:
            id = request.POST['id']
            self.object = Comment.objects.get(id=id)

            if (self.object.user.id == request.user.id):
                self.object.delete()
                model_obj = self.object.content_object
                count = model_obj.comments.count()
                data = {
                        "success": "1",
                        "count": count
                       }
            else:
                data = {"success": "0"}
        except:
            data = {"success": "0"}

        if request.is_ajax():
            return JsonResponse(data)
        else:
            return HttpResponseRedirect(self.success_url)

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('content_type', 'object_id', 'content_object')

        widgets = {
           'comment': forms.Textarea(attrs={'cols': 78, 'rows': 6}),
        }

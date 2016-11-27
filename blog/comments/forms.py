from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        exclude = ('content_type', 'object_id',
                   'content_object')

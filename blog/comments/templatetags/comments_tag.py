from django import template

from comments.forms import CommentForm

register = template.Library()


@register.simple_tag(name='get_model_name')
def get_model_name(object):
    return type(object).__name__


@register.simple_tag(name='get_app_name')
def get_app_name(object):
    return type(object)._meta.app_label


def get_comments(object, user):

    model_object = type(object).objects.get(id=object.id)

    ''' Fetch all comments related to a post
    '''
    comments = model_object.comments.all()
    print("Hi", comments.count())
    return {"form": CommentForm(),
            "comments": comments,
            "target": object,
            "user": user,
            "comments_count": comments.count()
           }

register.inclusion_tag('comments/comments.html')(get_comments)


def comment_form(object, user):

     return {"form": CommentForm(),
            "target": object,
            "user": user
            }

register.inclusion_tag('comments/comment_form.html')(comment_form)

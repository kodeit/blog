from django import template

from comments.forms import CommentForm

register = template.Library()

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


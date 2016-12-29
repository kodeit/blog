from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class Comment(models.Model):

    user = models.ForeignKey(User, null=True, blank=True)
    comment = models.CharField(max_length=512)

    created = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ["-created"]



from django.utils.text import slugify


def upload_location(instance, filename):
    post_model = instance.__class__
    try:
        new_id = post_model.objects.order_by("id").last().id + 1
    except AttributeError:
        new_id = 1
    return "%s/%s" % (new_id, filename)


def create_slug(instance, new_slug=None):
    post_model = instance.__class__
    slug = slugify(instance.title)

    if new_slug is not None:
        slug = new_slug

    qs = post_model.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

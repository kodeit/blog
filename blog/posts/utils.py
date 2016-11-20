def upload_location(instance, filename):
    post_model = instance.__class__
    print("saving catogory")
    print(post_model.objects.all())
    try:
        new_id = post_model.objects.order_by("id").last().id + 1
    except AttributeError:
        new_id = 1
    return "%s/%s" % (new_id, filename)

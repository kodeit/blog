from collections import defaultdict

from django.core.cache import cache
from django.shortcuts import render


class BlogCache:
    cache_key_dic = defaultdict(list)

    def cache_invalidate(self, prefix):
        cache_keys = BlogCache.cache_key_dic[prefix]
        print(cache_keys)
        try:
            cache.delete_many(cache_keys)
        except Exception as e:
            # TODO logging
            pass
        else:
            del(BlogCache.cache_key_dic[prefix])

    def cache_key(self, request):
        if request.user.is_anonymous():
           user = 'anonymous'
        else:
           user = request.user.id

        q = getattr(request, request.method)
        q.lists()
        urlencode = q.urlencode(safe='()')

        CACHE_KEY = 'cache_%s_%s_%s' % (request.path, user, urlencode)
        return CACHE_KEY

    def cache_per_user(self, ttl=None, prefix=None, cache_post=False):
        def decorator(function):
            def apply_cache(request, *args, **kwargs):
                CACHE_KEY = self.cache_key(request)

                if prefix:
                    CACHE_KEY = '%s_%s' % (prefix, CACHE_KEY)

                if not cache_post and request.method == 'POST':
                    can_cache = False
                else:
                    can_cache = True

                if can_cache:
                    response = cache.get(CACHE_KEY, None)
                else:
                    response = None

                if not response:
                    response = function(request, *args, **kwargs)
                    response.render()

                    if can_cache:
                        try:
                            BlogCache.cache_key_dic[prefix].append(CACHE_KEY)
                            cache.set(CACHE_KEY, response, ttl)
                        except Exception as e:
                            # TODO logging
                            pass
                return response
            return apply_cache
        return decorator

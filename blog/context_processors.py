from itertools import count
from django.db.models import Count, Q

from blog.models import Category, Tag


def common(request):
    context = {
        'categorys':Category.objects.annotate(
            count=Count('post', Q(post__is_publish=True))
        ),
        'tags': Tag.objects.all()
    }
    return context
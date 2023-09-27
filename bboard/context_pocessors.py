from django.contrib.auth.models import User

from bboard.models import Rubric
from bboard.views import count_bb


def rubrics(request):
    return {
        'rubrics': Rubric.objects.all(),
        'count_bb': count_bb(),
        'users': User.objects.all(),
        # 'groups_this_user': request.user.groups.all(),
        'groups_this_user': request.user.groups.values_list('name', flat=True),
    }

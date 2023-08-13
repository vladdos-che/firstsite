from django.urls import path, re_path
from django.views.generic.dates import WeekArchiveView

from bboard.models import Bb
from bboard.views import BbAddView, login, BbByRubricView, BbDetailView, BbIndexView, BbMonthArchiveView, \
    BbRedirectView, BbIndexRedirectView, index, by_rubric, BbLoginRedirectView, BbByRubricByDateView

vals = {
    'name': 'index',
    'beaver': 'бобёр'
}

# urlpatterns = [
#     re_path(r'^$', index, name='index'),
#     re_path(r'^(?P<rubric_id>[0-9]*)/$', by_rubric, vals, name='by_rubric'),
#     re_path(r'^add/$', BbCreateView.as_view(), name='add'),
#     path('login/', login, name='login'),
# ]

urlpatterns = [
    path(r'', index, name='index'),
    path(r'page/<int:page>/', index, name='page'),
    # path('', BbIndexView.as_view(), name='index'),
    path('index/', BbIndexRedirectView.as_view(), name='index_old'),
    path('<int:rubric_id>/', by_rubric, vals, name='by_rubric'),
    # path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    # path('<int:rubric_id>/page/<int:page>/', BbByRubricView.as_view(), name='rubric_page'),
    path('<int:rubric_id>/page/<int:page>/', BbByRubricByDateView.as_view(), name='rubric_page'),  # lesson_20_hw
    # path('add/', BbCreateView.as_view(), name='add'),
    path('add/', BbAddView.as_view(), name='add'),
    # path('add/save/', add_save, name='add_save'),
    # path('add/', add, name='add'),
    # path('add/', add_and_save, name='add'),
    path('login/', login, name='login'),

    path('loginme/', BbLoginRedirectView.as_view(), name='login_me'),  # lesson_16_hw

    path('read/<int:rec_id>/', BbDetailView.as_view(), name='read'),

    path('<int:year>/<int:month>/', BbMonthArchiveView.as_view()),
    path('<int:year>/week/<int:week>/', WeekArchiveView.as_view(
        model=Bb,
        date_field='published',
        context_object_name='bbs',
        template_name='bboard/bb_archive_month.html'
    )),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('detail/<int:year>/<int:month>/<int:day>/<int:pk>/', BbRedirectView.as_view(), name='old_detail'),
]

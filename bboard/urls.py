from django.urls import path, re_path, include
from django.views.decorators.cache import cache_page
from django.views.generic.dates import WeekArchiveView
from rest_framework.routers import DefaultRouter

from bboard.models import Bb
from bboard.views import BbAddView, BbByRubricView, BbDetailView, BbIndexView, BbMonthArchiveView, \
    BbRedirectView, BbIndexRedirectView, index, by_rubric, BbLoginRedirectView, BbByRubricByDateView, \
    IceCreamCreateView, rubrics, bbs, search, CaptchaLibraryView, BbEditView, api_rubrics, api_rubric_detail, \
    APIRubrics, APIRubricDetail, APIRubricViewSet

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

router = DefaultRouter()
router.register('rubrics', APIRubricViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('rubrics/', rubrics, name='rubrics'),

    # path('api/v1/rubrics/', api_rubrics),
    # path('api/v1/rubrics/<int:pk>/', api_rubric_detail),

    # lesson_50 Start
    # path('api/v1/rubrics/', APIRubrics.as_view()),
    # path('api/v1/rubrics/<int:pk>/', APIRubricDetail.as_view()),

    path('api/v1/', include(router.urls)),
    # lesson_50 End

    path('bbs/<int:rubric_id>/', bbs, name='bbs'),
    path('page/<int:page>/', index, name='page'),

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
    path('update/<int:pk>/', BbEditView.as_view(), name='update'),

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

    path('add_icecream/', IceCreamCreateView.as_view(), name='add_icecream'),  # lesson_25_hw

    path('search/', search, name='search'),

    path('captcha_library/', CaptchaLibraryView.as_view(), name='captcha_library'),  # lesson_32_hw
]

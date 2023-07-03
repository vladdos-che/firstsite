from django.urls import path, re_path

from bboard.views import BbAddView, login, BbByRubricView, BbDetailView, BbIndexView

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
    path('', BbIndexView.as_view(), name='index'),
    # path('<int:rubric_id>/', by_rubric, vals, name='by_rubric'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    # path('add/', BbCreateView.as_view(), name='add'),
    path('add/', BbAddView.as_view(), name='add'),
    # path('add/save/', add_save, name='add_save'),
    # path('add/', add, name='add'),
    # path('add/', add_and_save, name='add'),
    path('login/', login, name='login'),
    path('read/<int:rec_id>/', BbDetailView.as_view(), name='read'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
]

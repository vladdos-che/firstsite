from django.urls import path

from testapp.views import AddSms, ReadSms, ReadListSms, index_sms, DeleteSms, UpdateSms, add, edit, index, get, \
    test_cookie, test_mail

app_name = 'testapp'

urlpatterns = [
    path('indexsms/', index_sms, name='index_sms'),
    path('addsms/', AddSms.as_view(), name='add_sms'),
    path('readsms/<int:pk>/', ReadSms.as_view(), name='read_sms'),
    path('readlistsms/', ReadListSms.as_view(), name='read_list_sms'),
    path('deletesms/<int:sms_id>/', DeleteSms.as_view(), name='delete_sms'),
    path('updatesms/<int:pk>/', UpdateSms.as_view(), name='update_sms'),
    path('add/', add, name='add'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('', index, name='index'),
    path('get/<path:filename>/', get, name='get'),
    path('cookie/', test_cookie, name='test_cookie'),  # lesson_41

    path('mail/', test_mail, name='test_mail'),  # lesson_41
]

from django.urls import path

from testapp.views import AddSms, ReadSms, ReadListSms, index_sms, DeleteSms, UpdateSms, add, edit, index, get

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
]

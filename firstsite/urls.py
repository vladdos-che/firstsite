from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bboard.urls')),
    path('auth/', include('authapp.urls', namespace='authapp')),
    path('testapp/', include('testapp.urls', namespace='testapp'), name='testapp'),
    path('sheets/', include('tasksheet.urls')),

    path('accounts/login/', LoginView.as_view(next_page='index'), name='login'),
    # path('accounts/login/?next=index', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/password_change/', PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),
    path('accounts/password_change/done/', PasswordChangeDoneView.as_view(
        template_name='registration/password_changed.html'),
         name='password_change_done'),
]

urlpatterns += [
    path('captcha/', include('captcha.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

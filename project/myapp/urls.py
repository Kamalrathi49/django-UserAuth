from django.urls import path
from django.conf.urls import url
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myapp'
urlpatterns = [
    url(r'^accounts/login/$', views.Login.as_view(), name='login'),
    url(r'^$', views.home, name='home'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^signup/$', views.SignUp.as_view(), name='signup'),
    url(r'^delete_user/(?P<customuser_id>\d+)/$', views.deleteuser, name='delete-user'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
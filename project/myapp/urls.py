from django.urls import path
from django.conf.urls import url
from myapp import views

app_name = 'myapp'
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^delete_user/(?P<user_id>\d+)/$', views.deleteuser, name='delete-user'),
    # url(r'^update-user/(?P<user_id>\d+)/$', views.updateuser, name='update-user'),
]
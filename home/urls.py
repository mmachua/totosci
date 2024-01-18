from django.conf.urls import include, re_path
from .import views
from .views import home


app_name = 'home'

urlpatterns = [
    re_path(r'^home/$', views.home, name='home'),
    #re_path(r'^agent/$', views.agent, name='agent')

]

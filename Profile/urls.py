from django.urls import include, re_path
from Profile.views import ProfileView, allagents
from .import views


app_name = 'Profile'

urlpatterns = [
    re_path(r'^Profile/$', ProfileView.as_view(), name='Profile'),
    re_path(r'^Profile/(?P<pk>\d+)/$', ProfileView.as_view(), name='view_profile_with_pk'),
    re_path(r'^allagents/$', views.allagents, name='allagents'),

]
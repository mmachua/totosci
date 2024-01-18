from django.conf.urls import include, re_path
from .import views
from .views import all_agents, agent, agentadmin ,Post, Messages


app_name = 'agent'

urlpatterns = [
    re_path(r'^all_agents/$', views.all_agents, name='all_agents'),
    re_path(r'^agent/$', views.agent, name='agent'),
    re_path(r'^agentadmin/$', views.agentadmin, name='agentadmin'),
    re_path(r'^post/$', views.Post, name='post'),
    re_path(r'^messages/$', views.Messages, name='messages')

]

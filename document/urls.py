from django.conf.urls import include, re_path
from .import views
from document.views import upload_document


app_name = 'document'

urlpatterns = [
    re_path(r'^upload_document/$', views.upload_document, name='upload_document'),
    #re_path(r'^agent/$', views.agent, name='agent')

]

from django.conf.urls import url
from .views import *

app_name='post'

urlpatterns = [
            url(r'^(?P<id>\d+)/$', index, name='index'),
            ]

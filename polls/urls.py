from django.conf.urls import url

from . import views 

urlpetterns = [
        url(r'^$', views.index, name='index'),
]

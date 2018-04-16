from django.conf.urls import url, include
from urlparts import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
]

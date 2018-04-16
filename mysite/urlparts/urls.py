from django.conf.urls import url, include
from urlparts import views
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^.*$', views.andereurl,name='andereurl'),
]

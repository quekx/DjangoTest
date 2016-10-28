from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^update/$', views.update, name='update'),
    url(r'^page/(?P<page>[0-9]+)/$', views.page, name='page'),
]

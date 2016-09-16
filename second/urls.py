from django.conf.urls import url

from . import views

app_name = 'second'
urlpatterns = [
    # ex: /second/topten
    url(r'^topten$', views.topten, name='topten'),
    # ex: /second/article/link
    url(r'^topten/article/(?P<link>.*)/$', views.article, name='article'),
]
# asteroide/urls.py

from django.conf.urls import url

from asteroide import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^test/$', views.test, name='test'),
  url(r'^profile/$', views.profile, name='profile'),
  url(r'^infoasteroid/$', views.infoasteroid, name='infoasteroid')
]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.move_calendar_default, name='move_calendar'),
    url(r'^(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', views.move_calendar, name='move_calendar'),
    url(r'^(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)/moves/$', views.move_list, name='move_list'),
    url(r'^move/remove/(?P<pk>[0-9]+)/$', views.move_remove, name='move_remove'),
    url(r'^move/(?P<pk>[0-9]+)/edit/$', views.move_edit, name='move_edit'),
    url(r'^move/new/(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$', views.move_new, name='move_new'),
]


from django.conf.urls import include, url

from . import views
from . import consumers

urlpatterns = [
    url(r'^$', views.start_room, name='start_room'),
    url(r'^relase/$', consumers.relase, name='relase'),
    url(r'^room/(?P<label>\w+)/$', views.pick_room, name='pick_room'),
]

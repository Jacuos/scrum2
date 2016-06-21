from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.pick, name='pick'),
    url(r'^tasks/(?P<pk>\w+)/$', views.tasks, name='tasks'),
    url(r'^start_task/(?P<pk>\w+)/$', views.start_task, name='start_task'),
    url(r'^resolve_task/(?P<pk>\w+)/$', views.resolve_task, name='resolve_task'),
]

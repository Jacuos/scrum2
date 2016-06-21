from django.conf.urls import include, url

from . import views


urlpatterns = [
	url(r'^$', views.entries, name='entries'),
	url(r'^(?P<page>\d+)/$', views.entries, name='entries'),
	url(r'^write/$', views.write, name='write'),
	url(r'^(?P<entry_id>\d+)/', include([
		url(r'^remove/$', views.remove, name='remove'),
		url(r'^entry/$', views.entry, name='entry'),
		url(r'^subscribe/$', views.subscribe, name='subscribe'),
		url(r'^like/$', views.like, name='like'),
	]))
]

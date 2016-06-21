from django.conf.urls import url, include

from . import views


urlpatterns = [
	url(r'^$', views.questions, name='questions'),
	url(r'^ask/$', views.ask, name='ask'),
	url(r'^search/$', views.search, name='search'),
	url(r'^settings/$', views.settings, name='settings'),
	url(r'^(?P<question_id>\d+)/', include([
			url(r'^answer/$', views.answer, name='answer'),
			url(r'^ignore/$', views.ignore, name='ignore'),
			url(r'^remove/$', views.remove, name='remove'),
			url(r'^archive/$', views.archive, name='archive'),
			url(r'^details/$', views.details, name='details'),
	]))
]

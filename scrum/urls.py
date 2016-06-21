from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('dashboard.urls', namespace='dashboard')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')), # Django JET dashboard URLS
    url(r'^chat/', include('chat.urls', namespace='chat')),
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^teams/', include('teams.urls', namespace='teams')),
    url(r'^blogs/', include('blogs.urls', namespace='blogs')),
    url(r'^qanda/', include('qanda.urls', namespace='qanda')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
]

admin.site.site_header = 'Scrum management'
